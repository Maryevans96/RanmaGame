import pygame
import random

pygame.init()
pygame.mixer.init()

sfondo = pygame.image.load ('immagini/sfondo.jpg')
base = pygame.image.load ('immagini/base.jpg')
ranmamale = pygame.image.load ('immagini/ranmamale.png')
ranmafem = pygame.image.load ('immagini/ranmafem.png')
akane = pygame.image.load ('immagini/akane.png')
genma = pygame.image.load ('immagini/genma.png')
happosai = pygame.image.load ('immagini/happosai.png')
kuno = pygame.image.load ('immagini/kuno.png')
acquaalta = pygame.image.load ('immagini/acquaalta.png')
acquabassa = pygame.image.load ('immagini/acquabassa.png')
teiera = pygame.image.load ('immagini/teiera.png')
win = pygame.image.load('immagini/win.jpg')
loser = pygame.image.load('immagini/loser.jpg')

ranmacorrente = ranmamale
isranmamale =True

ultimatrasformazione_time= 0
TRANSFORM = 500

SCHERMO = pygame.display.set_mode((960, 720))
FPS = 50
VEL_AVANZ =3

try:
    pygame.mixer.music.load('musica/Ranmasigla.mp3')
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1)
except pygame.error as e:
    print(f"Errore caricamento audio:{e}")

class ostacoli_classe:
    def __init__(self):
        self.x = random.randint(200,500)
        self.y_genma = 440
        self.y_happosai = 0
        self.y_acquaalta = 0
        self.y_acquabassa =440
        self.y_teiera = random.randint(0,400)
        self.y_akane = random.randint(0,400)
        self.y_kuno = random.randint(0,400)
        self.tipo_ostacolo = random.choice(["genma", "happosai", "acquaalta","acquabassa","teiera", "akane", "kuno"])

    def avanza_e_disegna (self):
        self.x -= VEL_AVANZ
        if self.tipo_ostacolo == "genma":
           SCHERMO.blit(genma,(self.x,self.y_genma))
        elif self.tipo_ostacolo == "acquaalta":
            SCHERMO.blit(acquaalta,(self.x,self.y_acquaalta))
        elif self.tipo_ostacolo == "acquabassa":
            SCHERMO.blit(acquabassa, (self.x, self.y_acquabassa))
        elif self.tipo_ostacolo == "happosai":
           SCHERMO.blit(happosai, (self.x, self.y_happosai))
        elif self.tipo_ostacolo == "teiera":
            SCHERMO.blit(teiera,(self.x,self.y_teiera))
        elif self.tipo_ostacolo == "akane":
            SCHERMO.blit(akane,(self.x,self.y_akane))
        elif self.tipo_ostacolo == "kuno":
            SCHERMO.blit(kuno,(self.x,self.y_kuno))

    def collisione(self,ranmamale, ranmamalex, ranmamaley):
        tolleranza_hitbox = 20 # Prova valori più alti (es. 10, 15, 20)

        if self.tipo_ostacolo == "genma":
            ostacolo_img = genma
            ostacolo_y = self.y_genma
        elif self.tipo_ostacolo == "acquabassa":
            ostacolo_img = acquabassa
            ostacolo_y = self.y_acquabassa
        elif self.tipo_ostacolo == "happosai":
            ostacolo_img = happosai
            ostacolo_y = self.y_happosai
        elif self.tipo_ostacolo == "acquaalta":
            ostacolo_img = acquaalta
            ostacolo_y = self.y_acquaalta
        elif self.tipo_ostacolo == "teiera":
            ostacolo_img = teiera
            ostacolo_y = self.y_teiera
        elif self.tipo_ostacolo == "akane":
            ostacolo_img = akane
            ostacolo_y = self.y_akane
        elif self.tipo_ostacolo == "kuno":
            ostacolo_img = kuno
            ostacolo_y = self.y_kuno
        else:
            return

        ranmamale_lato_dx = ranmamalex + ranmamale.get_width() - tolleranza_hitbox  # Riduce a destra
        ranmamale_lato_sx = ranmamalex + tolleranza_hitbox

        # Usa l'immagine e le coordinate corrette
        ostacolo_lato_dx = self.x + ostacolo_img.get_width() - tolleranza_hitbox
        ostacolo_lato_sx = self.x + tolleranza_hitbox

        ranmamale_lato_su = ranmamaley + tolleranza_hitbox # Riduce in alto
        ranmamale_lato_giu = ranmamaley + ranmamale.get_height()

        # Usa l'immagine e le coordinate corrette
        ostacolo_lato_su = ostacolo_y + tolleranza_hitbox
        ostacolo_lato_giu = ostacolo_y + ostacolo_img.get_height() - tolleranza_hitbox

        # Controllo della collisione
        if ranmamale_lato_dx > ostacolo_lato_sx and ranmamale_lato_sx < ostacolo_lato_dx:
            if ranmamale_lato_su < ostacolo_lato_giu and ranmamale_lato_giu > ostacolo_lato_su:
                if self.tipo_ostacolo == "genma" or self.tipo_ostacolo =="happosai":
                    hai_perso()
                elif self.tipo_ostacolo == "acquaalta" or self.tipo_ostacolo == "acquabassa":
                    return trasformazione_fem()
                elif self.tipo_ostacolo == "teiera":
                    return trasformazione_male()
                elif self.tipo_ostacolo == "akane":
                    if ranmacorrente == ranmamale:
                       hai_vinto()
                    elif ranmacorrente == ranmafem:
                        hai_perso()
                elif self.tipo_ostacolo == "kuno":
                    hai_perso()






def aggiorna():
    pygame.display.update()
    pygame.time.Clock().tick(FPS)

def inizializza():
    global ranmamalex, ranmamaley, ranmamale_vely
    global basex
    global ostacoli
    ranmamalex, ranmamaley =60, 150
    ranmamale_vely=0
    basex=0
    ostacoli= []
    ostacoli.append(ostacoli_classe())

def disegna_oggetti():
    SCHERMO.blit(sfondo, (0,0))
    for o in ostacoli:
        o.avanza_e_disegna ()
    SCHERMO.blit(ranmacorrente,(ranmamalex,ranmamaley))
    SCHERMO.blit(base, (basex, 620))
    # Disegna la seconda copia immediatamente dopo
    SCHERMO.blit(base, (basex + 800, 620))

#funzione hai perso se ranmafem incontra kuno
def hai_perso():
    SCHERMO.blit (loser, (200, 180))
    aggiorna()
    ricominciamo =False
    while not ricominciamo:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                inizializza()
                ricominciamo=True
            if event.type == pygame.QUIT:
                pygame.quit()

#funzione hai vinto se ranmamaschio incontra akane
def hai_vinto():
    SCHERMO.blit (win, (200, 180))
    aggiorna()
    ricominciamo =False
    while not ricominciamo:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                inizializza()
                ricominciamo=True
            if event.type == pygame.QUIT:
                pygame.quit()

def trasformazione_fem():
    global ranmacorrente, isranmamale, ultimatrasformazione_time
    tempocorrente = pygame.time.get_ticks()

    if tempocorrente>ultimatrasformazione_time + TRANSFORM:
        if isranmamale:
            ranmacorrente=ranmafem
            isranmamale = False

        ultimatrasformazione_time =tempocorrente
        return True


def trasformazione_male():
    global ranmacorrente, isranmamale, ultimatrasformazione_time
    tempocorrente = pygame.time.get_ticks()

    if tempocorrente>ultimatrasformazione_time + TRANSFORM:
        if not isranmamale:
            ranmacorrente=ranmamale
            isranmamale = True

        ultimatrasformazione_time =tempocorrente
        return True


inizializza()

#ciclo principale
while True:
    basex -= VEL_AVANZ
    if basex < -800: basex = 0
    #movimento
    ranmamale_vely +=1
    ranmamaley += ranmamale_vely

    if ranmamaley >=400:
        ranmamaley = 400

    for event in pygame.event.get():

        if (event.type == pygame.KEYDOWN
                and event.key == pygame.K_UP):
            ranmamale_vely = -10

        if event.type == pygame.QUIT:
            pygame.quit()


    #gestione ostacoli
    if not ostacoli:
        ostacoli.append(ostacoli_classe())

    elif ostacoli [-1].x < 150:
           ostacoli.append(ostacoli_classe())

    ostacolidarimuovere =[]

    for o in ostacoli:
       if o.collisione(ranmacorrente, ranmamalex, ranmamaley):
            ostacolidarimuovere.append(o)

    for o in ostacolidarimuovere:
        if o in ostacoli:
            ostacoli.remove(o)

    #aggiornamento schermo
    disegna_oggetti()
    aggiorna ()


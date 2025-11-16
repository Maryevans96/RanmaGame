import pygame
import random

pygame.init()

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

SCHERMO = pygame.display.set_mode((960, 720))
FPS = 50
VEL_AVANZ =3

class ostacoli_classe:
    def __init__(self):
        self.x = random.randint(200,500)
        self.y_genma = 440
        self.y_happosai = 0
        self.y_acquaalta = 0
        self.y_acquabassa =440
        self.y_teiera = random.randint(0,400)
        self.tipo_ostacolo = random.choice(["genma", "happosai", "acquaalta","acquabassa"])
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
                    trasformazione()
                    return True

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

def trasformazione():
    global ranmacorrente, isranmamale
    if isranmamale:
        ranmacorrente=ranmafem
        isranmamale = False
    elif not isranmamale:
        ranmacorrente =ranmamale
        isranmamale =True




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
    if ostacoli [-1].x < 150: ostacoli.append(ostacoli_classe())
    for o in ostacoli:
        o.collisione(ranmacorrente, ranmamalex, ranmamaley)



    #aggiornamento schermo
    disegna_oggetti()
    aggiorna ()


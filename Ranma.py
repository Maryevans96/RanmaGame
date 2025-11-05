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

SCHERMO = pygame.display.set_mode((960, 720))
FPS = 50
VEL_AVANZ =3
EVENTO_IMMAGINE_FINALE=pygame.USEREVENT+1
pygame.time.set_timer(EVENTO_IMMAGINE_FINALE, 60)

class ostacoli_classe:
    def __init__(self):
        self.x = 500
        self.y = 520
        self.y2 = random.randint (600,720)
    def avanza_e_disegna (self):
        self.x += 20
        SCHERMO.blit(genma,(self.x,self.y))
        SCHERMO.blit(happosai, (self.x, self.y2))
    def collisione(self,ranmamale, ranmamalex, ranmamaley):
        tolleranza = 5

        ranmamale_lato_dx = ranmamalex+ranmamale.get_width ()-tolleranza
        ranmamale_lato_sx = ranmamalex + tolleranza
        genma_lato_dx = self.x + genma.get_width ()
        genma_lato_sx = self.x

        ranmamale_lato_su = ranmamaley+tolleranza
        ranmamale_lato_giu= ranmamaley+ranmamale.get_height ()-tolleranza
        genma_lato_su = self.y
        genma_lato_giu = self.y+ genma.get_height()
        if ranmamale_lato_dx>genma_lato_sx and ranmamale_lato_sx<genma_lato_dx:
            if ranmamale_lato_su<genma_lato_giu and ranmamale_lato_giu > genma_lato_su:
                hai_perso()

    def verifica_Akane(self,ranmamale, ranmamalex, ranmamaley):
        tolleranza = 5

        ranmamale_lato_dx = ranmamalex+ranmamale.get_width ()-tolleranza
        ranmamale_lato_sx = ranmamalex + tolleranza
        akane_lato_dx = self.x + akane.get_width ()
        akane_lato_sx = self.x

        ranmamale_lato_su = ranmamaley+tolleranza
        ranmamale_lato_giu= ranmamaley+ranmamale.get_height ()-tolleranza
        akane_lato_su = self.y
        akane_lato_giu = self.y+ akane.get_height()
        if ranmamale_lato_dx>akane_lato_sx and ranmamale_lato_sx<akane_lato_dx:
            if ranmamale_lato_su<akane_lato_giu and ranmamale_lato_giu > akane_lato_su:
                hai_vinto()


def aggiorna():
    pygame.display.update()
    pygame.time.Clock().tick(FPS)

def inizializza():
    global ranmamalex, ranmamaley, ranmamale_vely
    global basex
    global ostacoli
    global gioco_attivo
    ranmamalex, ranmamaley =60, 150
    ranmamale_vely=0
    basex=0
    ostacoli= []
    ostacoli.append(ostacoli_classe())
    gioco_attivo = True


def disegna_oggetti():
    SCHERMO.blit(sfondo, (0,0))
    for o in ostacoli:
        o.avanza_e_disegna ()
    SCHERMO.blit(ranmamale, (ranmamalex,ranmamaley))
    SCHERMO.blit(base, (basex, 620))
    # Disegna la seconda copia immediatamente dopo
    SCHERMO.blit(base, (basex + 800, 620))

#funzione hai perso se ranmafem incontra kuno
def hai_perso():
    SCHERMO.blit (loser, (200, 180))
    aggiorna()
    ricominciamo=False
    while not ricominciamo:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                inizializza()
                ricominciamo=True
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == EVENTO_IMMAGINE_FINALE:
                if ranmamale==ranmamale:
                    immagine=akane


def hai_vinto():
    SCHERMO.blit(win, (200, 180))
    aggiorna()
    ricominciamo = False
    while not ricominciamo:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                inizializza()
                ricominciamo = True
            if event.type == pygame.QUIT:
                pygame.quit()

#inizializzo le variabili
inizializza()

#ciclo principale
while gioco_attivo:
    basex -= VEL_AVANZ
    if basex < -800: basex = 0
    #movimento
    ranmamale_vely +=1
    ranmamaley += ranmamale_vely

    if ranmamaley >=400:
        ranmamaley=400
    for event in pygame.event.get():
        if (event.type == pygame.KEYDOWN
            and event.key == pygame.K_UP):
            ranmamale_vely = -10
        if event.type == pygame.QUIT:
            pygame.quit()


    #gestione ostacoli
    if ostacoli [-1].x < 200: ostacoli.append(ostacoli_classe())
    for o in ostacoli:
        o.collisione(ranmamale, ranmamalex, ranmamaley)

    #collisione Akane
    if verifica_Akane():
        gioco_attivo=False
        hai_vinto()


    #aggiornamento schermo
    disegna_oggetti()
    aggiorna ()


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

class oggetti_giu_classe:
    def _init_(self):
        self.x = 300
        self.y = 400
    def avanza_e_disegna (self):
        self.x -= VEL_AVANZ
        SCHERMO.blit(genma,(self.x,self.y))

def aggiorna():
    pygame.display.update()
    pygame.time.Clock().tick(FPS)

def inizializza():
    global ranmamalex, ranmamaley, ranmamale_vely
    global basex
    ranmamalex, ranmamaley =60, 150
    ranmamale_vely=0
    basex=0


def disegna_oggetti():
    SCHERMO.blit(sfondo, (0,0))
    SCHERMO.blit(ranmamale, (ranmamalex,ranmamaley))
    SCHERMO.blit(base, (basex, 620))
    # Disegna la seconda copia immediatamente dopo
    SCHERMO.blit(base, (basex + 800, 620))

#funzione hai perso se ranmafem incontra kuno
def hai_perso():
    SCHERMO.blit (loser (50, 180))
    aggiorna()

#inizializzo le variabili
inizializza()

#ciclo principale
while True:
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



    #aggiornamento schermo
    disegna_oggetti()
    aggiorna ()


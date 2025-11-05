import pygame
import random

pygame.init()

sfondo = pygame.image.load ('immagini/sfondo.jpg')
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

SCHERMO = pygame.display.set_mode((736, 552))
FPS = 50

def aggiorna():
    pygame.display.update()
    pygame.time.Clock().tick(FPS)



def inizializza():
    global ranmamalex, ranmamaley, ranmamale_vely
    ranmamalex, ranmamaley =60, 150
    ranmamale_vely=0

def disegna_oggetti():
    SCHERMO.blit(sfondo, (0,0))
    SCHERMO.blit(ranmamale, (ranmamalex,ranmamaley))
inizializza()

while True:
    ranmamale_vely +=1
    ranmamaley += ranmamale_vely
    disegna_oggetti()
    aggiorna ()


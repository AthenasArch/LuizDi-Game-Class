import time
import pygame
from pygame.locals import *
import sys

pygame.init()

RGB_COLOR_BLACK =       (000, 000, 000)
RGB_COLOR_RED =         (255, 000, 000)
RGB_COLOR_GREEN =       (000, 255, 000)
RGB_COLOR_NEW_GREEN =   (128, 255, 40 )
RGB_COLOR_BLUE =        (000, 000, 255)
RGB_COLOR_CYAN =        (000, 255, 255)
RGB_COLOR_MAGENTA =     (255, 000, 255)
RGB_COLOR_YELLOW =      (255, 255, 000)
RGB_COLOR_GRAY =        (128, 128, 128)

# contantes do projeto
SCREEN_WIDTH = 400
SCREEN_HIGHT = 450
SCREEN_TITLE = "LuizDi-Game V2"

FPS = 60

framePerSec = pygame.time.Clock()

# cria a tela
pygame.display.set_caption(SCREEN_TITLE)
displaySurface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # caracteristicas do personagem
        self.size = (30, 30)
        self.color = RGB_COLOR_BLUE
        self.iniPosition = (100, 420)

        # inicializamos o personagem
        self.surf = pygame.Surface((self.size))
        self.surf.fill(self.color)
        self.rect = self.surf.get_rect(center = (self.iniPosition)) 

class Platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # caracteristicas da plataforma
        self.size = (SCREEN_WIDTH, 20)
        self.color = RGB_COLOR_RED
        self.iniPosition = (SCREEN_WIDTH/2, SCREEN_HIGHT - 10)

        # inicializamos o personagem
        self.surf = pygame.Surface((self.size))
        self.surf.fill(self.color)
        self.rect = self.surf.get_rect(center = (self.iniPosition)) 

def main():
    BackgroundColor = RGB_COLOR_BLACK

    # cria uma instancia para o personagem
    P1 = Player()

    # cria uma instancia para a maior plataforma inferior
    PT1 = Platform()

    all_sprites = pygame.sprite.Group()

    # adiciona todos os sprites a lista
    all_sprites.add(PT1)    
    all_sprites.add(P1)

    while True:
        # trata os eventos
        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit() # finaliza o pygame
                sys.exit() # fecha o aplicativo

        displaySurface.fill(BackgroundColor) # seta cor de fundo da tela

        for entity in all_sprites:
            # desenha apartir da lista de sprites, as posicoes dos sprites
            displaySurface.blit(entity.surf, entity.rect) 

        # atualiza o conteudo do jogo
        pygame.display.update()

        # controla a taxa de atualizacoes do jogo para nao passar de FPS (60)
        framePerSec.tick(FPS)

if __name__ == "__main__":
    main()
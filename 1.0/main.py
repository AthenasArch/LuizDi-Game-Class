"""
------------------------------------------------------------------------------------------
AthenasArch.com
Nome do Jogo: <Luiz-Di Game>
Versão: 2.0
Data de Criação: 21/05/2023
Desenvolvedor: Leonardo Hilgemberg Lopes
Descrição: Jogo de plataforma, com personagem, plataformas, audios e gritaria.

Este script foi criado como parte de uma aula de programação em Python.

Baseado no tutorial: https://coderslegacy.com/python/pygame-platformer-game-development/

Aulas:

1.0 - Criando a janela, plataforma e o personagem.
------------------------------------------------------------------------------------------
"""

# importa as bibliotecas
import pygame
from pygame.locals import * # arquivos de definicoes
import sys

# Tabela RGB de Cores
RGB_COLOR_BLACK = (0, 0, 0)
RGB_COLOR_RED = (255, 0, 0)
RGB_COLOR_GREEN = (0, 255, 0)
RGB_COLOR_NEW_GREEN = (128,255,40)
RGB_COLOR_BLUE = (0, 0, 255)
RGB_COLOR_CYAN = (0, 255, 255)
RGB_COLOR_MAGENTA = (255, 0, 255)
RGB_COLOR_YELLOW = (255, 255, 0)
RGB_COLOR_GRAY = (128, 128, 128)

pygame.init()

#constantes do projto:
SCREEN_HEIGHT = 450 # Altura
SCREEN_WIDTH = 400 # Largura
SCREEN_TITLE = "LUIZ-DI GAME V1"

# Contantes de jogabilidade e gravidade
FPS = 60 # Frequencia de atualizacao, frames por segundo


FramePerSec = pygame.time.Clock()
 
# instanciamos a tela de forma global:
displaysurface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #inicializa a tela
pygame.display.set_caption(SCREEN_TITLE) # nome da janela

# Classe do jogador
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 

        # caracteristicas do personagem:
        self.size = (30, 30)
        self.color = RGB_COLOR_BLUE
        self.iniPosition = (100, 420)

        # inicializa o personagem
        self.surf = pygame.Surface((self.size))
        self.surf.fill(self.color)
        self.rect = self.surf.get_rect(center = (self.iniPosition))
 
# classe das plataformas
class Platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        # caracteristicas do personagem:
        self.size = (SCREEN_WIDTH, 20) # pega a largura total da tela no comprimento e passa 10px na altura. 
        self.color = RGB_COLOR_RED
        self.iniPosition = (SCREEN_WIDTH/2, SCREEN_HEIGHT - 10)

        self.surf = pygame.Surface(self.size)
        self.surf.fill(self.color)
        self.rect = self.surf.get_rect(center = self.iniPosition) # definimos um retangulo e setamos os pontos apartir do centro dele
 

# Função principal do jogo
def main():

    backgroundColor = RGB_COLOR_BLACK

    # Cria uma instância da classe Player e atribui à variável P1
    P1 = Player()

    # Cria uma instância da classe Platform e atribui à variável PT1
    PT1 = Platform()

    # Cria um grupo de sprites (objetos do jogo) 
    all_sprites = pygame.sprite.Group()

    # Adiciona a plataforma e o jogador ao grupo de sprites
    all_sprites.add(PT1)
    all_sprites.add(P1)
    
    # Loop infinito do jogo
    while True:
        # Loop que percorre a lista de todos os eventos que ocorreram
        for event in pygame.event.get():
            
            # Se o evento for do tipo QUIT (ou seja, se a janela do jogo foi fechada), termina o jogo
            if event.type == QUIT:
                pygame.quit() # Finaliza o pygame
                sys.exit() # Fecha o aplicativo

        # Preenche a tela de jogo com preto
        displaysurface.fill(backgroundColor)
    
        # Loop que percorre todos os sprites
        for entity in all_sprites:
            # Desenha cada sprite na tela de jogo nas posições definidas por seus retângulos
            displaysurface.blit(entity.surf, entity.rect)
    
        # Atualiza o conteúdo da tela de jogo
        pygame.display.update()

        # Controla a taxa de atualização do jogo para não passar de 'FPS' frames por segundo
        FramePerSec.tick(FPS)

# Verifica se este arquivo está sendo executado diretamente (em vez de importado como um módulo)
# Se sim, chama a função main()
if __name__ == "__main__":
    main()

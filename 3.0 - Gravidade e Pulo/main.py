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
2.0 - Movimento lateral e gravidade horizontal.
3.0 - Pulo livre do personagem.
6.0 - Adicionando Game Over do jogo se sair para fora da tela
6.1 - Sistema de pontuacao.
6.2 - Criando uma classe para gerenciar as operacoes da main
      E organizar o script
6.3 - Plataforma movel

7.0 - Movimento do jogador e da plataforma
------------------------------------------------------------------------------------------
"""
import pygame
from pygame.locals import *
import sys
 
pygame.init()
vec = pygame.math.Vector2  # Trata o vetor de 2 dimensoes 

RGB_COLOR_BLACK = (0, 0, 0)
RGB_COLOR_RED = (255, 0, 0)
RGB_COLOR_GREEN = (0, 255, 0)
RGB_COLOR_NEW_GREEN = (128,255,40)
RGB_COLOR_BLUE = (0, 0, 255)
RGB_COLOR_CYAN = (0, 255, 255)
RGB_COLOR_MAGENTA = (255, 0, 255)
RGB_COLOR_YELLOW = (255, 255, 0)
RGB_COLOR_GRAY = (128, 128, 128)

#constantes do projto:
SCREEN_HEIGHT = 450
SCREEN_WIDTH = 400
SCREEN_TITLE = "LUIZ-DI GAME V1"

# Contantes de jogabilidade e gravidade
FPS = 60 # Frequencia de atualizacao, frames por segundo
ACC = 0.5 # isso aqui e o movimento de aceleracao do personagem
FRIC = -0.12

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
        iniPos_x = SCREEN_WIDTH/2 # o personagem no meio da tela em X
        iniPos_y = 0 
        self.iniPosition = (iniPos_x, iniPos_y) # 

        # inicializa o personagem
        self.surf = pygame.Surface((self.size))
        self.surf.fill(self.color)
        self.rect = self.surf.get_rect(center = (self.iniPosition))
 
        # aqui e referente ao movimento do personagem
        self.pos = vec((SCREEN_WIDTH/2, iniPos_y))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
    
    def update(self, P1, platforms):
        # P1 - O primeiro parâmetro usa um único sprite como entrada, 
        #   como nosso player sprite, P1.
        #
        # platforms - O segundo parâmetro leva um sprite_grouplike all_sprites. 
        #   Essa função verifica se o sprite no primeiro parâmetro 
        #   está tocando em algum dos sprites no arquivo sprite_group.
        #
        # False - O último parâmetro assume um valor True ou False, dependendo
        #   se você deseja que o sprite seja excluído ou não após uma colisão. 
        #   (Mantenha este falso para a maioria dos casos).
        #
        # hits = pygame.sprite.spritecollide(P1 , platforms, False)
        # if hits:
        #     self.pos.y = hits[0].rect.top + 1
        #     self.vel.y = 0

        hits = pygame.sprite.spritecollide(P1 ,platforms, False)
        if P1.vel.y > 0:        
            if hits:
                self.vel.y = 0
                self.pos.y = hits[0].rect.top + 1

    def jump(self, platforms):
        # isso aqui, faz com que o personagem so pule quando estiver em contato com o chao
        # hits = pygame.sprite.spritecollide(self, platforms, False)
        # if hits:
        self.vel.y = -15

    def move(self, screenLimit):
        # Inicializa a aceleração como um vetor nulo
        ACC_X = 0 # Aceleracao horizontal em X
        ACC_Y = 0.5 # Aceleracao Vertical em Y, isso foi criado para esse jogo
        # essa aceleracao em Vertical, pode ser considerada como gravidade
        self.acc = vec(ACC_X, ACC_Y) 
    
        # Verifica quais teclas estão sendo pressionadas
        pressed_keys = pygame.key.get_pressed()
                
        # Se a tecla de seta para esquerda está pressionada, acelera para a esquerda
        if pressed_keys[K_LEFT]:
            self.acc.x = -ACC

        # Se a tecla de seta para direita está pressionada, acelera para a direita
        if pressed_keys[K_RIGHT]:
            self.acc.x = ACC  

        # Aplica a fricção ao movimento, reduzindo a aceleração
        self.acc.x += self.vel.x * FRIC

        # Atualiza a velocidade e posição do personagem de acordo com a aceleração
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc


        # Isso aqui faz o personagem ir de um lado da tela e aparecer no outro lado
        # caso nao queira seguir assim, pode seguir sistema regular de movimento
        if self.pos.x > SCREEN_WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = SCREEN_WIDTH

        # Atualiza a posição do retângulo do personagem para corresponder à posição calculada
        self.rect.midbottom = self.pos

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

    platforms = pygame.sprite.Group()
    platforms.add(PT1)

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
                print("Saiu ao pressionar fechar na tela")
                pygame.quit() # Finaliza o pygame
                sys.exit() # Fecha o aplicativo
            elif event.type == pygame.KEYDOWN:  # Verifica se alguma tecla foi pressionada
                if event.key == pygame.K_ESCAPE:  # Verifica se a tecla pressionada foi a ESC
                    print("Saiu ao pressionar ESC")
                    pygame.quit()
                    sys.exit()

            # trata o pulo do animal kkkk
            if event.type == pygame.KEYDOWN:    
                if event.key == pygame.K_SPACE:
                    P1.jump(platforms)

        # Preenche a tela de jogo com preto
        displaysurface.fill(backgroundColor)
    
        # Loop que percorre todos os sprites
        for entity in all_sprites:
            # Desenha cada sprite na tela de jogo nas posições definidas por seus retângulos
            displaysurface.blit(entity.surf, entity.rect)
    
        P1.update(P1, platforms)
        P1.move(True)
        # Atualiza o conteúdo da tela de jogo
        pygame.display.update()

        # Controla a taxa de atualização do jogo para não passar de 'FPS' frames por segundo
        FramePerSec.tick(FPS)

# Verifica se este arquivo está sendo executado diretamente (em vez de importado como um módulo)
# Se sim, chama a função main()
if __name__ == "__main__":
    main()

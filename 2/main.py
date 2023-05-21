#   *************************************************************
#
# atualizado por leonardo hilgemberg lopes.
# Empresa: AthenasArch.
#
# adicionar movimento do personagem
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
        self.iniPosition = (100, 420)

        # inicializa o personagem
        self.surf = pygame.Surface((self.size))
        self.surf.fill(self.color)
        self.rect = self.surf.get_rect(center = (self.iniPosition))
 
        # aqui e referente ao movimento do personagem
        self.pos = vec((10, 385))
        self.vel = vec(0,0)
        self.acc = vec(0,0)

    def move(self, screenLimit = False):
        # Inicializa a aceleração como um vetor nulo
        self.acc = vec(0,0)
    
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

        # Aqui podemos tratar o movimento do personagem na tela de duas formas.
        # limitando o personagem em um espaco conhecido da tela
        # deixando o personagem chegar em um lado e travar ele no limite da tela
        if (screenLimit == False):
            # Isso aqui faz o personagem ir de um lado da tela e aparecer no outro lado
            # caso nao queira seguir assim, pode seguir sistema regular de movimento
            if self.pos.x > SCREEN_WIDTH:
                self.pos.x = 0
            if self.pos.x < 0:
                self.pos.x = SCREEN_WIDTH
        else:
            # Limita o movimento do personagem dentro da tela
            if self.pos.x > SCREEN_WIDTH:
                self.pos.x = SCREEN_WIDTH
            if self.pos.x < 0:
                self.pos.x = 0
     
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

        # Preenche a tela de jogo com preto
        displaysurface.fill(backgroundColor)
    
        # Loop que percorre todos os sprites
        for entity in all_sprites:
            # Desenha cada sprite na tela de jogo nas posições definidas por seus retângulos
            displaysurface.blit(entity.surf, entity.rect)
    
        P1.move(True)
        # Atualiza o conteúdo da tela de jogo
        pygame.display.update()

        # Controla a taxa de atualização do jogo para não passar de 'FPS' frames por segundo
        FramePerSec.tick(FPS)

# Verifica se este arquivo está sendo executado diretamente (em vez de importado como um módulo)
# Se sim, chama a função main()
if __name__ == "__main__":
    main()

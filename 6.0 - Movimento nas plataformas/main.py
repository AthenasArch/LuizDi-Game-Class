#   *************************************************************
#
# atualizado por leonardo hilgemberg lopes.
# Empresa: AthenasArch.
#
# Adicionando Game Over do jogo se sair para fora da tela
import pygame
from pygame.locals import *
import sys
import random
import time
 
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

        # vai tratar o nivel de pulo do jogador
        self.jumping = False

        # caracteristicas do personagem:
        self.size = (30, 30)
        self.color = RGB_COLOR_BLUE
        iniPos_x = SCREEN_WIDTH/2 # o personagem no meio da tela em X
        iniPos_y = 430 
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

        hits = pygame.sprite.spritecollide(self ,platforms, False)
        if self.vel.y > 0:        
            if hits:
                # Esse comando novo remove o bug do personagem subir a linha magicamente sem ter passado ela
                if self.pos.y < hits[0].rect.bottom:               
                    self.pos.y = hits[0].rect.top +1
                    self.vel.y = 0
                    self.jumping = False

        # hits = pygame.sprite.spritecollide(P1 ,platforms, False)
        # if P1.vel.y > 0:        
        #     if hits:
        #         self.vel.y = 0
        #         self.pos.y = hits[0].rect.top + 1

    def jump(self, platforms):
        # isso aqui, faz com que o personagem so pule quando estiver em contato com o chao
        hits = pygame.sprite.spritecollide(self, platforms, False)
        # if hits and not self.jumping:
        if hits: 
           self.jumping = True
           self.vel.y = -15

    def cancel_jump(self):
        if self.jumping:
            if self.vel.y < -3:
                self.vel.y = -3

    def move(self, screenLimit = False):
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
        self.size = (random.randint(50,100), 12) # pega a largura total da tela no comprimento e passa 10px na altura. 
        self.color = RGB_COLOR_RED
        self.iniPosition = (random.randint(0, SCREEN_WIDTH-10), random.randint(0, SCREEN_HEIGHT-30))

        self.surf = pygame.Surface(self.size)
        self.surf.fill(self.color)
        self.rect = self.surf.get_rect(center = self.iniPosition) # definimos um retangulo e setamos os pontos apartir do centro dele

    def check(self, platform, groupies):
        if pygame.sprite.spritecollideany(platform,groupies):
            return True
        else:
            for entity in groupies:
                if entity == platform:
                    continue
                if (abs(platform.rect.top - entity.rect.bottom) < 50) and (abs(platform.rect.bottom - entity.rect.top) < 50):
                    return True
            C = False


    # Gerador de plataformas futuras.
    # Se começa a gerar, caso tenha menos de 7 plataformas    
    # 
    # def plat_gen(self, platforms, all_sprites):
    #     while len(platforms) < 6 :
    #         width = random.randrange(50,100)
    #         p  = Platform()      
    #         C = True
            
    #         # while C:           
    #         #     p = Platform()
    #         #     p.rect.center = (random.randrange(0, SCREEN_WIDTH - width),
    #         #                     random.randrange(-50, 0))
    #             # C = self.check(p, platforms)
    
    #         platforms.add(p)
    #         all_sprites.add(p)
    def plat_gen(self, platforms, all_sprites):
        while len(platforms) < 7 :
            # aqui geramos uma plataforma aleatoria dentro desse comprimento.
            width = random.randrange(50,100)
            p  = Platform()             
            # adiciona essas novas plataformas geradas dentro da tela
            p.rect.center = (random.randrange(0, SCREEN_WIDTH - width), random.randrange(-50, 0))
            platforms.add(p)
            all_sprites.add(p)


    # vamos adicionar movimento as plataformas
    def mov(self):
        pass

# Função principal do jogo
def main():
    backgroundColor = RGB_COLOR_BLACK

    # Cria uma instância da classe Player e atribui à variável P1
    P1 = Player()

    # Cria uma instância da classe Platform e atribui à variável PT1
    PT1 = Platform()
    PT1.surf = pygame.Surface((SCREEN_WIDTH, 20))
    PT1.surf.fill(RGB_COLOR_CYAN)
    PT1.rect = PT1.surf.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT - 10))


    platforms = pygame.sprite.Group()
    platforms.add(PT1)
    
    # Cria um grupo de sprites (objetos do jogo) 
    all_sprites = pygame.sprite.Group()

    # Adiciona a plataforma e o jogador ao grupo de sprites
    all_sprites.add(PT1)
    all_sprites.add(P1)

    for x in range(random.randint(5, 6)):
        pl = Platform()
        platforms.add(pl)
        all_sprites.add(pl)

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

            # trata o pulo do personagem
            if event.type == pygame.KEYDOWN:    
                if event.key == pygame.K_SPACE:
                    P1.jump(platforms)
            if event.type == pygame.KEYUP:    
                if event.key == pygame.K_SPACE:
                    P1.cancel_jump()  

        # Preenche a tela de jogo com preto
        displaysurface.fill(backgroundColor)
    
        # Loop que percorre todos os sprites
        for entity in all_sprites:
            # Desenha cada sprite na tela de jogo nas posições definidas por seus retângulos
            displaysurface.blit(entity.surf, entity.rect)

        # Isso aqui trata a fisica das plataformas
        # 1 - elimina as plataformas quando elas estao abaixo da tela
        # 2 - se a altura do personagem for maior que 1/3 da tela, sobe a tela
        # 3 - atualizamos a posicao do boneco e dos sprites
        if P1.rect.top <= SCREEN_HEIGHT / 3:
            P1.pos.y += abs(P1.vel.y)
            for plat in platforms:
                plat.rect.y += abs(P1.vel.y)
                if plat.rect.top >= SCREEN_HEIGHT:
                    plat.kill()

        P1.update(P1, platforms)
        P1.move(True)
        PT1.plat_gen(platforms, all_sprites)

        # trata o game over se ele cair abaixo do limite da tela
        if P1.rect.top > SCREEN_HEIGHT:
            for entity in all_sprites:
                entity.kill()
            time.sleep(1)

            # Configuração do texto
            font = pygame.font.Font(None, 36) # Define a fonte e o tamanho
            text = font.render('SE FODEU', True, (255, 255, 255)) # Cria o texto, (255, 255, 255) é a cor do texto em RGB (branco)
            text_rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)) # Define a posição do texto (centro da tela)
            
            # Atualiza a tela
            displaysurface.fill((RGB_COLOR_RED))
            displaysurface.blit(text, text_rect) # Desenha o texto na tela
            pygame.display.update()

            # Espera um tempo e fecha o jogo
            time.sleep(1)
            pygame.quit()
            sys.exit()

        # Atualiza o conteúdo da tela de jogo
        pygame.display.update()

        # Controla a taxa de atualização do jogo para não passar de 'FPS' frames por segundo
        FramePerSec.tick(FPS)

# Verifica se este arquivo está sendo executado diretamente (em vez de importado como um módulo)
# Se sim, chama a função main()
if __name__ == "__main__":
    main()




# if P1.rect.top <= SCREEN_HEIGHT / 3:
#     P1.pos.y += abs(P1.vel.y)
#     for plat in platforms:
#         plat.rect.y += abs(P1.vel.y)
#         if plat.rect.top >= SCREEN_HEIGHT:
#             plat.kill()
# Devido à sua complexidade e importância, vamos examiná-lo linha por linha.

# if P1.rect.top <= SCREEN_HEIGHT / 3:
#   Este é um conceito importante para entender. Ele verifica a posição do jogador 
#   em relação à tela. Este é basicamente o ponto decisivo para quando mover a tela 
#   para cima. Depois de alguns testes com o tamanho da tela, velocidade do player, 
#   etc., decidimos definir esse ponto para SCREEN_HEIGHT / 3.

# Toda vez que a posição do jogador atingir o SCREEN_HEIGHT / 3 ponto, o 
#   código dentro dele if statementserá executado.

# P1.pos.y += abs(P1.vel.y)
#
#   Como nossa tela não é mais um objeto dinâmico, temos que atualizar a posição do 
#   jogador conforme a tela se move. Usamos a função abs() para remover o sinal negativo 
#   do valor da velocidade.

# for plat in platforms:
#       plat.rect.y += abs(P1.vel.y)
# 
#   Atualizamos a posição do jogador, mas temos que fazer o mesmo para todos os outros 
#   sprites na tela. Aqui, iteramos por todas as plataformas no grupo de plataformas e 
#   também atualizamos suas posições.

# if plat.rect.top >= HEIGHT:
#        plat.kill()
# 
# Isso destrói todas as plataformas que saem da tela por baixo. Se não fosse por essa linha, 
#   o número de plataformas na memória continuaria se acumulando, tornando o jogo mais lento.




# Parte 5 - Melhorias
# - Consertando como o Player pousa em uma plataforma
# - Melhorando a mecânica do salto
# - Melhorando a geração de plataformas (colisões entre plataformas)
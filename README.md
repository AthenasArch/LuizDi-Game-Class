# LuizDi-Game-Class

### :wolf: Leonardo Hilgemberg, criador da AthenasArch
**`Hoje falaremos sobre o jogo que me gerou 950.000 vizualizações no Instagram.`**
**`Como criar um jogo em python - com jogo de pataforma de sucesso no instagram, o LuizDi-Game-V2.`**

#

<p align="center">
  <img src="https://github.com/AthenasArch/LuizDi-Game-Class/blob/71e2644d568c4d7740da9e8139f3528e9bb8104d/Doc/Gif/LuizDi.gif" alt="LunarLander GIF" width="300" />
</p>

#

# palavras e conceitos comuns que você pode encontrar ao desenvolver jogos com Pygame:
  - Surface: No Pygame, uma Surface é qualquer imagem carregada em memória ou qualquer imagem criada por código que será desenhada na tela.

  - Rect: Uma classe para representar objetos retangulares. É usado para manipular áreas retangulares de imagens e para detectar colisões entre sprites (se os Rects de dois sprites se sobrepõem, eles estão colidindo).

  - Blit: Esta é a operação de desenhar uma imagem (ou Surface) em outra imagem. Normalmente você desenha (ou "blit") seus sprites na tela.

  - Event: Eventos são como o Pygame lida com entrada do usuário - como cliques de mouse, pressionamentos de teclas e outros.

  - Tick: Um "tick" é uma única iteração do loop principal do jogo. A função pygame.time.Clock.tick(fps) pode ser usada para controlar a taxa de quadros do jogo.

  - Group: No Pygame, um Group é uma coleção de sprites. Isso é útil para atualizar ou desenhar muitos sprites de uma vez, ou para detectar colisões entre grupos de sprites.

# INFORMAÇÕES DE VERSÃO E CRIAÇÃO:
- AthenasArch.com
- Nome do Jogo: <Luiz-Di Game>
- Versão: 2.0
- Data de Criação: 21/05/2023
- Desenvolvedor: Leonardo Hilgemberg Lopes
- Descrição: Jogo de plataforma, com personagem, plataformas, audios e gritaria.

Este script foi criado como parte de uma aula de programação em Python.

Baseado no tutorial: https://coderslegacy.com/python/pygame-platformer-game-development/

# CONTEUDO:
    1.0 - Criando a janela, plataforma e o personagem.
    2.0 - Movimento lateral e gravidade horizontal.
    3.0 - Pulo livre do personagem.
    3.1 - Limitando a tela.
    3.2 - Personagem so pula quando está em contato com a plataforma.
    4.0 - Adicionando uma determinada quantidade de plataformas ao inicio do jogo.
    4.1 - Ao subir uma determinada altura da tela, mantemos sempre uma quantidade 
            de 5 ou 6 plataformas na tela, se for menor do que isso,
            gera novas plataformas.
    5.0 - Ajuste nas distancias entre plataformas pequenas geradas.
    5.1 - Resolvido o problema de bug do pulo da plataforma, agora ele só 
            fica na proxima plataforma, se o valor do personagem for maior 
            so que a base perior da plataforma.
    6.0 - Adicionando Game Over do jogo se sair para fora da tela
    6.1 - Sistema de pontuacao.
    6.2 - Criando uma classe para gerenciar as operacoes da main
            E organizar o script.
    6.3 - Plataforma movel.
    7.0 - Personagem agora vai se movimentar junto com a plataforma.
    7.1 - Adicionando Coins (Moedas ao jogo), forma de melhorar a pontuacao
    7.2 - Adicionando as imagens de fundo, do personagem e da plataforma
    8.0 - Adicionando audios no jogo.
    9.0 - Efeito de neve.
    9.1 - Melhorando o efeito de neve.
    9.2 - Vamos adicionando neve conforme a pontuacao vai aumentando, 
            mas só preencho com neve até um determinado limite.
    10.0 - Melhorias no jogo:
        A - Ajustando o game over.
        B - Melhoria na distancia entre as plataformas.

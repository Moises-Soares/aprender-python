# Modulos sao arquivos que contem funcoes que podem ser usadas em outros programas
# Para usar um modulo, voce deve importa-lo
# Neste caso pygame é um modulo que contem funcoes para criar jogos
import pygame
import sys
import random

# Inicializa o pygame
pygame.init()

# Constantes são variaveis que não mudam
# Normalmente escrevemos constantes em letras maiusculas
# Neste caso, definimos algumas cores
# Em Python, as cores são definidas como uma tupla (red, green, blue) chamado RGB
# Cada cor tem um valor de 0 a 255
# As cores primarias são vermelho, verde e azul
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# constante para a largura e altura da tela
LARGURA = 800
ALTURA = 600

# Cria um ecran com 
screen = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Titulo do jogo")

# Ciclo principal
# O ciclo principal serve para manter o jogo a rodar
# O jogo so termina quando o jogador fecha a janela

aCorrer = True
while aCorrer:
    # ignora isto por enquanto
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            aCorrer = False

    # Preenche o fundo com branco
    screen.fill(WHITE)

    # Desenhar um retangulo
    pygame.draw.rect(screen, RED, (50, 50, 100, 100))  
    # Desenhar um circulo
    # pygame.draw.circle(screen, GREEN, (200, 150), 50) 
    # Desenhar uma linha 
    # pygame.draw.line(screen, BLUE, (300, 50), (500, 50), 5)

    # Desenhar uma elipse
    # pygame.draw.ellipse(screen, BLACK, (100, 300, 150, 100))

    # Desengar um poligono
    # pygame.draw.polygon(screen, RED, [(400, 300), (350, 400), (450, 400)])

    # Atualizar o ecran com as figuras desenhadas
    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()


# Faz as seguintes alteracoes:
# 1. Desenha um circulo verde
# 2. Desenha uma linha azul
# 3. Desenha uma elipse preta
# 4. Desenha um poligono vermelho
# 5. Desenha um retangulo vermelho
# 6. Desenha um circulo verde
# 7. Desenha uma linha azul
# 8. Desenha uma elipse preta
# 9. Desenha um poligono vermelho
# 10. Desenha um retangulo vermelho
# 11. Desenha um circulo verde
# 13. Desenha a bandeira da França
# 14. Desenha a bandeira da Alemanha
# 15. Desenha a bandeira da Italia
# 16. Desenha a bandeira do Japao




# Muito bem, aprendeste os seguintes conceitos de programacao:
# 1. Variaveis - sao usadas para guardar valores (aCorrer)
# 2. Constantes - sao variaveis que nao mudam (WHITE, BLACK, RED, GREEN, BLUE)
# 3. Tuplas - sao variaveis que guardam varios valores (255, 255, 255
# 4. Funcoes - sao blocos de codigo que podem ser usados varias vezes (pygame.draw.rect)
# 5. Modulos - sao arquivos que contem funcoes que podem ser usadas em outros programas (pygame)
# 6. Ciclos - é um bloco de codigo que se repete (while aCorrer)
# No proximo tutorial vamos aprender a mover as figuras


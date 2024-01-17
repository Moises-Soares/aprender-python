# Modulos sao arquivos que contem funcoes que podem ser usadas em outros programas
# Para usar um modulo, voce deve importa-lo
# Neste caso pygame é um modulo que contem funcoes para criar jogos
import pygame

# O modulo sys contem funcoes para interagir com o sistema
import sys

# O modulo random contem funcoes para gerar numeros aleatorios
import random

# Inicializa o pygame
# Repara que .init() é uma funcao do modulo pygame
# Para chamar uma funcao de um modulo, escrevemos o nome do modulo, seguido de um ponto e o nome da funcao
pygame.init()

# Variaveis sao usadas para guardar valores
# Neste caso estamos a criar variaveis para guardar as cores
# As cores sao tuplas, que sao variaveis que guardam varios valores
# As cores sao guardadas no formato RGB (Red, Green, Blue)
# Cada cor tem um valor entre 0 e 255
# O vermelho é (255, 0, 0)
# O verde é (0, 255, 0)
# O azul é (0, 0, 255)
# O branco é (255, 255, 255)
# O preto é (0, 0, 0)
# Uma cor é sempre uma mistura de vermelho, verde e azul
# Por exemplo, o amarelo é (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# Variaveis para guardar a largura e altura do ecran
# A largura 800 representa 800 pixeis
# A altura 600 representa 600 pixeis
LARGURA = 800
ALTURA = 600

# Cria um ecran com a largura e altura especificadas
janela = pygame.display.set_mode((LARGURA, ALTURA))

# Define o titulo da janela
# repara que estamos a usar uma funcao do modulo pygame
# para chamar uma funcao de um modulo, escrevemos o nome do modulo, seguido de um ponto e o nome da funcao
# Neste caso display é um modulo do pygame e set_caption é uma funcao desse modulo
pygame.display.set_caption("Titulo do jogo")

# Ciclo principal
# O ciclo principal serve para manter o jogo a rodar
# O jogo so termina quando o jogador fecha a janela

# Variavel para guardar se o jogo esta a correr
aCorrer = True

# While é um ciclo
# O ciclo while repete o codigo que esta dentro dele enquanto a condicao for verdadeira
# Neste caso, o ciclo while repete o codigo que esta dentro dele enquanto aCorrer for verdadeiro
while aCorrer:
    # for tambem é um ciclo, para já nao precisas de saber como funciona
    # Este ciclo serve para verificar se o jogador fechou a janela
    # Para já ignoramos este ciclo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            aCorrer = False

    # Vamos então começar a usar a janela que criamos e guardamos na variavel janela
            
    # Para prencer a janela com uma cor, usamos a funcao fill
    # ja sabes que para chamar uma função escrevemos o nome do modulo, seguido de um ponto e o nome da funcao,
    # a seguir intre parenteses colocamos os argumentos da funcao
    # os argumentos sao os valores que a funcao precisa para funcionar
    # neste caso a funcao fill precisa de um argumento que é a cor
    janela.fill(WHITE)

    # Agora vamos então desenhar varias figuras na janela
    # Para desenhar uma figura, usamos a funcao draw
    # e depois colocamos o tipo de figura que queremos desenhar
    # neste caso vamos desenhar um retangulo
    pygame.draw.rect(janela, RED, (50, 50, 100, 100))  

    # Desenhar um circulo
    # Os argumentos sao: a janela, a cor, a posicao do centro do circulo e o raio
    # pygame.draw.circle(janela, GREEN, (200, 150), 50) 

    # Desenhar uma linha 
    # Os argumentos sao: a janela, a cor, a posicao do inicio da linha e a posicao do fim da linha
    # pygame.draw.line(janela, BLUE, (300, 50), (500, 50), 5)

    # Desenhar uma elipse
    # Os argumentos sao: a janela, a cor, a posicao do centro da elipse, a largura e a altura
    # pygame.draw.ellipse(janela, BLACK, (100, 300, 150, 100))

    # Desengar um poligono
    # Os argumentos sao: a janela, a cor e uma lista com as posicoes dos vertices do poligono
    # Uma lista é um tipo de dados que guarda varios valores
    # Em python uma lista é definida com parenteses retos: []
    # Exemplo de listas com numeros: [1, 2, 3, 4, 5]
    # Exemplo de lista com strings: ["ola", "mundo"]
    # Exemplo de lista com numeros e strings: [1, 2, "ola", "mundo"]
    # Neste caso a lista tem 3 tuplas
    # pygame.draw.polygon(janela, RED, [(400, 300), (350, 400), (450, 400)])

    # Esta funcao serve para atualizar o ecran com as alteracoes que fizemos
    # Sempre que fizeres alteracoes no ecran, tens que chamar esta funcao
    pygame.display.flip()


# Quando sair do ciclo principal, o jogo termina
pygame.quit()
sys.exit()


# Já aprendeste muito hoje:
# 1. Como criar um jogo
# 2. Como criar um ecran
# 3. Como desenhar figuras no ecran
# 4. Como atualizar o ecran
# 5. O que são variavei
# 6. O que são tuplas
# 7. O que são listas
# 8. O que são funcoes
# 9. O que são modulos
# 10. O que são ciclos

# Camos agora fazer um exercicio para testar o que aprendeste
# - Cria variaveis com mais cores
# - Consulta a internet para saberes qual o RGB de uma cor https://www.w3schools.com/colors/colors_picker.asp
# - Desenha mais figuras no ecran
# - Desenha um circulo
# - Desenha uma linha
# - Desenha uma elipse
# - Desenha um poligono
# - Desenha uma imagem á tia escolha com estas figuras
# - Desenha a bandeira da França
# - Desenha a bandeira da Alemanha
# - Desenha a bandeira de Portuga
# - Desenha a bandeira da Suiça


# Muito bem, aprendeste muita coisa hoje,
# mas isto aindas é só o começo
# Como será que se faz para desenhar uma imagem mais complexa?
# É isso que vamos aprender na proxima aula

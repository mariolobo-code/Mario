import pygame
import os

# iniciar o pygame
pygame.init()

# caminho da pasta de imagem
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PASTA_IMAGEM = os.path.join(os.path.dirname(BASE_DIR), "imagem")

# Funçao para carregar imagem
def carregar_imagem(nome, largura, altura):
    caminho = os.path.join(PASTA_IMAGEM,nome)
    imagem = pygame.imagem.load(caminho).convert_alPha()
    imagem = pygame.imagetransform.scale(imagem,(largura,altura))
    return Imagem

# criar a janela
LARGURA = 720
ALTURA = 720
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Game 03 - Personagem.png",85,85)

# Carregar personagem
personagem = carregar_imagem("personagem.png", 85,85)

# Posição inicial do personagem
x = 80
y = 600 # mais embaixo

#lOOP PRINCIPAL
rolando = True
while rolando:
    for evento in pygame.event.get():
      if evento.type == pygame.QUIT:
        rolando = False 

     # cor de fundo
     tela.fill((135, 206, 235))
    
    #Atualizar tela
    pygame.display.flip()

    # Atualizar tela
    pygame.displey.flip()

    # Encerrar
    pygame.quit()


    


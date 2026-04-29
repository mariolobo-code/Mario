import pygame
import os

# iniciar o pygame
pygame.init()

# caminho da pasta de imagens
BASE_DIR - os.path.dirname(os.patchabspath(__file__))
PASTA_IMAGEM = os.path.join(os.path.dirname(BASE_DIR)," imagem")

# Função para carregar imagem
def carregar_imagem(nome, largura, altura):
caminho = os.path.join(PASTA_IMAGEM)
imagem = pygame.image.load(caminho).convert_alfha()
imagem = pygame.tranform.scale(imagem, (largura, altura))
import pygame

# inicializando o Pygame
pygame.init()

# Definindo o tamanho da janela
LARGURA, ALTURA = 720, 720
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Nome da Janela")

#Loop principal do jogo
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Atualizar a tela
    pygame.display.flip()

# Finalizar o Pygame
pygame.quit()

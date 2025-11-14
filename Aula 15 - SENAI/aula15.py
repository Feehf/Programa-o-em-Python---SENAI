import pygame


pygame.init()


tela  = pygame.display.set_mode((300,200))
pygame.display.set_caption('titulo')
run = True


while run:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            run  = False


    tela.fill('purple')
    pygame.draw.rect(tela,'blue',(135,87,30,30))
    pygame.draw.circle(tela,'red', (100,150), 20)
    pygame.draw.ellipse(tela, 'green', (150,210,30,30))

    pygame.display.flip()


pygame.quit()
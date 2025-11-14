import pygame 

pygame.init()
tela  = pygame.display.set_mode((500,500))
pygame.display.set_caption('PONG')

BRANCO = (255,255,255)
PRETO = (0,0,0)

raquete1_x, raquete1_y = 50,225
raquete2_x, raquete2_y = 450,225
bola_x, bola_y = 250,250

velocidade_raquete = 0.6
velocidade_bola_x, velocidade_bola_y = 0.02, 0.05

raquete_largura, raquete_altura = 20,100
bola_largura, bola_altura = 20,20

placar_1 = 0
placar_2 = 0

font = pygame.font.SysFont(None, 50)

def desenhar():
    tela.fill(BRANCO) 
    pygame.draw.rect(tela, PRETO,(raquete1_x, raquete1_y,raquete_largura, raquete_altura))
    pygame.draw.rect(tela, PRETO,(raquete2_x, raquete2_y,raquete_largura, raquete_altura))
    pygame.draw.ellipse(tela, PRETO,(bola_x, bola_y,bola_largura, bola_altura ))

    placar_texto =  font.render(f'{placar_1}   x   {placar_2} ', True, PRETO)
    tela.blit(placar_texto,(190,20))


run = True

while run:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            run  = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and raquete1_y > 0:
        raquete1_y -= velocidade_raquete
    if keys[pygame.K_s] and raquete1_y < 500 - raquete_altura:
        raquete1_y += velocidade_raquete    
              
    if keys[pygame.K_UP] and raquete2_y > 0:
        raquete2_y -= velocidade_raquete
    if keys[pygame.K_DOWN] and raquete2_y < 500 - raquete_altura:
        raquete2_y += velocidade_raquete   

    bola_x += velocidade_bola_x    
    bola_y += velocidade_bola_y  

    if bola_y<=0 or bola_y >= 500 - bola_altura:
        velocidade_bola_y = -velocidade_bola_y

    if (raquete1_x < bola_x < raquete1_x + raquete_largura) and (raquete1_y < bola_y < raquete1_y + raquete_altura) :
        velocidade_bola_x= -velocidade_bola_x     

    if (raquete2_x < bola_x < raquete2_x + raquete_largura) and (raquete2_y < bola_y < raquete2_y + raquete_altura) :
        velocidade_bola_x= -velocidade_bola_x 
    
    if bola_x <= 0:
       placar_2 += 1
       bola_x, bola_y = 250,250
    if bola_x >= 500:
       placar_1 += 1
       bola_x, bola_y = 250,250

    desenhar()

    pygame.display.update()
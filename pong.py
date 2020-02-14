import pygame
import serial
import asyncio
import concurrent
from lib import *
from ball import Ball

(scherm_breedte, scherm_hoogte) = (700, 500)
scherm = start_spel()

positie_paddle_1 = (20, 200)
positie_paddle_2 = (670, 200)
positie_ball = (345, 195)
paddle_1 = voeg_paddle_toe(WHITE, 10, 100, positie_paddle_1)
paddle_2 = voeg_paddle_toe(WHITE, 10, 100, positie_paddle_2)
ball = voeg_bal_toe(WHITE, 10, positie_ball)

lijst_van_entities = entity_list()
voeg_entity_toe(lijst_van_entities, paddle_1)
voeg_entity_toe(lijst_van_entities, paddle_2)
voeg_entity_toe(lijst_van_entities, ball)

loop = True
clock = pygame.time.Clock()

scoreA = scoreB = 0

while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
              loop = False
        elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x:
                     loop=False

    keys = pygame.key.get_pressed()
    lees_knop(pygame.K_LEFT,    "naar_boven", paddle_1)
    lees_knop(pygame.K_RIGHT,   "naar_onder", paddle_1)
    lees_knop(pygame.K_UP,      "naar_boven", paddle_2)
    lees_knop(pygame.K_DOWN,    "naar_onder", paddle_2)
    lijst_van_entities.update()

    if paddle1_touch(ball, paddle_1) or paddle2_touch(ball, paddle_2):
    	ball.bounce()
    if ball.rect.x>=690:
        scoreA+=1
        ball.snelheid[0] = -ball.snelheid[0]
    if ball.rect.x<=0:
        scoreB+=1
        ball.snelheid[0] = -ball.snelheid[0]
    if ball.rect.y>490:
        ball.snelheid[1] = -ball.snelheid[1]
    if ball.rect.y<0:
        ball.snelheid[1] = -ball.snelheid[1]

    scherm.fill(BLACK)
    pygame.draw.line(scherm, WHITE, [349, 0], [349, 500], 5)
    
    lijst_van_entities.draw(scherm)

    scoreText(scoreA, scherm, (250, 10))
    scoreText(scoreB, scherm, (420, 10))

    pygame.display.flip()
     
    clock.tick(60)
pygame.quit()
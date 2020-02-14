import pygame
from random import randint
BLACK = (0, 0, 0)
WHITE = (255,255,255)
RED   = (255, 0, 0)
GREEN   = (0, 255, 0)
BLUE   = (0, 0, 255)

rechtermuur = 690
linkermuur  = 0
vloer       = 490
plafond     = 0

class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        self.rect = self.image.get_rect()
    
    def moveUp(self, pixels):
        self.rect.y -= pixels
        if self.rect.y < 0:
            self.rect.y = 0

    def moveDown(self, pixels):
        self.rect.y += pixels
        if self.rect.y > 400:
            self.rect.y = 400

class Ball(pygame.sprite.Sprite):
    def __init__(self, color, width):
        super().__init__()
        
        self.image = pygame.Surface([width, width])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        pygame.draw.rect(self.image, color, [0, 0, width, width])
        
        self.snelheid = [randint(4,8),randint(-8,8)]
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.x += self.snelheid[0]
        self.rect.y += self.snelheid[1]
    def bounce(self):
        self.snelheid[0] = -self.snelheid[0]
        self.snelheid[1] = randint(-8,8)

def start_spel():
    pygame.init()
    size = (700, 500)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Pong")

    return screen

def voeg_paddle_toe(kleur=WHITE, breedte=20, lengte=200, start_positie=(20, 200)):
    paddle = Paddle(kleur, breedte, lengte)
    (paddle.rect.x, paddle.rect.y) = start_positie
    return paddle

def voeg_bal_toe(kleur=WHITE, breedte=10, pos=(345, 195)):
    ball = Ball(kleur, breedte)
    (ball.rect.x, ball.rect.y) = pos
    return ball

def entity_list():
    return pygame.sprite.Group()

def voeg_entity_toe(lijst, entity):
    lijst.add(entity)

def lees_knop(key, wat, van):
    keys = pygame.key.get_pressed()
    if keys[key]:
        if (wat == "naar_boven"):
            van.moveUp(5)
        elif (wat == "naar_onder"):
            van.moveDown(5)
        
def raakt(wat, waar):
    if (waar == "rechtermuur" or waar == "linkermuur"):
        if (wat.rect.x >= rechtermuur or wat.rect.x <= 0):
            ball.snelheid[0] = -ball.snelheid[0]
    if (waar == "vloer" or "plafond"):
        if (wat.rect.y > vloer or wat.rect.y < 0):
            ball.snelheid[0] = -ball.snelheid[0]
def paddle1_touch(b, p) -> bool:
    return pygame.sprite.collide_mask(b, p)
def paddle2_touch(b, p) -> bool:
    return pygame.sprite.collide_mask(b, p)
def scoreText(score, S, pos) -> None:
    font = pygame.font.Font(None, 74)
    text = font.render(str(score), 1, WHITE)
    S.blit(text, pos)

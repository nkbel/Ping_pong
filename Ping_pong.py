from pygame import *
from random import randint
window = display.set_mode((700, 500))
display.set_caption("Пинг понг")
window.fill((30, 144, 255))

font.init()
font1 = font.SysFont("Arial", 36)
font2 = font.SysFont("Arial", 36)
win = font2.render("YOU WIN", True, (255, 255, 255))
lose = font2.render("YOU LOSE", True, (180, 0, 0))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 700 - 80:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 700 - 80:
            self.rect.y += self.speed




wall1 = Player("racket.png", 100, 350, 50, 100, 10)
wall2 = Player("racket.png", 600, 350, 50, 100, 10)
ball = GameSprite("ball.png", 300, 250, 80, 100, 10)
speed_x = 3
speed_y = 3
clock = time.Clock()
FPS = 60
game = True
Finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if Finish != True:
        window.fill((30, 144, 255))
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(wall1, ball) or sprite.collide_rect(wall2, ball):
            speed_x *= -1
        if ball.rect.y > 500-80 or ball.rect.y < 0:
            speed_y *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose, (200, 200))
        if ball.rect.x < 700:
            finish = True
            window.blit(lose, (200, 200))
        
        
        
        
        wall1.update_l()
        wall1.reset()
        wall2.update_r()
        wall2.reset()
        ball.reset()

        
      










    clock.tick(FPS)
    display.update()


    

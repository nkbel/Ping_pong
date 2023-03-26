from pygame import *
from random import randint
window = display.set_mode((700, 500))
display.set_caption("Пинг понг")
window.fill((30, 144, 255))

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
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_DOWN] and self.rect.x < 700 - 80:
            self.rect.x += self.speed




wall1 = Player("rocket1.png", 100, 350, 50, 100, 10)
wall2 = Player("rocket1.png", 100, 350, 50, 100, 10)
ball = GameSprite("ball.png", 300, 250, 80, 100, 10)

clock = time.Clock()
FPS = 60
game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        wall1.update()
        wall1.reset()
        wall2.update()
        wall2.reset()
        ball.update()
        ball.reset()

        
      










    clock.tick(FPS)
    display.update()
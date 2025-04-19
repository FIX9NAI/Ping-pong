from pygame import *

import random

from random import randint

class GameSprite(sprite.Sprite):

    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (80, 80))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
class Player(GameSprite):

    def __init__(self, image_path, x, y, speed):
        super().__init__(image_path, x, y, speed)
        self.speed = speed
        self.last_shot = 0  # время последнего выстрела

    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 1190 - self.rect.width:
            self.rect.x += self.speed
        if keys[K_SPACE]:
            player.fire()

back = (0, 100, 0)
win_widht = 1600
win_height = 900
window = display.set_mode((win_widht, win_height))
window.fill(back)

clock = time.Clock()
FPS = 90
game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(FPS)
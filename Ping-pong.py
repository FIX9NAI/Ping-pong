from pygame import *

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

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 890 - self.rect.height:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_RIGHT] and self.rect.y < 890 - self.rect.height:
            self.rect.y += self.speed

back = (0, 100, 0)
win_width = 1600
win_height = 900
window = display.set_mode((win_width, win_height))
window.fill(back)

clock = time.Clock()
FPS = 90
game = True

player = Player('rocket.png', 10, 450, 10)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    player.reset()

    player.update_l()
    display.update()
    clock.tick(FPS)

display.update()

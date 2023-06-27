from pygame import *
from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height)) #вместе 55,55 - параметры
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y


    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

font.init()
font_1 = font.Font(None, 70)


back = (200, 255, 255)
win_width = 700
win_height = 500

window = display.set_mode((win_width, win_height))

window.fill(back)

player_1 = Player("racket.png", 10, 175, 5, 50, 150)
player_2 = Player("racket.png", 640, 175, 5, 50, 150)

ball = GameSprite("tenis_ball.png", 325, 225, 5, 50, 50)


#флаги, отвечающие за состояние игры
game = True
finish = False
clock = time.Clock()
FPS = 60

speed_x = 5
speed_y = 5

while game:

    if finish != True:
        window.fill(back)
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y <= 5 or ball.rect.y >= 445:
            if speed_y >= 0:
                speed_y = randint(-9, -3)
            else:
                speed_y = randint(3, 9)
            if ball.rect.y <= 5:
                ball.rect.y = 5
            else:
                ball.rect.y = 445
        if sprite.collide_rect(ball, player_1) or sprite.collide_rect(ball, player_2):
            if speed_x >= 0:
                speed_x = randint(-9, -3)
            else:
                speed_x = randint(3, 9)
        if ball.rect.x <= 5:
            win_text_1 = font_1.render('Победил 2 игрок', True, (0, 0 , 0))
            window.blit(win_text_1, (100, 100))
            finish = True
        if ball.rect.x >= 645:
            win_text_2 = font_1.render('Победил 1 игрок', True, (0, 0, 0))
            window.blit(win_text_2, (200, 200))
            finish = True


        player_1.update_l()
        player_1.reset()
        player_2.update_r()
        player_2.reset()
        ball.reset()
        
    display.update()

    

    for e in event.get():
        if e.type == QUIT:
            game = False

    clock.tick(FPS)
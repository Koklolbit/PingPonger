from pygame import *

mixer.init()

win_width = 1000
win_height = 500

#Universal Sprite
class GameSprite(sprite.Sprite):

   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):

       sprite.Sprite.__init__(self)

       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))


class Blue(GameSprite):
    def update(self):
        global win_height
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 105:
           self.rect.y += self.speed

class Red(GameSprite):
    def update(self):
        global win_height
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 105:
           self.rect.y += self.speed

back = "back.png"
blue = 'blue.png'
red = 'red.png'
ball = 'ball.png'


player1 = Blue(blue, 10, win_height / 2 - 50, 25, 100, 7)
player2 = Red(red, win_width - 10 - 50, win_height / 2 - 50, 25, 100, 7)


display.set_caption("PingPong")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(back), (win_width, win_height))
run = True
clock = time.Clock()


#Work
while run:
    window.blit(background, (0,0))
    player1.update()
    player2.update()
    player1.reset()
    player2.reset()
    for e in event.get():
        if e.type == QUIT:
            run = False 
    display.update()
    clock.tick(60)

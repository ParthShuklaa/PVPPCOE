import pygame
import random
from pygame.locals import *
from os import path

pygame.init()

img_dir = path.join(path.dirname(__file__), "Explosions")

pygame.init()

display_width = 1260
display_height = 560

pygame.mixer.init()

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Batmobil Game")

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
block_colour = (145, 190, 200)
font_name = pygame.font.match_font("arial")


def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, green)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def draw_shield_bar(surf, x, y, pct):    # pct means percentage
        BAR_LENGTH = 20
        BAR_HEIGHT = 1
        fill = (pct/10) * BAR_LENGTH
        outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
        fill_rect = pygame.Rect(x, y, fill, BAR_LENGTH)
        pygame.draw.rect(surf, green, fill_rect)
        pygame.draw.rect(surf, black, outline_rect)
        

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(carImg, (220, 111))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.left = 100
        self.rect.y = random.randrange(125,400)
        self.speedy = 0
        self.shield = 100

    def update(self):
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP]:
            self.speedy = 10
        if keystate[pygame.K_DOWN]:
            self.speedy = -10
        self.rect.y -= self.speedy
        if self.rect.top > 430:
            self.rect.top = 430
        if self.rect.top < 105:
            self.rect.top = 105
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYUP and event.key == K_RETURN:
                    player.shoot()
                    
    def shoot(self):
        bullet = Bullet(self.rect.centerx + 60, self.rect.bottom - 45)
        all_sprites.add(bullet)
        bullets.add(bullet)
        shoot_sound.play()


class Car(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(car1, (200, 79))
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.right = 0
        self.rect.y = random.randrange(125, 400)
        self.speedx = random.randrange(10, 50)

    def update(self):
        self.rect.x -= self.speedx
        keystate = pygame.key.get_pressed()

        if self.rect.right < 0-500:
            self.rect.left = 1260
            self.rect.y = random.randrange(125, 400)
            self.speedx = random.randrange(20, 50)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(box, (100, 100))
        self.image.set_colorkey(black)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.right = 0
        self.rect.y = random.randrange(125, 400)
        self.speedx = 20

    def update(self):
        self.rect.x -= self.speedx
        keystate = pygame.key.get_pressed()

        if self.rect.right < 0-500:
            self.rect.left = 1260
            self.rect.y = random.randrange(125, 400)
            self.speedx = 20

            
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(coin, (90, 90))
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        self.rect.right = 0
        self.rect.y = random.randrange(125, 400)
        self.speedx = random.randrange(10, 12)

    def update(self):
        self.rect.x -= self.speedx
        keystate = pygame.key.get_pressed()

        if self.rect.right < 0-500:
            self.rect.left = 1260
            self.rect.y = random.randrange(125, 400)
            self.speedx = random.randrange(10, 12)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(bullet, (40, 40))
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedx = 20

    def update(self):
        self.rect.x += self.speedx
        if self.rect.right < 0:
            self.kill()


class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = explosion_anim["lg"][0]    # Part of Animation of Explosion
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 100

    def update(self):
            now = pygame.time.get_ticks()
            if now - self.last_update > self.frame_rate:
                self.last_update = now
                self.frame += 1
                if self.frame == len(explosion_anim["lg"]):
                    self.kill()
                else:
                    center = self.rect.center
                    self.image = explosion_anim["lg"][self.frame]
                    self.rect = self.image.get_rect()
                    self.rect.center = center


def show_go_screen():
    gameDisplay.blit(bat, (0, 0))    # Shows the Main Start Screen
    pygame.display.flip()            # Updates the Display of Screen
    waiting = True
    while waiting:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP and event.key == K_RETURN:
                 waiting =False


clock = pygame.time.Clock()
crashed = False
game_over = True
carImg = pygame.image.load("batmobil.png")
bg = pygame.image.load("street2.png")
car1 = pygame.image.load("car_2.png").convert()
car2 = pygame.image.load("batmobil.png").convert()
bullet = pygame.image.load("bullet.png").convert()
coin = pygame.image.load("batcoin.png").convert()
box = pygame.image.load("box.png").convert()
bat = pygame.image.load("batman.png").convert()

explosion_anim = {}    # Dictionary used for Animation of Explosion
explosion_anim["lg"]=[]
for i in range (9):
    filename = "regularExplosion0{}.png".format(i)
    img = pygame.image.load(path.join(img_dir, filename))
    img.set_colorkey(black)
    img_lg = pygame.transform.scale(img, (80, 80))
    explosion_anim["lg"].append(img_lg)
    

z = 0
x = (display_width * 0.100)
y = (display_height * 0.35)
x_change = 0
y_change = 0
car_speed = 0
z_change = -30

# Sound Files
shoot_sound = pygame.mixer.Sound("Shoot.wav")
crash_sound = pygame.mixer.Sound("Explosion.wav")
o_sound = pygame.mixer.music.load("Awaken.wav")
c_sound = pygame.mixer.Sound("coin.wav")
_sound = pygame.mixer.Sound("Shoot.wav")

# Game Loop
pygame.mixer.music.play()
while not crashed:
    if game_over:
        show_go_screen()
        game_over = False
        all_sprites = pygame.sprite.Group()
        player = Player()
        all_sprites.add(player)
        cars = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        enemies = pygame.sprite.Group()
        coins = pygame.sprite.Group()
        for i in range(3):
            d = Coin()
            all_sprites.add(d)
            coins.add(d)

        for i in range(1):
            c = Car()
            all_sprites.add(c)
            cars.add(c)
            score = 0
            
        for i in range(1):
            e = Enemy()
            all_sprites.add(e)
            enemies.add(e)
            score = 0
            
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.KEYUP and event.key == K_SPACE:
                player.shoot()

                
    z += z_change
    y += y_change
    x += x_change

    # Updates the Sprites means (Characters)
    all_sprites.update()

    # If Bullet Hits Enemy
    hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
    for hit in hits:
        crash_sound.play()
        expl = Explosion(hit.rect.center, "lg")
        all_sprites.add(expl)
        score += 5
        e = Enemy()
        all_sprites.add(e)
        enemies.add(e)

    # If Player Hits Coin
    hits = pygame.sprite.spritecollide(player, coins, True, pygame.sprite.collide_mask)
    if hits:
        c_sound.play()
        score += 10
        d = Coin()
        all_sprites.add(d)
        coins.add(d)
        
    # If Player Hits Enemies
    hits = pygame.sprite.spritecollide(player, enemies, True, pygame.sprite.collide_mask)
    for hit in hits:
        crash_sound.play()
        expl = Explosion(hit.rect.center, "lg")
        all_sprites.add(expl)
        score += 3
        e = Enemy()
        player.shield -= 10
        all_sprites.add(e)
        enemies.add(e)
        
    # If Player Hits the Obstacle Car
    hits = pygame.sprite.spritecollide(player, cars, False, pygame.sprite.collide_mask)
    for hit in hits:
        crash_sound.play()
        player.shield -= 2
        if player.shield < 0:
            game_over = True

    # If Bullet Hits the Obstacle Car
    hits = pygame.sprite.groupcollide(cars, bullets, False, False)
    for hit in hits:
        crash_sound.play()
        player.shield -= 3
        if player.shield < 0:
            game_over = True

    # Conditions for Score and Speed
    if score > 20:
        z_change = -30
        
    if score > 30:
        z_change = -40

    if score > 40:
        z_change = -50
        
    if score > 50:
        z_change = -60
        
    if score > 60:
        z_change = -70

    if score > 70:
        z_change = -80

    if score > 80:
        z_change = -90

    if score > 90:
        z_change = -100
        
    if game_over == True:
        z_change = -30


    rel_z = z % bg.get_rect().width
    gameDisplay.blit(bg, (rel_z - bg.get_rect().width, 0))
    if rel_z < display_width:
       gameDisplay.blit(bg, [rel_z, 0])

    # Draw
    all_sprites.draw(gameDisplay)
    draw_text(gameDisplay, str(score), 18, display_width / 2, 10)
    draw_text(gameDisplay, "SCORE = ", 18, display_width - 680, 10)
    draw_shield_bar(gameDisplay, 5, 5, player.shield)

    pygame.display.update()   # Updates the Display Every Time
    clock.tick(60)

pygame.quit()
exit()
quit()

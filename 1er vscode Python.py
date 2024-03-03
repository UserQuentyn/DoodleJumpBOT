# imports
import pygame
import sys
import random
# Windows
clock = pygame.time.Clock()
pygame.init()
Run = True
pygame.display.set_caption(("DoodleJump Bot"))
screen = pygame.display.set_mode((680,960))
# Background

background = pygame.image.load("Background.jpeg")
background = pygame.transform.scale(background,(680,960))

# Class PLayer
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.velocity = 13
        self.image = pygame.image.load("doodle Jump PLayer.png")
        self.rect = self.image.get_rect()
        self.rect.x = 340
        self.rect.y = 100
        self.image = pygame.transform.scale(self.image,(110,110))
        self.origine_image = self.image
        self.angle = 1
        self.jumping = False
        self.y_gravity = 1
        self.jump_height = 27
        self.y_velocity = self.jump_height
        self.on = self.rect.y + 15
# class platform
class Plateform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x_scale = 200
        self.y_scale = 30
        self.x1 = random.randint(200, 480)
        self.y1 = random.randint(30, 930)
        self.x2 = random.randint(200, 480)
        self.y2 = random.randint(30, 930)
        self.x3 = random.randint(30, 930)
        self.y3 = random.randint(30, 930)
        self.x4 = random.randint(200, 480)
        self.y4 = random.randint(30, 930)
        self.scroll_velocity = 5
        self.image1 = pygame.Rect((self.x1, self.y1, self.x_scale, self.y_scale))
        self.image2 = pygame.Rect((self.x2, self.y2, self.x_scale, self.y_scale))
        self.image3 = pygame.Rect((self.x3, self.y3, self.x_scale, self.y_scale))
        self.image4 = pygame.Rect((self.x4, self.y4, self.x_scale, self.y_scale))
        





plateform = Plateform()
player = Player()
while Run :
    # Background Sprite
    screen.blit(background, (0,0))
    pygame.display.flip()
    # Player Sprite
    screen.blit(player.image, player.rect)

    plat1 = pygame.draw.rect(screen,pygame.Color("#16fe29"), plateform.image1, 0, 233)
    plat2 = pygame.draw.rect(screen,pygame.Color("#16fe29"), plateform.image2, 0, 233)
    plat3 = pygame.draw.rect(screen,pygame.Color("#16fe29"), plateform.image3, 0, 233)
    plat4 = pygame.draw.rect(screen,pygame.Color("#16fe29"), plateform.image4, 0, 233)
    
    # Move (Control)
    player.rect.y += 3
    presse = pygame.key.get_pressed()
    if presse[pygame.K_a] or presse[pygame.K_LEFT]:
        player.angle = 1
        player.image = pygame.transform.flip(player.origine_image, player.angle, 0)
        player.rect.x -= player.velocity
    if presse[pygame.K_d] or presse[pygame.K_RIGHT]:
        player.angle = 0
        player.image = pygame.transform.flip(player.origine_image, player.angle, 0)
        player.rect.x += player.velocity
    def jump():
        player.jumping = True
        if player.jumping:
            player.rect.y -= player.y_velocity
            player.y_velocity -= player.y_gravity
            if player.y_velocity < -player.jump_height:
                player.jumping = False
                player.y_velocity = player.jump_height

    if player.rect.x < 10 :
        player.rect.x = 600
    if player.rect.x > 600 :
        player.rect.x = 10
    if player.rect.y < 100:
        plateform.y1 -= plateform.scroll_velocity
        plateform.y2 -= plateform.scroll_velocity
        plateform.y3 -= plateform.scroll_velocity
        plateform.y4 -= plateform.scroll_velocity
       


    # colision
    if plat1.colliderect(player):
        if player.rect.y > plateform.y1:
            player.rect.y -= player.on
        jump()
    if plat2.colliderect(player):
        if player.rect.y > plateform.y2:
            player.rect.y -= player.on
        jump
    if plat3.colliderect(player):
        if player.rect.y > plateform.y3:
            player.rect.y -= player.on
        jump()
    if plat4.colliderect(player):
        if player.rect.y > plateform.y4:
            player.rect.y -= player.on
        jump()
    # Refreish screen
    pygame.display.flip()
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    clock.tick(60)
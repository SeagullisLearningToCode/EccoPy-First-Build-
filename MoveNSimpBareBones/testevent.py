# Test Key-pressed
try:
    import pygame
    import pygame.gfxdraw as gd
    import pygame.freetype as ft
    from random import *
    from math import *
    import time
    import sys
    import os
    from dataTST.dataSCR.Dol_Anim.Dol_move_pgi import *
except ImportError as err:
    print("couldn't load module. %s" % (err))
    sys.exit(2)

imgdir = os.path.dirname(os.path.abspath(__file__))
fntdir = os.path.dirname(os.path.abspath(__file__))
snddir = os.path.dirname(os.path.abspath(__file__))

shz = 8000

sound = pygame.mixer.init(shz)
sfx01 = pygame.mixer.Sound(os.path.join(snddir, "dataSND/SFX/", "CSOBB_BE.wav"))
print(sfx01)

sfx02 = pygame.mixer.Sound(os.path.join(snddir, "dataSND/SFX/", "CSOBB_KI.wav"))
print(sfx02)

sfx03 = pygame.mixer.Sound(os.path.join(snddir, "dataSND/SFX/", "SON1.wav"))
print(sfx03)

sfx04 = pygame.mixer.Sound(os.path.join(snddir, "dataSND/SFX/", "GYORSIT.wav"))
print(sfx04)

snd01 = pygame.mixer.Sound(os.path.join(snddir, "dataSND/EDOLPHIN1/", "Ecco_the_Dolphin_19.wav"))
print(snd01)

pygame.init()

size = rx, ry = 1885, 1080  # Resolution
screen = pygame.display.set_mode((size))
surface = pygame.Surface(size).convert()

dol00 = pygame.image.load(os.path.join(imgdir, "dataIMG/ECCO/DOLPHIN1/", "0-0.png")) # IDLE
print(dol00)

bkgrd = pygame.image.load(os.path.join(imgdir, "dataIMG/ECCO/BL/LQ/", "Artic_cropped.bmp"))
bkgrd = pygame.transform.scale(bkgrd, (1920, 384))
print(bkgrd)

w_surface = pygame.image.load(os.path.join(imgdir, "dataIMG/ECCO/BL/LQ/", "ar_wa_upscaled.bmp"))
w_surface = pygame.transform.scale(w_surface, (1920, 100))
print(w_surface)

underwater = pygame.image.load(os.path.join(imgdir, "dataIMG/ECCO/BL/LQ/", "OceanUpscaled.bmp"))
#underwater = pygame.transform.scale(underwater, (1920, 20))
print(underwater)

clock = pygame.time.Clock()
t = 60

# Keyboard
keyb = pygame.KEYUP
# Keyboard/Bindings
ic_fr = pygame.K_KP_PLUS
dc_fr = pygame.K_KP_MINUS
up = pygame.K_UP
down = pygame.K_DOWN
left = pygame.K_LEFT
right = pygame.K_RIGHT
sonar = pygame.K_z
dash = pygame.K_x

class player(pygame.sprite.Sprite):
    global dol00
    def __init__(self): # Initializer
        super().__init__()
        # C-Frame
        self.current_frame = 0
        # Image
        self.image = dol00
        self.image = pygame.transform.scale2x(self.image)
        self.surf = pygame.Surface((50, 50))
        self.rect = self.surf.get_rect(center = (randint(40, 360), randint(40, 360)))

    def update(self): # Controls
        prke = pygame.key.get_pressed()
        if prke[left]:
            self.current_frame += 1
            self.sprites = a_left_dict
            self.image = self.sprites[self.current_frame]
            self.image = pygame.transform.scale2x(self.image)
            if self.current_frame >= 5:
                self.current_frame = 0
            self.rect.move_ip(-5, 0)


        if prke[right]:
            self.current_frame += 1
            self.sprites = a_right_dict
            self.image = self.sprites[self.current_frame]
            self.image = pygame.transform.scale2x(self.image)
            if self.current_frame >= 5:
                self.current_frame = 0
            self.rect.move_ip(5, 0)

        if prke[up]:
            self.current_frame += 1
            self.sprites = a_up_dict
            self.image = self.sprites[self.current_frame]
            self.image = pygame.transform.scale2x(self.image)
            if self.current_frame >= 5:
                self.current_frame = 0
            self.rect.move_ip(0, -5)

        if prke[down]:
            self.current_frame += 1
            self.sprites = a_down_dict
            self.image = self.sprites[self.current_frame]
            self.image = pygame.transform.scale2x(self.image)
            if self.current_frame >= 5:
                self.current_frame = 0
            self.rect.move_ip(0, 5)

        if prke[left] and prke[down]:
            self.current_frame += 1
            self.sprites = a_leftd_dict
            self.image = self.sprites[self.current_frame]
            self.image = pygame.transform.scale2x(self.image)
            if self.current_frame >= 5:
                self.current_frame = 0

        if prke[right] and prke[down]:
            self.current_frame += 1
            self.sprites = a_leftd_dict
            self.image = self.sprites[self.current_frame]
            self.image = pygame.transform.scale2x(self.image)
            self.image = pygame.transform.flip(self.image, 90, 0)
            if self.current_frame >= 5:
                self.current_frame = 0

        if prke[left] and prke[up]:
            self.current_frame += 1
            self.sprites = a_leftu_dict
            self.image = self.sprites[self.current_frame]
            self.image = pygame.transform.scale2x(self.image)
            if self.current_frame >= 5:
                self.current_frame = 0

        if prke[right] and prke[up]:
            self.current_frame += 1
            self.sprites = a_rightu_dict
            self.image = self.sprites[self.current_frame]
            self.image = pygame.transform.scale2x(self.image)
            if self.current_frame >= 5:
                self.current_frame = 0

        if prke[sonar]:
            sfx03.play()

    def d(self, surface): # Render Sprite
        screen.blit(self.image, self.rect)

ecco = player()

anim = 0.0
xblocks = range(0, 1920, 20)
yblocks = range(0, 1080, 20)

# Window
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == keyb:
            if event.key == ic_fr:
                if not t >= 60:
                    t += 5
                    print(t)
                else:
                    print(f"Can't go higher than {t} FPS \n Decrease it")
            elif event.key == dc_fr:
                if not t <= 1:
                    t -= 5
                    print(t)
                else:
                    print(f"Can't go any lower than {t} FPS \n Increase it")

    clock.tick(t)
    screen.blit(bkgrd, (0, 0))
    #screen.blit(w_surface, (0, 384))

    anim = anim + 0.02
    for x in xblocks:
        xpos = (x + (sin(anim + x * 0.01) * 15)) + 20
        for y in yblocks:
            ypos = (x + (sin(anim + x * 0.01) * 15)) + 20
        screen.blit(underwater, (0, 414), (xpos, ypos, 1920, 1080))

    ecco.update()
    ecco.d(screen)

    for x in xblocks:
        xpos = (x + (sin(anim + x * 0.01) * 5)) + 5
        for y in yblocks:
            ypos = (x + (sin(anim + x * 0.01) * 5)) + 5
        screen.blit(w_surface, (0, 384), (xpos, ypos, 1920, 100))

#    snd01.play(1)

#        if event.type == keyb:
#            if event.key == up:
#                sfx02.play(0)
#                print(f"SPLASH_OUT_OF_WATER: {sfx02}")
#                py -= 20
#            elif event.key == down:
#                sfx01.play(0)
#                print("SPLASH_INTO_WATER")
#                py += 20
#            elif event.key == right:
#                px += 10
#            elif event.key == left:
#                px -= 10
#            elif event.key == sonar:
#                sfx03.play(0)
#                print(sfx03)
#            elif event.key == dash:
#                sfx04.play(0)
#                print(sfx04)
#
#    screen.blit(dol00, (px, py))


    # Display
    pygame.display.set_caption(f"{clock.get_fps()} Dolphin: {ecco}")
    pygame.display.flip()

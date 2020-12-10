try:
    import sys
    import time
    from math import *
    from random import *
    import pygame
    import pygame.freetype as ft
    import os
except ImportError as err:
    print("couldn't load module. %s" % (err))
    sys.exit(2)

# Colors
# AgR Color Presets
fennec_fox_white = 230, 224, 207
red_panda_arp = 247, 148, 29 # Bright Orange
red_panda_brownage = 125, 86, 48
thomps_gazelle_orange = 190, 134, 62
blue = 0, 0, 255
white = 255, 255, 255
red = 255, 0, 0
red1 = 128, 0, 0
green = 0, 255, 0

fntdir = os.path.dirname(os.path.abspath(__file__))

pygame.freetype.init(cache_size=1024)
# Fonts
dos = ft.Font(os.path.join(fntdir, "dataFNT/MessFont/DOS", "DOS_VGA_437.ttf"))
print(dos)

ari = ft.Font(os.path.join(fntdir, "dataFNT/MessFont/Arial8", "Arial_11pt_st.ttf"))
print(ari)

avc = ft.Font(os.path.join(fntdir, "dataFNT/MessFont/AV_Cwm_t", "AV_Cwm_t.ttf"))
print(avc)

get_fonts = ft.get_fonts()
print(get_fonts)
print(ft.match_font('comicsansms'))

pygame.init()

size = rx, ry = 1920, 1080  # Resolution
screen = pygame.display.set_mode(size)
surface = pygame.Surface(size)

# Strings, mann Aggresive
teststr = '''
I've done it again fronting like I'm a good girl
Collecting the points like a goody two-shoes
My head is filled with dissatisfaction
Everything about this world is full of b.s
All of you all of you all of you all of you!
Everyday everyday everyday everyday!
'''
teststr_01 = "I've done it again fronting like I'm a good girl"
teststr_02 = "Collecting the points like a goody two-shoes"
teststr_03 = "My head is filled with dissatisfaction"
teststr_04 = "Everything about this world is full of b.s"
teststr_05 = "All of you all of you all of you all of you!"
teststr_06 = "Everyday everyday everyday everyday!"

code_cre = "Scott Colten /--_ (2020)"
dev_not = "SIS loves this too much :)"

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    rs01 = dos.render_to(
        screen,
        (rx/3.5, ry/4),
        teststr_01,
        fgcolor=red_panda_arp,
        style=ft.STYLE_DEFAULT,
        size=32
    )

    rs02 = dos.render_to(
        screen,
        (rx/3.3, ry/3.5),
        teststr_02,
        fgcolor=red_panda_arp,
        style=ft.STYLE_DEFAULT,
        size=32
    )

    rs03 = dos.render_to(
        screen,
        (rx/3.1, ry/3.2),
        teststr_03,
        fgcolor=red_panda_arp,
        style=ft.STYLE_DEFAULT,
        size=32
    )

    rs04 = dos.render_to(
        screen,
        (rx/3.3, ry/2.9),
        teststr_04,
        fgcolor=red_panda_arp,
        style=ft.STYLE_DEFAULT,
        size=32
    )

    rs05 = avc.render_to(
        screen,
        (rx/3.9, ry/2.7),
        teststr_05,
        fgcolor=red1,
        style=ft.STYLE_DEFAULT,
        size=128
    )

    rs06 = avc.render_to(
        screen,
        (rx/3.9, ry/2.3),
        teststr_06,
        fgcolor=red1,
        style=ft.STYLE_DEFAULT,
        size=128
    )

    rs07 = ari.render_to(
        screen,
        (rx/320, ry/1.05),
        code_cre,
        fgcolor=fennec_fox_white,
        style=ft.STYLE_DEFAULT,
        size=24
    )

    rs08 = ari.render_to(
        screen,
        (rx/320, ry/1.1),
        dev_not,
        fgcolor=fennec_fox_white,
        style=ft.STYLE_DEFAULT,
        size=32
    )
    pygame.display.set_caption('Aggressive Program')
    pygame.display.flip()
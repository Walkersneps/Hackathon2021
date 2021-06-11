import numpy as np
import sys
import pygame as pg
import cwiid
import colors
import configurazioni
import wii
import coordinate


off_set = 100
radius_big = 50
radius_small = 5
stroke = 5

screen_upper_left = [off_set, off_set]
screen_upper_right = [configurazioni.screen_res_x-off_set, off_set]
screen_lower_right = [configurazioni.screen_res_x-off_set, configurazioni.screen_res_y-off_set]
screen_lower_left = [off_set, configurazioni.screen_res_y-off_set]
screen_coords = [screen_upper_left, screen_upper_right, screen_lower_left, screen_lower_right]

def waitAngolo(screen, wiimote: cwiid.Wiimote, angolo) -> (int, int):
    while 1:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    print("spazio premuto!")
                    sorgenti = wii.poll(wiimote)
                    if sorgenti.count(None) != len(sorgenti):
                        return wii.get_best_coords(sorgenti)
                    else:
                        print("Riprova")

        screen.fill(colors.BLACK)
        
        if angolo == 1:
            pg.draw.circle(screen, colors.CYAN, screen_upper_left, radius_big, stroke)
            pg.draw.circle(screen, colors.CYAN, screen_upper_left, radius_small, stroke)
        elif angolo == 2:
            pg.draw.circle(screen,colors.CYAN, screen_upper_right, radius_big, stroke)
            pg.draw.circle(screen,colors.CYAN, screen_upper_right, radius_small, stroke)
        elif angolo == 3:
            pg.draw.circle(screen,colors.CYAN, screen_lower_right, radius_big, stroke)
            pg.draw.circle(screen,colors.CYAN, screen_lower_right, radius_small, stroke)
        elif angolo == 4:
            pg.draw.circle(screen,colors.CYAN, screen_lower_left, radius_big, stroke)
            pg.draw.circle(screen,colors.CYAN, screen_lower_left, radius_small, stroke)

        pg.display.flip()
        




def esegui_calibrazione(screen, wiimote: cwiid.Wiimote) -> np.ndarray:
    """Mostra la schermata di calibrazione e fa eseguire la procedura.
    Ritorna gli otto parametri di conversione
    """

    # Angolo 1
    #screen.fill(colors.BLACK)
   # pg.draw.circle(screen, colors.CYAN, screen_upper_left, radius_big, stroke)
   # pg.draw.circle(screen, colors.CYAN, screen_upper_left, radius_small, stroke)
   # display.flip()
    wii_upper_left = waitAngolo(screen, wiimote, 1)

    # Angolo 2
    """
    screen.fill(colors.BLACK)
    pg.draw.circle(screen,colors.CYAN, screen_upper_right, radius_big, stroke)
    pg.draw.circle(screen,colors.CYAN, screen_upper_right, radius_small, stroke)
    display.flip()
    """
    wii_upper_right = waitAngolo(screen, wiimote, 2)

    # Angolo 3
    """
    screen.fill(colors.BLACK)
    pg.draw.circle(screen,colors.CYAN, screen_lower_right, radius_big, stroke)
    pg.draw.circle(screen,colors.CYAN, screen_lower_right, radius_small, stroke)
    display.flip()
    """
    wii_lower_right = waitAngolo(screen, wiimote, 3)

    # Angolo 4
    """
    screen.fill(colors.BLACK)
    pg.draw.circle(screen,colors.CYAN, screen_lower_left, radius_big, stroke)
    pg.draw.circle(screen,colors.CYAN, screen_lower_left, radius_small, stroke)
    display.flip()
    """
    wii_lower_left = waitAngolo(screen, wiimote, 4)

    wii_coords = [wii_upper_left, wii_upper_right, wii_lower_left, wii_lower_right]

    return coordinate.calibrazione(wii_coords, screen_coords)
    





    
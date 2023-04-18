import pygame as pg
import sys

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800,600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("./ex01/fig/pg_bg.jpg") #p44に書いてある.
    bg_img2 = pg.image.load("./ex01/fig/pg_bg.jpg")
    bg_img3 = pg.transform.flip(bg_img2, True,False)
    

    

    kk_img = pg.image.load("./ex01/fig/3.png")
    kk_img1 = pg.transform.flip(kk_img, True,False)
    kk_img2 = pg.transform.rotozoom(kk_img1, 1, 1.0)
    kk_img3 = pg.transform.rotozoom(kk_img1, 2, 1.0)
    kk_img4 = pg.transform.rotozoom(kk_img1, 3, 1.0)
    kk_img5 = pg.transform.rotozoom(kk_img1, 4, 1.0)
    kk_img6 = pg.transform.rotozoom(kk_img1, 5, 1.0)
    kk_img7 = pg.transform.rotozoom(kk_img1, 6, 1.0)
    kk_img8 = pg.transform.rotozoom(kk_img1, 7, 1.0)
    kk_img9 = pg.transform.rotozoom(kk_img1, 8, 1.0)
    kk_img10 = pg.transform.rotozoom(kk_img1, 9, 1.0)
    kk_img11 = pg.transform.rotozoom(kk_img1, 10, 1.0)
    matome = [kk_img2,kk_img3,kk_img4,kk_img5,kk_img6,kk_img7,kk_img8,kk_img9,kk_img10,kk_img11,kk_img11,kk_img10,kk_img9,kk_img8,kk_img7,kk_img6,kk_img5,kk_img4,kk_img3,kk_img2]
    #time = [1,2,3,4,5,6,7,8,9,10]
    # for i in range(20):
    #     y = time + 1
    #     z = pg.transform.rotozoom(kk_img1, y, 1.0)
    #     if y==10:
    #         y = time - 1
    #         if y == 1:
    #             continue

    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        tmr += 1
        x = tmr%3200
        
        # screen.blit(bg_img, [-x, 0]) 
        # screen.blit(bg_img,[1600-x,0])
        screen.blit(bg_img3,[1600-x,0])
        screen.blit(bg_img3,[-x,0])
        screen.blit(matome[tmr%20], [300,200])
        

        pg.display.update()
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
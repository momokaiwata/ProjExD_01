import pygame as pg
import sys

def main():
    pg.display.set_caption("はじめてのPygame")  #画面の左上に名前が書いてある
    screen = pg.display.set_mode((800, 600)) #画面の大きさ
    clock  = pg.time.Clock()   #初期化
    fonto  = pg.font.Font(None, 80)  #フォントサイズ
    tmr = 0

    while True:
        for event in pg.event.get():  #ユーザが操作するもの（クリックとか全般）
            if event.type == pg.QUIT: return  #×ボタン(pg.QUIT)をクリックしたらmain関数から出る
        
        tmr += 1  #カウントアップ
        txt = fonto.render(str(tmr), True, (255, 255, 255))  #(表示する文字,True,色)を示している
        screen.fill((0, 0, 0))  #バックグランド黒
        screen.blit(txt, [300, 200]) #txtというものを(300,200)のところのスクリーンに張り付ける
        pg.display.update()  
        clock.tick(1)  #フレームレイト(1秒あたりどれくらいの間隔)を1と示している.大きくなるほど滑らかになる.


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
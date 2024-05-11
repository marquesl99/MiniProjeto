import pyautogui as pg
import time 

pg.PAUSE = 0.4

pg.press('win')
pg.write('spotify')
pg.press('enter')


time.sleep(5)   

pg.click(x=47, y=315)
pg.click(x=485, y=460)
time.sleep(1)


pg.click(x=1370, y=107)
pg.press('win')
pg.write('chrome')
pg.press('enter')
pg.click(x=876, y=600)

pg.write('facebook.com.br')
pg.press('enter')
pg.hotkey('ctrl', 't')
pg.write('gmail.com.br')
pg.press('enter')
pg.hotkey('ctrl', 't')
pg.write('linkedin.com.br')
pg.press('enter')
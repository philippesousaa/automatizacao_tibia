import constants
import pyautogui as pg


battle_image = 'images/region_battle.png'
target_image = 'images/reg_target.png'
monster_image = 'images/monster_dead.png'
hole_image = 'images/holy_down.png'
anchor2_image = 'images/anchor_floor_2.png'
anchor3_image = 'images/anchor_floor_3.png'

def hole_down(should_down):
    if should_down:
        try:
            box = pg.locateOnScreen(hole_image, confidence=0.8)
            if box:
                x, y = pg.center(box)
                pg.moveTo(x, y)
                pg.click()
                pg.sleep(5)
        except Exception as e:
            print('error hole down')

def hole_up(img_anchor, plus_x, plus_y, should_up):
    if should_up:
        try:
            box = pg.locateOnScreen(img_anchor, confidence=0.8)
            if box:
                x, y = pg.center(box)
                pg.moveTo(x + plus_x, y + plus_y)
                pg.press('F4')
                pg.click()
        except Exception as e:
            print('error hole up')


def check_battle():
    try:
        print(pg.locateOnScreen(battle_image, region=constants.REGION_BATTLE)) 
        return pg.locateOnScreen(battle_image, region=constants.REGION_BATTLE)
    except Exception as e:
        print(f'Bicho na battle')
        return None

import constants
import pyautogui as pg
import keyboard as k


battle_image = "images/region_battle.png"
target_image = "images/reg_target.png"
monster_image = "images/monster_dead.png"
hole_image = "images/holy_down.png"
anchor2_image = "images/anchor_floor_2.png"
anchor3_image = "images/anchor_floor_3.png"


def hole_down(should_down):
    if should_down:
        try:
            print(f'Entando no hole_down...')
            box = pg.locateOnScreen(hole_image, confidence=0.8)
            x, y = pg.center(box)
            pg.moveTo(x, y )
            pg.click(button='left')
            print(f'Saindo do hole_down...')
            return box
        except Exception as e:
            print(f'Saindo do hole_down sem buraco...')
            return None

def hole_up(should_up, img_anchor, plus_x, plus_y):
    if should_up:
        try:       
            print(f'Entrado no hole_up... ')
            box = pg.locateOnScreen(img_anchor, confidence=0.8)
            x, y = pg.center(box)
            pg.moveTo(x + plus_x, y + plus_y)
            pg.press("F4")
            pg.click(button='left')
            print(f'Saindo do hole_up com buraco....')
            return box
        except Exception as e:
            print(f'Saindo do hole_up sem buraco...')
            return None

def check_battle():
    try:
        return pg.locateOnScreen(battle_image, region=constants.REGION_BATTLE)
    except Exception as e:
        print(f"Bicho na battle")
        pg.sleep(1)
        return None

def check_status(name, delay, x, y, rgb, button_name):
    print(f"checando {name} ....")
    pg.sleep(delay)
    if pg.pixelMatchesColor(x, y, rgb):
        pg.press(button_name)

def eat_food():
    pg.press('F6')
    print('comendo comida')
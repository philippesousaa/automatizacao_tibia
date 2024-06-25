from asyncio import sleep
import os
import pyautogui as pg
import keyboard as k
import actions
import constants
import json


battle_image = 'images/region_battle.png'
target_image = 'images/reg_target.png'
monster_image = 'images/monster_dead.png'
hole_image = 'images/holy_down.png'
anchor2_image = 'images/anchor_floor_2.png'
anchor3_image = 'images/anchor_floor_3.png'


def is_attacking():
    try:
        print('atacando')
        return pg.locateOnScreen(target_image, region=constants.REGION_BATTLE, confidence=0.7  )
    except Exception as e:
        print(f'Erro ao localizar a imagem is_attacking: {e}')
        return None

def kill_monster():
    print("actions.check_battle começando kill monster")
    while actions.check_battle() == None:
        print("entrou no while")
        pg.press('space')
        while is_attacking() != None:
            print('esperando o bicho morrerr')
        print('procurando bicho')


def get_loot():
    try:
        loot = pg.locateAllOnScreen(monster_image, confidence=0.9, region=constants.REGION_LOOT)
        for box in loot:
            x, y = pg.center(box)
            pg.moveTo(x, y)
            pg.click()
            pg.sleep(0.5)
            
        print('loot', loot)
    except Exception as e:
        print('sem bicho')

def go_to_flag(path, wait):
    print(f'indo para : {path}')
    flag = pg.locateOnScreen(path, confidence=0.8, region=constants.REGION_MAP)
    if flag:
        x, y = pg.center(flag)
        pg.moveTo(x, y)
        pg.click()
        pg.sleep(wait)
        print(f'esperando path : {path}')

def check_player_position():
    try:
       return pg.locateOnScreen('images\point_player.png', confidence=0.8, region=constants.REGION_MAP)
    except Exception as e:
        return None
    

def run():
    with open(f'{constants.FOLDER_NAME}/infos.json', 'r') as file:
        data = json.loads(file.read())
    for item in data:
        kill_monster()
        
        get_loot()
    
        go_to_flag(item['path'], item ['wait'])
        if check_player_position():
            kill_monster()
            pg.sleep(1)
            get_loot()
            pg.sleep(3)
            go_to_flag(item['path'], item ['wait'])
            actions.hole_down(item['down_hole'])
            actions.hole_up(item['up_hole'], f'{constants.FOLDER_NAME}/anchor_floor_2.png', 430, 0)
            actions.hole_up(item['up_hole'], f'{constants.FOLDER_NAME}/anchor_floor_2.png', 130, 130)

k.wait('h')
run()
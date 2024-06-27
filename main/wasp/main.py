from asyncio import sleep
import os
import pyautogui as pg
import keyboard as k
import actions
import constants
import json


battle_image = "images/region_battle.png"
target_image = "images/reg_target.png"
monster_image = "images/monster_dead.png"
hole_image = "images/holy_down.png"
anchor2_image = "images/anchor_floor_2.png"
anchor3_image = "images/anchor_floor_3.png"


def is_attacking():
    try:
        print("atacando")
        return pg.locateOnScreen(
            target_image, region=constants.REGION_BATTLE, confidence=0.7
        )
    except Exception as e:
        return None


def kill_monster():
    print("Entrando no kill_monster...")
    while actions.check_battle() is None:
        pg.press("space")
        while is_attacking() is not None:
            print("esperando o bicho morrer")
    print("Encerrando no kill_monster...")


def get_loot():
    try:
        print("Entrando no get_loot...")
        loot = pg.locateAllOnScreen(
            monster_image, confidence=0.9, region=constants.REGION_LOOT
        )
        for i in loot:
            x, y = pg.center(i)
            pg.moveTo(x, y)
            pg.click(button="left")
        print("Encerrando no get_loot com bicho morto ao lado...")
    except Exception as e:
        print("Encerrando no get_loot sem bichos proximos...")
        return None

def go_to_flag(path, wait):
    print(f'entrando GO_TO_FLAG com param: {path} e {wait}...')
    try:
        flag = pg.locateOnScreen(path, region=constants.REGION_MAP, confidence=0.8)
        x, y = pg.center(flag)
        pg.moveTo(x, y)
        pg.click(button="left")
        pg.sleep(wait)  
        print('Encerrando GO_TO_FLAG...')  
        return flag
    except Exception as e:
        return None


def check_player_position():
    try:
        print(f'Entrando no check_player_position')
        check =  pg.locateOnScreen(
            "images/point_player.png", confidence=0.8, region=constants.REGION_MAP
        )
        print(f'Encerrando no check_player_position achando imagem no minimapa...') 
        return check
    except Exception as e:
        print(f'Encerrando no check_player_position não achando imagem no minimapa...') 
        return None

def run():
    print(f'iniciando run()...') 
    with open(f"{constants.FOLDER_NAME}/infos.json", "r") as file:
        data = json.loads(file.read())
    print(f'json: {data}...') 
    for item in data:
        kill_monster()
        pg.sleep(1)
        get_loot()
        print(item["path"]+ ' SEM CHECK...')
        go_to_flag(item["path"], item["wait"])
        while check_player_position() != None:
            kill_monster()  
            pg.sleep(1)
            get_loot()       
            print(item["path"]+ ' COM CHECK...')
            go_to_flag(item["path"], item["wait"])
        actions.eat_food()
        actions.hole_down(item['down_hole'])
        actions.hole_up(item['up_hole'], f'{constants.anchor2_image}', 430, 0)
        actions.hole_up(item['up_hole'], f'{constants.anchor3_image}', 130, 130)


# Início da execução do script

k.wait("h")
while True: 
    run()
# check_status("mana", 1, 988, 31, (0, 63, 141), 'F3')
# check_status("vida", 1, 838, 32, (35, 35, 35), 'F3')

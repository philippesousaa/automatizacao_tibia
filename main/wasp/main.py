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
        return pg.locateOnScreen(target_image, region=constants.REGION_BATTLE, confidence=0.7)
    except Exception as e:
        print(f'Erro ao localizar a imagem is_attacking: {e}')
        return None

def kill_monster():
    print("actions.check_battle começando kill monster")
    while actions.check_battle() is None:
        print("entrou no while")
        pg.press('space')
        while is_attacking() is not None:
            print('esperando o bicho morrer')
        print('procurando bicho')

def get_loot():
    try:
        loot = list(pg.locateAllOnScreen(monster_image, confidence=0.9, region=constants.REGION_LOOT))
        if not loot:
            print('Sem loot encontrado.')
            return
        print(f'Encontrado {len(loot)} monstros')
        for box in loot:
            x, y = pg.center(box)
            pg.moveTo(x, y)
            pg.click()
            pg.sleep(0.5)
            print('Clique realizado no loot')
    except Exception as e:
        print(f'Erro ao procurar loot: {e}')

def go_to_flag(data):
    try:
        for item in data:
            path = item['path']
            wait = item['wait']
            
            print(f'Indo para: {path}')
            flag = pg.locateOnScreen(path, confidence=0.8, region=constants.REGION_MAP)
            if flag:
                x, y = pg.center(flag)
                pg.moveTo(x, y)
                pg.click()
                pg.sleep(wait)
                print(f'Esperando path: {path}')
                return True
            else:
                print(f'Não encontrou: {path}')
        
        print('Nenhum dos caminhos foi encontrado.')
        return False
    
    except Exception as e:
        print(f'Erro ao procurar a flag: {e}')
        return False

def check_player_position():
    try:
        return pg.locateOnScreen('images/point_player.png', confidence=0.8, region=constants.REGION_MAP)
    except Exception as e:
        print(f'Erro ao verificar a posição do jogador: {e}')
        return None

def run():
    try:
        with open(f'{constants.FOLDER_NAME}/infos.json', 'r') as file:
            data = json.load(file)
        
        for _ in range(2): # loop two times
            for item in data:
                kill_monster()
                get_loot()
                try:
                    go_to_flag(item['path'])
                
                except Exception as e:
                    Eliminate even had ה th havePs4 even Did<|end_of_action|><|start_of_action|> Drag  had

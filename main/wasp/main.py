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


import pyautogui as pg
import constants
import json

def is_attacking():
    try:
        return pg.locateOnScreen(target_image, region=constants.REGION_BATTLE, confidence=0.7)
    except Exception as e:
        print(f'Erro ao localizar a imagem is_attacking: {e}')
        return None

def kill_monster():
    while actions.check_battle() is None:
        pg.press('space')
        while is_attacking() is not None:
            pass  # Espera até não estar atacando

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
    except Exception as e:
        print(f'Erro ao procurar loot: {e}')

def go_to_flag(paths):
    try:
        for item in paths:
            path = item['path']
            wait = item['wait']
            
            print(f'Tentando ir para: {path}')
            while True:
                flag = pg.locateOnScreen(path, confidence=0.7, region=constants.REGION_MAP)
                if flag:
                    x, y = pg.center(flag)
                    pg.moveTo(x, y)
                    pg.click()
                    pg.sleep(wait)
                    print(f'Sucesso ao ir para: {path}')
                    while check_player_position() is None:
                        pass  # Espera até o jogador estar na posição correta
                    break  # Sai do loop interno pois chegou no path correto
                else:
                    print(f'Não encontrou: {path}')
        
        print('Concluídas todas as flags.')
        return True
    
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
        
        for item in data:
            kill_monster()
            get_loot()
            
            try:
                paths = [item]  # Passando o item como lista para go_to_flag
                if not go_to_flag(paths):
                    print(f'Não foi possível encontrar nenhum dos caminhos para o item: {item}')
            
            except Exception as e:
                print(f'Erro ao executar go_to_flag para o item: {item}. Erro: {e}')
                continue
    
    except Exception as e:
        print(f'Erro durante a execução do script: {e}')

# Início da execução do script
run()


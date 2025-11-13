#!/usr/bin/env python3

from constants import ROOMS
from player_actions import
from utils import

def main():
    print("Первая попытка запустить проект")
    

#Переменная, ослеживающая статус игрока

game_state = {
        'player_inventory': [], # Инвентарь игрока
        'current_room': 'entrance', # Текущая комната
        'game_over': False, # Значения окончания игры
        'steps_taken': 0 # Количество шагов
  }

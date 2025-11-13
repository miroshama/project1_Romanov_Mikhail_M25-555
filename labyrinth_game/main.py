#!/usr/bin/env python3

from .player_actions import show_inventory
from .utils import describe_current_room

# Функция для обработки пользовательских команд

def process_command(game_state: dict, command: str) -> None:
    
    splited_command = command.split()
    
    match splited_command[0].lower():
        case "quit":
            game_state['game_over'] = True
            print("Выход из игры.")

def main():
  game_state = {
        'player_inventory': [], # Инвентарь игрока
        'current_room': 'entrance', # Текущая комната
        'game_over': False, # Значения окончания игры
        'steps_taken': 0 # Количество шагов
  }
  
  print("\nДобро пожаловать в Лабиринт сокровищ!")
  describe_current_room(game_state=game_state)
  
  while not game_state['game_over']:
    user_cmd = input()
    process_command(game_state=game_state, command=user_cmd)

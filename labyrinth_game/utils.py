# labyrinth_game/utils.py
import math as ma

from .constants import (
  BEAST_DMG_PROBABILITY,
  COMMANDS,
  EVENT1_DEATH_DMG,
  EVENT2_DEATH_DMG,
  EVENT_COUNT,
  EVENT_INTENSIVITY,
  EVENT_PROBABILITY,
  NUMBERS,
  ROOMS,
  TRAP_DMG_PROBABILITY,
)


def describe_current_room(game_state: dict) -> None:
  '''
  Функция описания текущей комнаты
  
  game_state - текущее состояние игры
  '''
  current_player_room = game_state['current_room']
  current_room_info = ROOMS[current_player_room]
  
  print(f"\n== {current_player_room.upper()} ==")
  
  if len(current_room_info['items']) > 0:
    print(f"Заметные предметы: {', '.join(current_room_info['items'])}") # noqa: E501
  else:
    print("В комнате не видно никаких предметов.")
  
  
  print(f"Выходы: {', '.join([i + ' - ' + current_room_info['exits'][i] for i in current_room_info['exits']])}") # noqa: E501
  
  if current_room_info['puzzle'] is not None:
    print("Кажется, здесь есть загадка (используйте команду solve).")
  else:
    print("Загадок здесь нет.")


def solve_puzzle(game_state: dict) -> None:
  '''
  Функция решения загадки

  game_state - текущее состояние игры
  '''
  if ROOMS[game_state['current_room']]['puzzle'] is None:
    print("Загадок здесь нет.")
    
  else:
    print(f"{ROOMS[game_state['current_room']]['puzzle'][0]}")
    users_answer = input("Ваш ответ: ")
    
    if (users_answer.lower() == ROOMS[game_state['current_room']]['puzzle'][1].lower() or ROOMS[game_state['current_room']]['puzzle'][1] in NUMBERS and NUMBERS[ROOMS[game_state['current_room']]['puzzle'][1]] == users_answer.lower()): # noqa: E501
      print("Загадка решена верно!")
      ROOMS[game_state['current_room']]['puzzle'] = None
      
      if game_state['current_room'] == "hall":
        game_state['player_inventory'].append('torch')
        
      elif game_state['current_room'] == "trap_room":
        game_state['player_inventory'].append('coin')
      
      elif game_state['current_room'] == "library":
        game_state['player_inventory'].append('long_sword')
      
      print(f"Ваша награда: {game_state['player_inventory'][-1]}")
      
    else:
        
      if game_state['current_room'] == "trap_room":
        trigger_trap(game_state=game_state)
        
      else:
        print("Неверно. Попробуйте снова.")

def attempt_open_treasure(game_state: dict) -> None:
  '''
  Функция попытки открытия сундука с сокровищами

  game_state - текущее состояние игры
  '''
  if "treasure_key" in game_state['player_inventory']:
    print("Вы используете ключ, раздаётся щелчок, и крышка сундука поднимается!")
    ROOMS[game_state['current_room']]['items'].remove('treasure_chest')
    print(f"В сундуке сокровище! Вы победили за {game_state['steps_taken']} шагов!")
    game_state['game_over'] = True
    
  else:
    users_answer = input("Сундук заперт. ... Ввести код? (да/нет) ")
    
    if users_answer.lower() == "да":
      users_code = input("Введние код: ")
      
      if users_code == ROOMS[game_state['current_room']]['puzzle'][1]:
        print("Вы правильно вводите код, раздаётся щелчок, и крышка сундука поднимается!")
        print(f"В сундуке сокровище! Вы победили за {game_state['steps_taken']} шагов!")
        game_state['game_over'] = True
      
      else:
        print("Код был введён неправильно. Пожалуйста, повторите попытку.")
        
    else:
      print("Вы делаете шаг назад, отходя от сундука.")
    
def show_help(commands_list: dict = COMMANDS) -> None:
  '''
  Функция отображения помощи

  commands_list - список команд
  '''
  print("\nДоступные команды:")
  str_lens = [len(list(commands_list.keys())[i]) for i in range(0, len(commands_list))]
  max_str_len = max(str_lens)
  
  for command in commands_list:
    print(command + ': ' + ' ' * (max_str_len - len(command)) + commands_list[command])

def pseudo_random(seed: int, modulo: int) -> int:
  '''
  Функция генерации псевдо-случайных чисел

  seed - количество шагов,
  modulo - целое число для определения диапазона результата
  '''
  rng_number = ma.sin(seed) * 12.9898 * 43758.5453
  rng_number_final = round((rng_number - ma.floor(rng_number)) * modulo)
  
  return rng_number_final

def trigger_trap(game_state: dict) -> None:
  '''Функция имитации срабатывания ловушки в комнате '''
  print("\nЛовушка активирована! Пол стал дрожать...")
  
  if len(game_state['player_inventory']) > 0:
    rng_item_index = pseudo_random(seed=game_state['steps_taken'], modulo=len(game_state['player_inventory'])-1)
    deleted_item = game_state['player_inventory'].pop(rng_item_index)
    print(f"Вы смогли выбраться, но в процессе потеряли {deleted_item}.")
    
  else:
    rng_damage = pseudo_random(seed=game_state['steps_taken'], modulo=TRAP_DMG_PROBABILITY)
    
    if rng_damage < EVENT1_DEATH_DMG:
    
      if "old_armor" in game_state['player_inventory']:
        print("Вам повезло, что на вас были старые доспехи. Вы избежали смертельного урона.")
        print("Ваши доспехи сломались.")
        game_state['player_inventory'].remove('old_armor')
        
      else: 
        print("Вы не успеваете увернуться, и на вас падает каменная плита. Игра окончена!")
        game_state['game_over'] = True
      
    else:
      print("Вы успеваете увернуться от падающей плиты.")

def random_event(game_state: dict) -> None:
  '''
  Функция генерации случайных событий
  '''
  rng_event_trigger = pseudo_random(seed=game_state['steps_taken'], modulo=EVENT_PROBABILITY) # noqa: E501
  
  if rng_event_trigger < EVENT_INTENSIVITY:
    rng_event_number = pseudo_random(seed=game_state['steps_taken'], modulo=EVENT_COUNT) # noqa: E501
    
    print("\nСобытие:")
    
    if rng_event_number == 0:
      print("Вы замечаете что-то блестящее на полу, это золотая монета (coin).")
      print("Вы подбираете монету.")
      game_state['player_inventory'].append('coin')
      
    elif rng_event_number == 1:
    
      print("Вы слышите шорох в темном углу комнаты. Ваш пульс заметно учащается.")
      if "sword" in game_state['player_inventory']:
        print("Вы обнажаете свой меч. Существо с гортанным рыком пятится назад и скрывается темноте.") # noqa: E501
        
      else:
        rng_damage_beast = pseudo_random(seed=game_state['steps_taken'], modulo=BEAST_DMG_PROBABILITY) # noqa: E501
        if rng_damage_beast < EVENT2_DEATH_DMG:
    
          if "old_armor" in game_state['player_inventory']:
            print("Вам повезло, что на вас были старые доспехи. Существо когтями проходится по вашей броне и скрывается в темноте.") # noqa: E501
            print("Ваши доспехи пришли в негодность.")
            game_state['player_inventory'].remove('old_armor')
        
          else: 
            print("Существо прыгает на вас и наносит смертельную рану.")
            print("Вы истекаете кровью на полу комнаты. Игра окончена")
            game_state['game_over'] = True
            
        else:
          print("Существо прыгает в вашу сторону, но вам везет, и оно промахивается.")
          print("После чего скрывается во тьме.")
        
    elif rng_event_number == 2:
    
      if game_state['current_room'] == "trap_room" and ("torch" not in game_state['player_inventory']): # noqa: E501
        trigger_trap(game_state=game_state)


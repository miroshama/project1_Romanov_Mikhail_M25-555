# player_actions.py

from .constants import ROOMS
from .utils import attempt_open_treasure, describe_current_room, random_event


def show_inventory(game_state):
    '''Функция отображения инвентаря'''
    inventory = game_state.get("player_inventory", [])

    if not inventory:
        print("\nВаш инвентарь пуст.")
    else:
        print("\nВаш инвентарь:")
        for i, item in enumerate(inventory, 1):
            print(f"  {i}. {item}")

def get_input(prompt="> "):
    '''Функция ввода пользователя'''

    try:
        user_input = input(prompt)
        return user_input.strip()
    except (KeyboardInterrupt, EOFError):
        print("\nВыход из игры.")
        return "quit"
    
def move_player(game_state: dict, direction: str) -> None:
  '''
  Функция движения игрока

  game_state - текущее состояние игры,
  direction - направление
  '''
  if direction in ROOMS[game_state['current_room']]['exits']:
    
    if ROOMS[game_state['current_room']]['exits'][direction] == "treasure_room":
      if "rusty_key" in game_state['player_inventory']:
      
        print("Вы применяете обнаруженный ключ, чтобы получить доступ к сокровищнице.")
        game_state['current_room'] = ROOMS[game_state['current_room']]['exits'][direction] # noqa: E501
        game_state['steps_taken'] += 1
        describe_current_room(game_state=game_state)
        
      else:
        print("Проход закрыт. Для продолжения пути необходим ключ.")
        
    else:
      game_state['current_room'] = ROOMS[game_state['current_room']]['exits'][direction] # noqa: E501
      game_state['steps_taken'] += 1
      describe_current_room(game_state=game_state)
    
    random_event(game_state=game_state)
    
  else:
    print("Двигаться в эту сторону невозможно.")

def take_item(game_state: dict, item_name: str) -> None:
  '''
  Функция поднятия предмета игроком

  game_state - текущее состояние игры,
  item_name - название предмета
  '''
  if item_name in ROOMS[game_state['current_room']]['items']:
  
    if item_name == "treasure_chest":
      print("Взять сундук не получится — он чересчур массивный.")
    
    else:
      game_state['player_inventory'].append(item_name)
      ROOMS[game_state['current_room']]['items'].remove(item_name)
      print(f"Вы подняли: {item_name}")
    
  else:
    print("В этой локации указанный предмет отсутствует.")

def use_item(game_state: dict, item_name: str) -> None:
  '''
  Функция использования предмета

  game_state - текущее состояние игры,
  item_name - название предмета
  '''
  if item_name in game_state['player_inventory']:
  
    if item_name == "torch":
      print("Комната наполнилась более ярким светом.")
      
    elif item_name == "sword":
      print("Вас охватывает невероятное ощущение уверенности.")
      
    elif item_name == "bronze_box":
      print("Подняв крышку шкатулки, вы обнаруживаете загадочный ключ.")
      game_state['player_inventory'].remove('bronze_box')
      
      if "treasure_key" not in game_state['player_inventory']:
        game_state['player_inventory'].append('treasure_key')
    
    elif item_name == "old_armor":
      print("В вашем распоряжении старые доспехи," 
      " которые могут выручить в опасной ситуации.")
    
    elif item_name == "treasure_key":
      if game_state['current_room'] == 'treasure_room':
        attempt_open_treasure(game_state=game_state)
        
      else:
        print(f"Нельзя использовать {item_name} в этой комнате.")
    
    elif item_name == "old_note":
      print("Вы читаете старую записку:")
      print("В этом замке царит тревожная атмосфера... Будь осторожен с ловушками.")
    
    else:
      print("Вы не представляете, как этим распорядиться.")
  
  else:
    print("Указанная вещь отсутствует в вашем инвентаре.")

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
  Функция перемещения игрока

  game_state - текущее состояние игры,
  direction - направление
  '''
  if direction in ROOMS[game_state['current_room']]['exits']:
    
    if ROOMS[game_state['current_room']]['exits'][direction] == "treasure_room":
      if "rusty_key" in game_state['player_inventory']:
      
        print("Вы применяете обнаруженный ключ, чтобы получить доступ к сокровищнице.")
        game_state['current_room'] = ROOMS[game_state['current_room']]['exits'][direction]
        game_state['steps_taken'] += 1
        describe_current_room(game_state=game_state)
        
      else:
        print("Проход закрыт. Для продолжения пути необходим ключ.")
        
    else:
      game_state['current_room'] = ROOMS[game_state['current_room']]['exits'][direction]
      game_state['steps_taken'] += 1
      describe_current_room(game_state=game_state)
    
    random_event(game_state=game_state)
    
  else:
    print("Двигаться в эту сторону невозможно.")
# player_actions.py

from .constants import ROOMS

def show_inventory(game_state):
    # Отображает содержимое инвентаря игрока

    inventory = game_state.get("player_inventory", [])

    if not inventory:
        print("\nВаш инвентарь пуст.")
    else:
        print("\nВаш инвентарь:")
        for i, item in enumerate(inventory, 1):
            print(f"  {i}. {item}")

def get_input(prompt="> "):
    # Запрос ввода пользователя

    try:
        user_input = input(prompt)
        return user_input.strip()
    except (KeyboardInterrupt, EOFError):
        print("\nВыход из игры.")
        return "quit"
    
'''def move_player(game_state: dict, direction: str):
    if direction in ROOMS[game_state['current_room']]['exits']:'''
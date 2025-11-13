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

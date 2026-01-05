# labyrinth_game/utils.py
import math as ma
from .constants import ROOMS

def describe_current_room(game_state):
    '''Функция вывода полного описания текущей комнаты'''

    current_room_name = game_state["current_room"]
    room = ROOMS.get(current_room_name)

    if not room:
        print(f"Ошибка: комната '{current_room_name}' не найдена!")
        return

    print(f"\n== {current_room_name.upper()} ==")

    print(f"{room['description']}")

    if room["items"]:
        print("\nЗаметные предметы:")
        for item in room["items"]:
            print(f"  - {item}")
    else:
        print("\nЗаметные предметы: нет")

    if room["exits"]:
        print("\nВыходы:")
        for direction, target_room in room["exits"].items():
            print(f"  {direction} -> {target_room}")
    else:
        print("\nВыходы: нет")

    if room["puzzle"] is not None:
        print("\nКажется, здесь есть загадка (используйте команду solve).")

# Функция генерации "случайных" чисел
def pseudo_random(seed: int, modulo: int) -> int:
  '''
  seed - количество шагов,
  modulo - целое число для определения диапазона результата
  '''
  rng_number = ma.sin(seed) * 12.9898 * 43758.5453
  rng_number_final = round((rng_number - ma.floor(rng_number)) * modulo)
  
  return rng_number_final

def show_help():
    print("\nДоступные команды:")
    print("  go <direction>  - перейти в направлении (north/south/east/west)")
    print("  look            - осмотреть текущую комнату")
    print("  take <item>     - поднять предмет")
    print("  use <item>      - использовать предмет из инвентаря")
    print("  inventory       - показать инвентарь")
    print("  solve           - попытаться решить загадку в комнате")
    print("  quit            - выйти из игры")
    print("  help            - показать это сообщение")

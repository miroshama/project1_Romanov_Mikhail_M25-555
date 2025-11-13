# labyrinth_game/utils.py
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

from .constants import ROOMS

def get_input(prompt="> "):
    # Запрос ввода пользователя

    try:
        user_input = input(prompt)
        return user_input.strip()
    except (KeyboardInterrupt, EOFError):
        print("\nВыход из игры.")
        return "quit"
    
def describe_current_room(game_state):
    # Выводит полное описание текущей комнаты

    current_room_name = game_state["current_room"]
    room = ROOMS.get(current_room_name)

    if not room:
        print(f"Ошибка: комната '{current_room_name}' не найдена!")
        return

    # Название комнаты в верхнем регистре

    print(f"\n== {current_room_name.upper()} ==")

    # Описание комнаты

    print(f"{room['description']}")

    # Список видимых предметов

    if room["items"]:
        print("\nЗаметные предметы:")
        for item in room["items"]:
            print(f"  - {item}")
    else:
        print("\nЗаметные предметы: нет")

    # Доступные выходы
    if room["exits"]:
        print("\nВыходы:")
        for direction, target_room in room["exits"].items():
            print(f"  {direction} -> {target_room}")
    else:
        print("\nВыходы: нет")

    # Сообщение о наличии загадки

    if room["puzzle"] is not None:
        print("\nКажется, здесь есть загадка (используйте команду solve).")

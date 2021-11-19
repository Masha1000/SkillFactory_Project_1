print("Перед Вами игра Крестики-нолики! Вам необходимо вводить координаты x и y через пробел.")
def play_field(): # рисуем игровое поле
    print('x/y 0  1  2')
    for i in range(3):
        n = '  '.join(field[i])
        print(f" {i}  {n}")

def coordinates(): # Запрашиваем координаты ходов у игроков
    while True:
        prop = input('Введите координаты: ').split()
        if len(prop) != 2:
            print('Введите координаты x и y через пробел')
            continue

        x, y = prop
        x, y = int(x), int(y)

        if 0 > x > 2 or 0 > y > 2: # Проверяем координаты
            print('Координаты находятся вне диапазона')
            continue
        if field[x][y] != "-":
            print('Клетка занята')
            continue
        return x, y

def victory(): # Сверяем с выигрышными комбинациями
    win = (((0,0), (0,1), (0,2)), ((1,0), (1,1), (1,2)), ((2,0), (2,1), (2,2)),
           ((0,2), (1,1), (2,0)), ((0,0), (1,1), (2,2)), ((0,0), (1,0), (2,0)),
           ((0,1), (1,1), (2,1)), ((0,2), (1,2), (2,2)))
    for prop in win:
        symbols = []
        for j in prop:
            symbols.append(field[j[0]][j[1]])
        if symbols == ['X', 'X', 'X']:
            print('Победили крестики!')
            return True
        if symbols == ['0', '0', '0']:
            print('Победили нолики!')
            return True
    return False
field = [["-"] * 3 for i in range(3)] # Начало игры
numbers = 0
while True:
    numbers += 1
    play_field()
    if numbers % 2 == 1:
        print('Сейчас ходят крестики')
    else:
        print('Сейчас ходят нолики')

    x, y = coordinates()
    if numbers % 2 == 1:
        field[x][y] = 'X'
    else:
        field[x][y] = '0'

    if victory():
        play_field()
        break

    if numbers == 9:
        print('Игра закончилась с ничейным результатом!')
        break
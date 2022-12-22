print('''
    Игра "Крестики - нолики". Игроки ходят по очереди. 
    Ходом считается двузначное число без пробелов: 
    первая цифра - номер строки
    вторая цифра - номер ряда
    Победит тот, кто первым заполнит своим символом строку, столбец или диагональ
    Крестик делает ход первым. Успехов!
    ''')

game_field = ([' ', "0", "1", "2"],
              ['0', "-", "-", "-"],
              ['1', "-", "-", "-"],
              ['2', "-", "-", "-"],)

players = ['x', 'o']
moves_variants = ['00', '01', '02', '10', '11', '12', '20', '21', '22']
moves = 0
Flag = True
while Flag:
    for _ in game_field:
        print(*_)
    if moves == 9:
        print('Ничья!')
        break
    if moves > 0:
        if (
                game_field[1][1] == game_field[1][2] == game_field[1][3] == players[1] or
                game_field[2][1] == game_field[2][2] == game_field[2][3] == players[1] or
                game_field[3][1] == game_field[3][2] == game_field[3][3] == players[1] or
                game_field[1][1] == game_field[2][1] == game_field[3][1] == players[1] or
                game_field[1][2] == game_field[2][2] == game_field[3][2] == players[1] or
                game_field[1][3] == game_field[2][3] == game_field[3][3] == players[1] or
                game_field[1][1] == game_field[2][2] == game_field[3][3] == players[1] or
                game_field[1][3] == game_field[2][2] == game_field[3][1] == players[1]
        ):
            print(f'<<{players[1]}>>, Вы победили, игра окончена!')
            flag = False
            break

    move = 'игрок делает ход'
    while move not in moves_variants:
        move = input(f'<<{players[0]}>>, ваш ход: ')
        if move in moves_variants:
            moves_variants.remove(move)
            break
        else:
            print('Будьте внимательнее!')

    line = int(move[0]) + 1
    column = int(move[1]) + 1
    game_field[line][column] = players[0]
    players.append(players[0])
    players.pop(0)
    moves += 1

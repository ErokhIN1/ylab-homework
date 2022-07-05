from typing import Tuple


def create_bord(s: int) -> Tuple[list, set]:
    matrix = [[chr(96 + j) if i == 0 else (str(i) if j == 0 else "_")
               for j in range(s + 1)] for i in range(s + 1)]
    matrix[0][0] = ''

    turns = set(i + j for i in map(str, range(1, s + 1))
                for j in map(str, range(1, s + 1)))
    return matrix, turns


def show_game(board: list):
    print()
    for row in board:
        row = list(map(lambda x: x.ljust(2), row))
        print(*row)
    return


def check_items(board: list) -> Tuple[set, set, set, set]:
    column = diagm = diagr = ''
    rows, columns, diagrama, diagrama_2 = set(), set(), set(), set()

    for i in range(1, len(board)):
        row = ''.join(board[i][1:])
        for j in range(1, len(board)):
            column += board[j][i]
        columns.add(column)
        rows.add(row)
        column = ''

    for step in range(len(board) - 5):
        for i in range(len(board) - 5):
            for j in range(1, 6):
                diagr += board[len(board) - j - i][j + step]
                diagm += board[j + i][j + step]
            diagrama.add(diagm)
            diagrama_2.add(diagr)
            diagm = diagr = ''
    return rows, columns, diagrama, diagrama_2


def check_result(board: list, turns: set, player_item: str, bot_item: str) -> bool:
    end_game = False
    win, lose, draw = '\nВы победитель!\n', '\nВы проиграли!\n', '\nИгра закончилась в ничью\n'
    good, bad = bot_item * 5, player_item * 5
    rows, columns, diagrama, diagrama_2 = check_items(board)
    items = rows | columns | diagrama | diagrama_2
    for t in items:
        if good in t:
            print(win)
            end_game = True
            break
        if bad in t:
            print(lose)
            end_game = True
            break
    if len(turns) == 0 and not end_game:
        print(draw)
        end_game = True
    return end_game


def bot_move(board: list, free_move: set, bot_item: str, d: dict) -> str:
    move = free_move.pop()
    if move.startswith('10'):
        x, y = 10, int(move[2:])
        print(f'\nХод компьютера: {d["10"]}{move[0]}')
    else:
        x, y = int(move[0]), int(move[1:])
        print(f"\nХод компьютера: {d[move[1:]]}{move[0]}")
    board[x][y] = bot_item
    show_game(board)
    return move


def player_move(board: list, player_item: str) -> str:
    dict_columns = {chr(96 + i): i for i in range(1, len(board))}
    d = dict_columns.copy()
    dict_rows = {str(i): i for i in range(1, len(board))}
    d.update(dict_rows)
    move = ''
    flag = False
    while not flag:
        move = input('\nВаш ход: ').lower()
        if len(move) < 2 or len(move) > 3:
            print("\nНеверный формат входных данных. Пример входных данных: 'A1'")
            continue
        if move[0].isdigit():
            move = move[-1] + move[:-1]
        column = move[0]
        row = move[1:]

        if column in dict_columns.keys() and row in dict_rows.keys():
            move = str(d[move[1:]]) + str(d[move[0]])

            if board[d[row]][d[column]] != '_':
                print("\nДанное поле уже занято!")
            else:
                board[d[row]][d[column]] = player_item
                flag = True
        else:
            print("\nНеверный формат входных данных. Пример входных данных: 'A1")
        show_game(board)
    return move


def main(size: int, player_item: str):
    board, turns = set(), []
    bot_item, d = '', {}
    end_game = False
    items = ['x', '0']
    if any([player_item not in items, size not in range(5, 11)]):
        end_game = True
        print('Неверные параметры при запуске!')
    else:
        d = {str(i + 1): chr(97 + i) for i in range(size)}
        items.remove(player_item)
        bot_item = ''.join(items)
        board, turns = create_bord(size)
        print(f'\nВы играете {player_item.upper()}')
    show_game(board)

    while not end_game:
        move = player_move(board, player_item)
        turns.remove(move)
        end_game = check_result(board, turns, player_item, bot_item)

        if not end_game:
            bot_move(board, turns, bot_item, d)
            end_game = check_result(board, turns, player_item, bot_item)


if __name__ == "__main__":
    main(player_item='x', size=10)

# Игровое поле
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# Проверка окончания игры
game_still_going = True

# Проверка победителя
winner = None

# Текущий игрок (начинает X)
current_player = "X"


# Запуск игры
def play_game():
    # Вызываем игровое поле
    display_board()

    while game_still_going:
        # Совершение хода
        player_moves(current_player)

        # Проверка окончания игры
        check_gameover()

        # Переход хода
        change_player()

    if winner == "X" or winner == "O":
        print(winner + " победил")
    elif winner == None:
        print("Ничья")

#Отображаем поле
def display_board():
    print("\n")
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])
    print("\n")


def player_moves(player):
    print(player + " ходит")
    position = input("Выберите цифру от 1 до 9: ")

    # Проверка ввода игрока
    valid = False
    while not valid:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Выберите цифру от 1 до 9: ")

        # Корректируем ввод игрока, так как в списке отчёт идёт с 0
        position = int(position) - 1

        # Проверяем что место доступно для ввода
        if board[position] == "-":
            valid = True
        else:
            print("Неправильный ход")

    # Фиксируем ход на поле
    board[position] = player

    # Вызываем игровое поле
    display_board()


# Проверка окончания игры
def check_gameover():
    check_winner()
    check_for_tie()


# Проверка наличия победителя
def check_winner():
    global winner
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None

# Проверка строк
def check_rows():
    global game_still_going

    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_still_going = False

    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    else:
        return None

# Проверка столбцов
def check_columns():
    global game_still_going
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    if column_1 or column_2 or column_3:
        game_still_going = False

    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    else:
        return None

# Проверка диагоналей
def check_diagonals():
    global game_still_going
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"
    if diagonal_1 or diagonal_2:
        game_still_going = False
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    else:
        return None

# Проверка на ничью
def check_for_tie():
    global game_still_going
    # Если всё поле заполнено
    if "-" not in board:
        game_still_going = False
        return True
    else:
        return False

# Переход хода другому игроку
def change_player():
    global current_player

    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"

play_game()
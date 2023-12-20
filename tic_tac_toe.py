# ==================================================================================== #
#                               КРЕСТИКИ-НОЛИКИ                                        #
# ==================================================================================== #
#                                                                                      #
#     Правила игры:                                                                    #
#     Игра для двух игроков.                                                           #
#     1. Выберете желаемую размерность игрового поля.                                  #
#     2. Первым ходит "X", затем "O".                                                  #
#     3. Вводите по очереди координаты выбранного вами поля:                           #
#        Например:                                                                     #
#        12 означает 1-й ряд, 2-й столбец;                                             #
#        33 означает 3-й ряд, 3-й столбец и т.д.                                       #
#     Победил тот, кто первм выставит подряд количество своих знаков ("X" bkb "O"),    #
#     равное выбранной размерности игрового поля.                                      #
#                                                                                      #
# ==================================================================================== #

def print_playing_field(matrix, dim):
    """ Вывод игрового поля в консоль """
    number_of_cell = [i + 1 for i in range(dim)]
    print('   ', end='')
    for num in number_of_cell:
        print('{: ^4}'.format(num), end='')
    print()
    row_counter = 0
    for row in matrix:
        print('  ' + '+---' * dim + '+')
        print(number_of_cell[row_counter], end=' ')
        row_counter += 1
        for cell in row:
            print(f'| {cell} ', end='')
        print('|')
    print('  ' + '+---' * dim + '+')


def congratulation_banner(winner):
    text = f'Игра окончена. Победили {winner}!'
    print('+-' + '-' * len(text) + '-+')
    print(f'| {text} |')
    print('+-' + '-' * len(text) + '-+')


def check_cell(coords, matrix):
    """ Проверка ячейки на занятость """
    if matrix[coords[0]][coords[1]] == ' ':
        return True
    print('Это поле занято!')
    return False


def check_input(coords, dim):
    """ Проверка корректности введенных пользователем данных """
    good_symbols = ''
    for i in range(1, dim + 1):
        good_symbols += str(i)
    if len(coords) == 2 and coords[0] in good_symbols and coords[1] in good_symbols:
        return True
    print('Введите номер поля в правильном формате!')
    return False


def check_winner(matrix, dim):
    """ Проверка победителя """

    # проверка горизонталей:
    for i_row in matrix:
        symbol = i_row[0]
        row = list(filter(lambda x: x == symbol and x != ' ', i_row))
        if len(row) == dim:
            congratulation_banner(row[0])
            return True

    # проверка вертикалей:
    for i in range(dim):
        j_col = []
        for j in range(dim):
            j_col.append(matrix[j][i])
        symbol = j_col[0]
        col = list(filter(lambda x: x == symbol and x != ' ', j_col))
        if len(col) == dim:
            congratulation_banner(col[0])
            return True

    # проверка главной диагонали:
    diagonal = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == j:
                diagonal.append(matrix[i][j])
    symbol = diagonal[0]
    diagonal = list(filter(lambda x: x == symbol and x != ' ', diagonal))
    if len(diagonal) == dim:
        congratulation_banner(diagonal[0])
        return True

    # проверка побочной диагонали:
    diagonal = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == len(matrix) - 1 - j:
                diagonal.append(matrix[i][j])
    symbol = diagonal[0]
    diagonal = list(filter(lambda x: x == symbol and x != ' ', diagonal))
    if len(diagonal) == dim:
        congratulation_banner(diagonal[0])
        return True


def check_playing_field(matrix):
    """ Проверка свободных ячеек в игровом поле """
    free_cells = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == ' ':
                free_cells.append(1)
    if len(free_cells) == 0:
        return True
    return False


def input_data(player_x, player_o, dim):
    step = 'X' if player_x else 'O'
    while True:
        coords = input(f'{step}, введите номер поля: ')
        if check_input(coords, dim):
            coords = list(map(lambda x: int(x) - 1, coords))
            if check_cell(coords, play_matrix):
                if player_x:
                    play_matrix[coords[0]][coords[1]] = 'X'
                elif player_o:
                    play_matrix[coords[0]][coords[1]] = 'O'
                print_playing_field(play_matrix, dim)
                break


def play_the_game(x, o, dim):
    stop_game = False
    while not stop_game:
        input_data(x, o, dim)
        x, o = o, x
        if check_winner(play_matrix, dim):
            stop_game = True
        if check_playing_field(play_matrix):
            print('Игра окончена. Победителя нет!')
            stop_game = True


print('\
------------------ КРЕСТИКИ-НОЛИКИ ------------------\n\
  Игра для двух игроков.\n\
  Первым ходит "X", затем "O".\n\
  Вводите по очереди координаты выбранного вами поля.\n\
  Например:\n\
  12 означает 1-й ряд, 2-й столбец;\n\
  33 означает 3-й ряд, 3-й столбец и т.д.\n\
-----------------------------------------------------')
dimension = int(input('Введите размерность игрового поля: '))
play_matrix = [[' ' for j in range(dimension)] for i in range(dimension)]
print_playing_field(play_matrix, dimension)

player_X = True
player_O = False

play_the_game(player_X, player_O, dimension)

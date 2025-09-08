BLANK = '  '
X = 'X'
O = 'O'
N = 3
MAX_TRIES = N*N
isGame = True
tries = 0
turn = X

matrix = [
    [BLANK, BLANK, BLANK],
    [BLANK, BLANK, BLANK],
    [BLANK, BLANK, BLANK]
]


def print_mat(mat, whos_turn):
    print(f"{whos_turn} to play")
    for row in range(N):
        for cell in range(N-1):
            print(mat[row][cell], end="|")
        print(mat[row][N-1])
        if row != N-1:
            print("--------")

def valid_input(sign):
    cord = int(input(f"Enter {sign} cord (1~{N}): "))
    while not 1 <= cord <= N:
        cord = int(input(f"Enter {sign} cord (1~{N}): "))
    return cord - 1

def toggle(whos_turn):
    if whos_turn == X:
        return O
    return X

def is_there_a_winner(mat, is_game):
    a_row = []
    a_col = []
    for row in mat:
        a_row.append(row[0])
        a_row = [x for x in row[0] if x in a_row]
        if len(a_row) == N:
            print("Win")
            return False
    for



    for row in mat:
        how_much_in_row = 0
        for col in mat:
            how_much_in_row += 1
            if how_much_in_row == N:
                print("Win")
                is_game = False
    for col_index in len(mat)-1:
        for row_index in len(mat) - 1:
            mat[]

    return is_game




while isGame and tries < MAX_TRIES:
    print_mat(matrix, turn)
    col = valid_input('x')
    row = valid_input('y')

    if matrix[row][col] == BLANK:
        matrix[row][col] = turn
        tries += 1
        turn = toggle(turn)
    else:
        print("The place isn't BLANK!!!")
        print("Play again")



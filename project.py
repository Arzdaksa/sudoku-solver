import random

FINISH_SUCCESS = "FINISH SUCCESS"
FINISH_FAILURE = "FINISH FAILURE"
NOT_FINISHED = "NOT FINISHED"
CANT_SOLVE = "CANT SOLVE"
UNSOLVABLE = "UNSOLVABLE"

BOARD_SIZE = 9
LEGAL_NUMBERS = [1,2,3,4,5,6,7,8,9]

example_board = [[5,3,-1,-1,7,-1,-1,-1,-1],
                 [6,-1,-1,-1,-1,-1,1,-1,-1],
                 [-1,-1,9,-1,-1,-1,-1,6,-1],
                 [-1,-1,-1,-1,6,-1,-1,-1,3],
                 [-1,-1,-1,8,-1,3,-1,-1,1],
                 [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                 [-1,6,-1,-1,-1,-1,-1,-1,-1],
                 [-1,-1,-1,-1,1,-1,-1,-1,-1],
                 [-1,-1,-1,-1,8,-1,-1,-1,9]]

board2 = [[-1,6,-1,4,3,-1,-1,-1,1],
         [5,-1,-1,-1,7,-1,-1,-1,-1],
         [-1,1,-1,9,-1,-1,8,-1,-1],
         [-1,-1,-1,-1,-1,2,3,-1,9],
         [-1,8,-1,-1,-1,-1,-1,6,-1],
         [-1,-1,-1,-1,-1,-1,-1,-1,-1],
         [-1,-1,-1,-1,-1,-1,-1,-1,-1],
         [9,-1,2,3,-1,-1,-1,-1,4],
         [-1,-1,4,7,2,-1,-1,-1,8]]

board1 = [[5,-1, 4,-1, 7,-1,-1, 1,-1],
         [6,-1, 2, 1,-1,-1, 3,-1,-1],
         [1,-1, 8,-1, 4,-1,-1, 6,-1],
         [-1, 5,-1,-1, 6,-1,-1, 2,-1],
         [-1, 2,-1, 8,-1, 3,-1,-1,-1],
         [-1,-1,-1,-1,-1, 4,-1, 5, 6],
         [-1, 6, 1, 5, 3, 7, 2, 8, 4],
         [-1, 8, 7,-1, 1, 9,-1, 3,-1],
         [-1,-1,-1, 2, 8,-1,-1,-1, 9]]

empty_board = [[-1,-1,-1,-1,-1,-1,-1,-1,-1],
                 [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                 [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                 [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                 [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                 [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                 [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                 [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                 [-1,-1,-1,-1,-1,-1,-1,-1,-1]]

second_example = [[-1,-1,-1,-1,1,-1,7,5,6],
                 [-1,3,7,-1,8,9,1,2,4],
                 [-1,2,5,-1,-1,-1,-1,-1,-1],
                 [-1,-1,9,6,-1,-1,-1,8,2],
                 [-1,-1,6,-1,3,-1,-1,-1,-1],
                 [7,-1,4,-1,-1,-1,9,-1,-1],
                 [-1,-1,-1,-1,-1,-1,-1,-1,5],
                 [-1,4,2,-1,-1,-1,8,1,7],
                 [5,-1,3,-1,-1,8,6,-1,9]]

bug_board = [[5,3,4,6,7,8,9,1,2],
             [6,7,2,1,9,5,3,4,9],
             [1,9,8,3,4,2,5,6,7],
             [8,5,9,7,6,1,4,2,3],
             [4,2,6,8,5,3,7,9,1],
             [7,1,3,9,2,4,8,5,6],
             [9,6,1,5,3,7,2,8,4],
             [2,8,7,4,1,9,6,3,5],
             [3,4,5,2,8,6,1,7,9]]

impossible_board = [[5,1,6,8,4,9,7,3,2],
                 [3,-1,7,6,-1,5,-1,-1,-1],
                 [8,-1,9,7,-1,-1,-1,6,5],
                 [1,3,5,-1,6,-1,9,-1,7],
                 [4,7,2,5,9,1,-1,-1,6],
                 [9,6,8,3,7,-1,-1,5,-1],
                 [2,5,3,1,8,6,-1,7,4],
                 [6,8,4,2,-1,7,5,-1,-1],
                 [7,9,1,-1,5,-1,6,-1,8]]

interesting_board = [[5,3,4,6,7,8,9,1,2],
                     [6,7,2,1,9,5,3,4,8],
                     [1,9,8,3,4,2,5,6,7],
                     [-1,-1,-1,7,6,1,4,2,3],
                     [-1,-1,-1,8,5,3,7,9,1],
                     [-1,-1,-1,9,2,4,8,5,6],
                     [-1,-1,-1,-1,3,7,2,8,4],
                     [-1,-1,-1,-1,1,9,6,3,5],
                     [-1,-1,-1,-1,8,6,1,7,9]]

perfect_board = [[5,3,4,6,7,8,9,1,2],
                 [6,7,2,1,9,5,3,4,8],
                 [1,9,8,3,4,2,5,6,7],
                 [8,5,9,7,6,1,4,2,3],
                 [4,2,6,8,5,3,7,9,1],
                 [7,1,3,9,2,4,8,5,6],
                 [9,6,1,5,3,7,2,8,4],
                 [2,8,7,4,1,9,6,3,5],
                 [3,4,5,2,8,6,1,7,9]]

#print the board and return it as a str
def print_board(sudoku_board:list) -> list:
    board_str = []
    for i in range(0, BOARD_SIZE):
        board_str.append(make_row_str(sudoku_board[i]))
    for i in board_str:
        print(i)

    return board_str

def make_row_str(board_row: list) -> str:
    row_str = "|"
    for i in board_row:
        if i in LEGAL_NUMBERS:
            row_str += str(i)
        else:
            row_str += "-1"
        row_str += "|"
    return row_str


#loc = (i, j)
#remove cell options by checking the columns
def check_column (sudoku_board, loc, cell_options) -> list:
    for i in range(len(sudoku_board)):
        if sudoku_board[i][loc[1]] != -1 and sudoku_board[i][loc[1]] in cell_options:
            cell_options.remove(sudoku_board[i][loc[1]])

    return cell_options

# loc = (i, j)
#remove cell options by checking the rows
def check_row(sudoku_board, loc, cell_options) -> list:
    for i in range(len(sudoku_board)):
        if sudoku_board[loc[0]][i] != -1 and sudoku_board[loc[0]][i] in cell_options:
            cell_options.remove(sudoku_board[loc[0]][i])

    return cell_options

#return the possible options for a specific cell
def options (sudoku_board, loc) -> list:
    cell_options = [1,2,3,4,5,6,7,8,9]
    cell_options = check_row(sudoku_board, loc, cell_options)
    cell_options = check_column(sudoku_board, loc, cell_options)
    cell_options = check_square(sudoku_board, loc, cell_options)
    return cell_options

#remove cell options by checking the 3*3 square
def check_square(sudoku_board: [], loc: tuple, cell_options: []) -> list:  # בודק כל מצב אפשרי
    new_i = loc[0] - loc[0] % 3
    new_j = loc[1] - loc[1] % 3
    for i in range(new_i, new_i + 3):
        for j in range(new_j, new_j + 3):
            if j == loc[1] and i == loc[0]:
                continue
            else:
                if sudoku_board[i][j] != -1 and sudoku_board[i][j] in cell_options:
                    cell_options.remove(sudoku_board[i][j])
    return cell_options

#check and input into each cell the options for the specific cell
def possible_digits (sudoku_board:list) -> list:
    for j in range(BOARD_SIZE):
        for i in range(BOARD_SIZE):
            if sudoku_board[j][i] not in LEGAL_NUMBERS:
                sudoku_board[j][i] = options(sudoku_board, (j, i))
    return sudoku_board

#solve the board until no cells have 1 option
def one_stage (sudoku_board:list, possibilities:list) -> tuple:
    doubles = True
    max_runs = BOARD_SIZE * BOARD_SIZE
    runs_count = 0
    while check_fill_board(sudoku_board) and runs_count != max_runs:
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if possibilities[i][j] not in LEGAL_NUMBERS:
                    if len(possibilities[i][j]) == 1:
                        sudoku_board[i][j] = possibilities[i][j][0]
                        possibilities = possible_digits(sudoku_board)
                        doubles = doubles_check(sudoku_board,i,j,sudoku_board[i][j])

                        if not doubles:
                            return FINISH_FAILURE, sudoku_board
        runs_count += 1

    if not check_fill_board(sudoku_board):
        return FINISH_SUCCESS, sudoku_board

    elif check_fill_board(sudoku_board):
        min = 9
        index_of_min = ()
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if sudoku_board[i][j] not in LEGAL_NUMBERS and sudoku_board[i][j] != -1:
                    if len(sudoku_board[i][j]) < min:
                        min = len(sudoku_board[i][j])
                        index_of_min = NOT_FINISHED ,i , j, sudoku_board[i][j], sudoku_board

        if index_of_min == ():
            return CANT_SOLVE, sudoku_board

        return index_of_min

#result = (error type, column index, row index, options, sudoku board) or (message, sudoku board)
#checks the board status and acts accordingly
def fill_board(sudoku_board:list) -> tuple:
    result = one_stage(sudoku_board, possible_digits(sudoku_board))
    while result[0] == NOT_FINISHED:
        if not result[3]:
            print(UNSOLVABLE)
            return result[0], sudoku_board

        if result[0] == NOT_FINISHED:
            print_board(sudoku_board)
            print("Please enter one of the following options", result[3], "for index", result[1], result[2], ":")
            choice = int(input())
            if choice in result[3]:
                sudoku_board[result[1]][result[2]] = choice
                result = one_stage(sudoku_board, possible_digits(sudoku_board))

    print_board(sudoku_board)
    print(result[0])
    return result[0], sudoku_board

#checks if the board has been solved
def check_fill_board(sudoku_board:list) -> bool:
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if sudoku_board[i][j] not in LEGAL_NUMBERS:
                return True
    return False

#copies board
def copy_board (copy_this:list) -> list:
    temp = []
    for row in copy_this:
        temp.append(row.copy())

    return temp

#checks if the board has doubles
def doubles_check(sudoku_board:list,i:int,j:int,num:int) -> bool:
    new_i = i - i % 3
    new_j = j - j % 3
    for k in range (new_i,new_i+3):#square check
        for m in range(new_j,new_j+3):
            if k == i and m == j:
                continue
            elif sudoku_board[k][m] == num:
                    return False

    for k in range (9):#culumn check
        if k == i:
            continue
        elif sudoku_board[k][j] == num:
            return False

    for k in range(9):#row check
        if k == j :
            continue
        elif num == sudoku_board[i][k]:
            return False
    return True

#creates a random board
def create_random_board(sudoku_board) -> list:
    n_to_fill = random.randrange(10, 21)
    for p in range(n_to_fill):
        random_i = random.randrange(0, 9)
        random_j = random.randrange(0, 9)
        if sudoku_board[random_i][random_j] not in LEGAL_NUMBERS:
            cell_option = options(sudoku_board, (random_i, random_j))
            random_k = random.randrange(0, len(cell_option) - 1)
            sudoku_board[random_i][random_j] = cell_option[random_k]
        else:
            p -= 1

    return sudoku_board

#writes boards result onto a txt file
def print_to_file(sudoku_board, file_name="solved_sudoku.txt"):
    my_file = open(file_name, "a")
    if sudoku_board[0] == FINISH_SUCCESS:
        my_file.write("Here is the solved board:")
        my_file.write("\n-------------------\n")
        for row in range(BOARD_SIZE):
            my_file.write(make_row_str(sudoku_board[1][row]))
            my_file.write("\n-------------------\n")

    elif sudoku_board[0] == UNSOLVABLE:
        my_file.write("Board Is Unsolvable!")

    else:
        my_file.write("Board Is Not Legit!")

    my_file.write("\n-------------------\n ")
    my_file.close()


new_file = open("solved_sudoku.txt", "w").close()
solved_board1  = fill_board(board1)
print_to_file(solved_board1)

solved_example_board  = fill_board(example_board)
print_to_file(solved_example_board)

solved_board2  = fill_board(board2)
print_to_file(solved_board2)

solved_perfect_board  = fill_board(perfect_board)
print_to_file(solved_perfect_board)

solved_impossible_board = fill_board(impossible_board)
print_to_file(solved_impossible_board)

solved_bug_board = fill_board(bug_board)
print_to_file(solved_bug_board)

solved_interesting_board  = fill_board(interesting_board)
print_to_file(solved_interesting_board)

random_board = create_random_board(empty_board)
solved_random_board = fill_board(random_board)
print_to_file(solved_random_board)
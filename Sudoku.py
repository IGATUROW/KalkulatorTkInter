def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j], end=" ")
        print()

def is_valid_move(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid_move(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def is_equal(board1, board2):
    for i in range(9):
        for j in range(9):
            if board1[i][j] != board2[i][j]:
                return False
    return True

def play_sudoku():
    solved_board = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ]

    current_board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("Witaj w grze Sudoku!")
    print("Instrukcja: Wprowadź numer wiersza (0-8) i numer kolumny (0-8), a następnie wprowadź liczbę (1-9) do wypełnienia pola.")

    while True:
        print_board(current_board)
        row = int(input("Podaj numer wiersza (0-8): "))
        col = int(input("Podaj numer kolumny (0-8): "))
        num = int(input("Podaj liczbę (1-9) do wypełnienia pola: "))

        if row < 0 or row > 8 or col < 0 or col > 8 or num < 1 or num > 9:
            print("Błąd: Nieprawidłowe dane wejściowe. Wprowadź prawidłowe dane.")
            continue

        if is_valid_move(current_board, row, col, num):
            current_board[row][col] = num
        else:
            print("Błąd: Ten ruch jest nieprawidłowy. Spróbuj ponownie.")

        if is_equal(current_board, solved_board):
            print("Gratulacje! Wygrałeś grę Sudoku!")
            break

if __name__ == "__main__":
    play_sudoku()
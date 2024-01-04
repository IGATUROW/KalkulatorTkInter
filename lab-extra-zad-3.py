# Gra "Kółko i krzyżyk"

# stałe globalne
KOMPUTER = "X"
CZLOWIEK = "O"
EMPTY = " "
TIE = "REMIS"
NUM_SQUARES = 9


# Instrukcja gry

def display_instruct():
    """Wyświetl instrukcję gry"""
    print(
        """
        Witaj w grze Kółko i krzyżyk. 
        Ja gram "X"
        A Ty "O"
    
        Aby ze mną zagrać, będziesz musiał wprowadzić cyfrę od 1 do 9.
        Cyfra ta odpowiada pozycji na planszy zgodnie z poniższym schematem:
    
                    +-------+-------+-------+
                    |       |       |       |
                    |   1   |   2   |   3   |
                    |       |       |       |
                    +-------+-------+-------+
                    |       |       |       |
                    |   4   |   5   |   6   |
                    |       |       |       |
                    +-------+-------+-------+
                    |       |       |       |
                    |   7   |   8   |   9   |
                    |       |       |       |
                    +-------+-------+-------+
    
        Zaczynamy!\n
        """
    )


def ask_number(question, low, high):
    """Poproś o liczbę z odpowiedniego zakresu"""
    response = None
    while response not in range(low, high):
        response = int(input(question))
        if response not in range(low, high):
            print("Wybierz liczbę od", low, "do", high - 1)
    return response - 1  # Odejmujemy 1, aby dostosować się do indeksowania od 0


def new_board():
    """Utwórz nową planszę gry"""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


def display_board(board):
    print("\n\t", "+-------+-------+-------+")
    print("\t", "|", "\t\t", "|", "\t\t", "|", "\t\t", "|")
    print("\t", "|", "\t", board[0], "\t", "|", "\t", board[1], "\t", "|", "\t", board[2], "\t", "|")
    print("\t", "|", "\t\t", "|", "\t\t", "|", "\t\t", "|")
    print("\t", "+-------+-------+-------+")
    print("\t", "|", "\t\t", "|", "\t\t", "|", "\t\t", "|")
    print("\t", "|", "\t", board[3], "\t", "|", "\t", board[4], "\t", "|", "\t", board[5], "\t", "|")
    print("\t", "|", "\t\t", "|", "\t\t", "|", "\t\t", "|")
    print("\t", "+-------+-------+-------+")
    print("\t", "|", "\t\t", "|", "\t\t", "|", "\t\t", "|")
    print("\t", "|", "\t", board[6], "\t", "|", "\t", board[7], "\t", "|", "\t", board[8], "\t", "|")
    print("\t", "|", "\t\t", "|", "\t\t", "|", "\t\t", "|")
    print("\t", "+-------+-------+-------+")


def legal_moves(board):
    """Utwórz listę prawidłowych ruchów"""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves


def winner(board):
    """Ustal zwycięzcę"""
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            return board[row[0]]

    if EMPTY not in board:
        return TIE

    return None


def human_move(board, CZLOWIEK):
    """Odczytaj ruch człowieka"""
    legal = legal_moves(board)
    move = None
    while move not in legal:
        display_board([str(i + 1) if square == EMPTY else square for i, square in enumerate(board)])
        move = ask_number("Jaki będzie Twój ruch? (1-9): ", 1, NUM_SQUARES + 1)
        if move not in legal:
            print("\nTo pole jest już zajęte lub numer jest niepoprawny. Wybierz inne: ")
    print("Znakomicie...")
    return move


def computer_move(board, KOMPUTER, CZLOWIEK):
    """Spowoduj wykonanie ruchu przez komputer."""
    # utwórz kopię roboczą, ponieważ funkcja będzie zmieniać listę
    board_copy = board[:]

    # najlepsze pozycje według kolejności
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    # jeśli komputer może wygrać, wykonaj ten ruch
    for move in legal_moves(board):
        board_copy[move] = KOMPUTER
        if winner(board_copy) == KOMPUTER:
            return move
        # ten ruch został sprawdzony, wycofaj go
        board_copy[move] = EMPTY

    # jeśli człowiek może wygrać, zablokuj ten ruch
    for move in legal_moves(board):
        board_copy[move] = CZLOWIEK
        if winner(board_copy) == CZLOWIEK:
            return move
        # ten ruch został sprawdzony, wycofaj go
        board_copy[move] = EMPTY

    # ponieważ nikt nie może wygrać w kolejnym ruchu, wybierz najlepsze wolne pole
    for move in BEST_MOVES:
        if move in legal_moves(board):
            return move


def next_turn(turn):
    """Zmień wykonawcę ruchu"""
    if turn == KOMPUTER:
        return CZLOWIEK
    else:
        return KOMPUTER


def congrat_winner(the_winner, KOMPUTER, CZLOWIEK):
    """Pogratuluj zwycięzcy"""
    if the_winner != TIE:
        print(the_winner, "jest zwycięzcą!\n")
    else:
        print("Remis!\n")

    if the_winner == KOMPUTER:
        print("Ja wygrałem! Ty przegrałeś!\n")

    elif the_winner == CZLOWIEK:
        print("Gratulacje! Wygrałeś!\n")

    elif the_winner == TIE:
        print("Remis! Dziś nikt nie wygrał!")


def main():
    display_instruct()
    turn = KOMPUTER
    board = new_board()
    display_board(board)
    while not winner(board):
        if turn == CZLOWIEK:
            move = human_move(board, CZLOWIEK)
            board[move] = CZLOWIEK
        else:
            move = computer_move(board, KOMPUTER, CZLOWIEK)
            board[move] = KOMPUTER
        display_board(board)
        turn = next_turn(turn)

    the_winner = winner(board)
    display_board([str(i + 1) for i in range(NUM_SQUARES)])  # Wyświetl numerację pól przed zakończeniem gry
    congrat_winner(the_winner, KOMPUTER, CZLOWIEK)


# rozpocznij program
main()
input("\n\nAby zakończyć grę, naciśnij klawisz Enter.")

board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]


def print_board(board):
    line = '---+---+---'
    print(line)
    for row in board:
        print(f' {row[0]} | {row[1]} | {row[2]}')
        print(line)


def check_winner(board):
    # check rows
    for row in board:
        # [" ", " ", " "]
        if row[0] == row[1] == row[2] != " ":
            return True
    # check columns
    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] != ' ':
            return True
    # Check Diagonals
    if (board[0][0] == board[1][1] == board[2][2] != ' ' or
            board[0][2] == board[1][1] == board[2][0] != ' '):
        return True

    return False


def is_full(board):
    for row in board:
        if ' ' in row:
            return False

    return True


def main():

    print_board(board)

    current_player = 'X'
    while True:
        print(f"Player {current_player}'s turn")
        row = int(input("Enter row (0-2): "))
        column = int(input("Enter column (0-2): "))

        if board[row][column] == " ":
            board[row][column] = current_player
        else:
            print("This spot is already taken!")
            continue

        print_board(board)

        if check_winner(board):
            print(f"Player {current_player} wins!")
            break

        if is_full(board):
            print(f'Board is full')
            break

        current_player = 'O' if current_player == 'X' else 'X'

        print()


if __name__ == '__main__':
    main()

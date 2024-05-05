import random

class TicTacToe:
    def __init__(self):
        self.board = []

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)

    def get_random_first_player(self):
        return random.choice(['X', 'O'])

    def fix_spot(self, row, col, player):
        if row not in range(1, 4) or col not in range(1, 4):
            print("Error: Row and column numbers should be between 1 and 3.")
            return False  # Invalid input, spot not marked
        if self.board[row - 1][col - 1] == '-':
            self.board[row - 1][col - 1] = player
            return True  # Spot successfully marked
        else:
            print("Error: Spot already marked. Choose another spot.")
            return False

    def is_player_win(self, player):
        n = len(self.board)

        # checking rows
        for i in range(n):
            if all(self.board[i][j] == player for j in range(n)):
                return True

        # checking columns
        for i in range(n):
            if all(self.board[j][i] == player for j in range(n)):
                return True

        # checking diagonals
        if all(self.board[i][i] == player for i in range(n)):
            return True

        if all(self.board[i][n - 1 - i] == player for i in range(n)):
            return True

        return False

    def is_board_filled(self):
        return all(item != '-' for row in self.board for item in row)

    def swap_player_turn(self, player):
        return 'X' if player == 'O' else 'O'

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def start(self):
        self.create_board()
        player = self.get_random_first_player()

        while True:
            print(f"Player {player}'s turn")
            self.show_board()

            # taking user input
            row_col_input = input("Enter row and column numbers to fix spot: ").strip()
            if not row_col_input:
                print("Error: Input cannot be blank. Please enter row and column numbers.")
                continue

            try:
                row, col = map(int, row_col_input.split())
            except ValueError:
                print("Error: Input should be two integers separated by a space.")
                continue

            # fixing the spot
            spot_marked = self.fix_spot(row, col, player)

            # checking whether the current player has won or not
            if self.is_player_win(player):
                print(f"Player {player} wins the game!")
                break

            # checking whether the game is a draw or not
            if self.is_board_filled():
                print("Match Draw!")
                break

            # swapping the turn if the spot was successfully marked
            if spot_marked:
                player = self.swap_player_turn(player)


if __name__ == "__main__":
    # starting the game
    tic_tac_toe = TicTacToe()
    tic_tac_toe.start()

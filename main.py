import os

class TicTacToe:
    """Console-based TicTacToe game using a simple OOP design.

    Attributes:
        board: Linear list of 9 cells (" ", "X", "O").
        current_player: The active player symbol ("X" or "O").
    """

    # All winning line index triples (rows, columns, diagonals)
    WINS = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    
    def __init__(self):
        self.board = [" "] * 9
        self.current_player = "X"

    def display_board(self):
        """Print the current board layout."""
        for i in range(0, 9, 3):
            print(f"{self.board[i]} | {self.board[i+1]} | {self.board[i+2]}")
            if i < 6:
                print("--+---+--")

    def clear_screen(self):
        """Clear the console for a cleaner game experience."""
        os.system("cls" if os.name == "nt" else "clear")

    def get_valid_move(self):
        """Prompt the current player until a valid move is entered.

        Returns:
            An integer board index in the range [0, 8].
        """
        while True:
            try:
                player_num = int(input(f"Player {self.current_player}, choose a position (0-8): "))
            except ValueError:
                print("Invalid input, please enter a number.")
                continue

            # Guard: reject out-of-range positions early
            if not 0 <= player_num <= 8:
                print("Position out of range (0-8).")
                continue
            # Guard: cell must be empty
            if self.board[player_num] != " ":
                print("Field is already occupied.")
                continue
            return player_num
                
    def make_move(self, position):
        """Place the current player's symbol on the board.

        Args:
            position: Zero-based index of the target cell. Assumed valid.
        """
        self.board[position] = self.current_player
    
    def check_winner(self):
        for a,b,c in TicTacToe.WINS:
            s = self.board[a]
            if s != " " and all(self.board[i] == s for i in (a,b,c)):
                return s
        return None

    def is_draw(self):
        """Return True if the board is full (assuming winner was checked first)."""
        return " " not in self.board
                
    def switch_player(self):
        """Toggle the current player between X and O."""
        self.current_player = "O" if self.current_player == "X" else "X"
        
    def play(self):
        """Run the main game loop"""
        while True:
            self.clear_screen()
            self.display_board()
            pos = self.get_valid_move()
            self.make_move(pos)

            winner = self.check_winner()
            if winner:
                self.clear_screen()
                self.display_board()
                print(f"Player {winner} has won")
                break
            elif self.is_draw():
                self.clear_screen()
                self.display_board()
                print("It's a draw!")
                break
            self.switch_player()

        # replay prompt
        choice = input("Play again? (y/n): ").strip().lower()
        if choice == "y":
            self.board = [" "] * 9
            self.current_player = "X"
            self.play()
        
if __name__ == "__main__":
    game = TicTacToe()
    game.play()
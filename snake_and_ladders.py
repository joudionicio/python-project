import random

class SnakeAndLadders:
    def __init__(self):
        self.board = self.create_board()
        self.players = [0, 0]  # Starting positions for two players
        self.current_player = 0

    def create_board(self):
        # Create a board with snakes and ladders
        board = list(range(101))  # 0 to 100
        # Define snakes (start: end)
        snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
        # Define ladders (start: end)
        ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

        for start, end in snakes.items():
            board[start] = end
        for start, end in ladders.items():
            board[start] = end

        return board

    def roll_dice(self):
        return random.randint(1, 6)

    def move_player(self, player):
        roll = self.roll_dice()
        print(f"Player {player + 1} rolled a {roll}")
        self.players[player] += roll

        if self.players[player] > 100:
            print(f"Player {player + 1} cannot move, overshoot!")
            self.players[player] -= roll  # Move back if overshoot
        else:
            self.players[player] = self.board[self.players[player]]
            print(f"Player {player + 1} is now on square {self.players[player]}")

    def check_winner(self):
        if self.players[self.current_player] == 100:
            print(f"Player {self.current_player + 1} wins!")
            return True
        return False

    def play_game(self):
        while True:
            self.move_player(self.current_player)
            if self.check_winner():
                break
            self.current_player = (self.current_player + 1) % 2  # Switch player

if __name__ == "__main__":
    game = SnakeAndLadders()
    game.play_game()

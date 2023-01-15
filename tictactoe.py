class TicTacToe:
    def __init__(self):
        self.board = [" " for x in range(9)]
        self.player = "X"
        self.winner = None

    def draw_board(self):
        print(" %c | %c | %c " % (self.board[0], self.board[1], self.board[2]))
        print("___|___|___")
        print(" %c | %c | %c " % (self.board[3], self.board[4], self.board[5]))
        print("___|___|___")
        print(" %c | %c | %c " % (self.board[6], self.board[7], self.board[8]))
        print("   |   |   ")

    def check_for_winner(self):
        for x in range(0, 9, 3):
            if (self.board[x] == self.board[x + 1] == self.board[x + 2]) and self.board[x] != " ":
                self.winner = self.board[x]
                return True
        for x in range(3):
            if (self.board[x] == self.board[x + 3] == self.board[x + 6]) and self.board[x] != " ":
                self.winner = self.board[x]
                return True
        if (self.board[0] == self.board[4] == self.board[8]) and self.board[0] != " ":
            self.winner = self.board[0]
            return True
        if (self.board[2] == self.board[4] == self.board[6]) and self.board[2] != " ":
            self.winner = self.board[2]
            return True
        return False

    def play(self):
        while not self.check_for_winner():
            self.draw_board()
            print("Player %s choose where to place a marker (1-9):" % self.player)
            choice = int(input()) - 1
            if self.board[choice] == " ":
                self.board[choice] = self.player
                if self.player == "X":
                    self.player = "O"
                else:
                    self.player = "X"
            else:
                print("Space already filled. Try again.")
        self.draw_board()
        if self.winner == "X":
            print("X wins!")
        elif self.winner == "O":
            print("O wins!")
        else:
            print("It's a tie!")

game = TicTacToe()
game.play()
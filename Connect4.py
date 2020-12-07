
DARKCYAN = "\033[36m"
PURPLE = "\033[95m"
BLUE = "\033[94m"
GREEN = "\033[92m"
RED = "\033[91m"
BOLD = "\033[1m"
END = "\033[0m"


class Game:
    def __init__(self):
        self.board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
        ]

    def display(self):
        for row in self.board:
            print(" ", end="")
            for i in row:
                clr = None
                if i == 0:
                    clr = DARKCYAN
                if i == 1:
                    clr = BLUE
                if i == 2:
                    clr = RED
                print(clr + str(i) + END, end=" ")
            print()
        print("_______________")
        print(" 0 1 2 3 4 5 6\n")

    def valid_move(self, col):
        if 0 <= col <= 6 and not self.board[0][col]:
            return True
        return False

    def valid_columns(self):
        cols = []
        for i in range(len(self.board[0])):
            if self.board[0][i] == 0:
                cols.append(i)
        return cols

    def board_full(self):
        return self.valid_columns() == []

    def player_turn(self, col):
        self.drop_piece(col, 1)

    def ai_turn(self):
        result = self.minimax(0, 0, -1000000, 1000000, True)
        self.drop_piece(result[0], 2)
        print("Heuristic: ", result[1])

    def drop_piece(self, col, plr):
        row = 5
        while self.board[row][col] != 0:
            row -= 1
        self.board[row][col] = plr

    def withdraw_piece(self, col):
        row = 0
        while self.board[row][col] == 0:
            row += 1
        self.board[row][col] = 0

    def minimax(self, col, depth, alpha, beta, maximizing_player):
        if depth == 3 or self.winner():
            return [col, self.heuristic(self.board, col)]

        if maximizing_player:
            max_best = [6, -1000000]
            for pos in self.valid_columns():
                self.drop_piece(pos, 2)
                score = self.minimax(pos, depth+1, alpha, beta, False)
                max_best = max(max_best, score, key=lambda eval: eval[1])
                self.withdraw_piece(pos)
                alpha = max(alpha, score[1])
                if beta <= alpha:
                    break
            return max_best
        else:
            min_best = [6, 1000000]
            for pos in self.valid_columns():
                self.drop_piece(pos, 1)
                score = self.minimax(pos, depth+1, alpha, beta, True)
                min_best = min(min_best, score, key=lambda eval: eval[1])
                self.withdraw_piece(pos)
                beta = min(beta, score[1])
                if beta <= alpha:
                    break
            return min_best

    # @staticmethod
    def heuristic(self, grid, pos):
        ai = self.streaks4(2) + self.streaks3(2) + self.streaks2(2)
        pl = self.streaks4(1) + self.streaks3(1) + self.streaks2(1)
        score = ai - pl
        row = 0
        while grid[row][pos] == 0:
            row += 1
        if row < 5:
            if 1 == grid[row+1][pos] and self.streaks3(1) > 1:
                score += 10
            else:
                score += -1
        #
        # if self.winner():
        #     score = 6
        return score

    def streaks4(self, plr):
        count = 0
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j]:
                    if j <= 3:
                        if self.board[i][j] == self.board[i][j + 1] == \
                                self.board[i][j + 2] == self.board[i][j + 3] == plr:
                            count += 1
                    if i <= 2:
                        if self.board[i][j] == self.board[i + 1][j] == \
                                self.board[i + 2][j] == self.board[i + 3][j] == plr:
                            count += 1
                    if j <= 3 and i <= 2:
                        if self.board[i][j] == self.board[i + 1][j + 1] == \
                                self.board[i + 2][j + 2] == self.board[i + 3][j + 3] == plr:
                            count += 1
                    if j >= 3 and i <= 2:
                        if self.board[i][j] == self.board[i + 1][j - 1] == \
                                self.board[i + 2][j - 2] == self.board[i + 3][j - 3] == plr:
                            count += 1
        return count * 4

    def streaks3(self, plr):
        count = 0
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j]:
                    if j <= 4:
                        if self.board[i][j] == self.board[i][j + 1] == \
                                self.board[i][j + 2] == plr:
                            count += 1
                    if i <= 3:
                        if self.board[i][j] == self.board[i + 1][j] == \
                                self.board[i + 2][j] == plr:
                            count += 1
                    if j <= 4 and i <= 3:
                        if self.board[i][j] == self.board[i + 1][j + 1] == \
                                self.board[i + 2][j + 2] == plr:
                            count += 1
                    if j >= 2 and i <= 3:
                        if self.board[i][j] == self.board[i + 1][j - 1] == \
                                self.board[i + 2][j - 2] == plr:
                            count += 1
        return count * 3

    def streaks2(self, plr):
        count = 0
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j]:
                    if j <= 5:
                        if self.board[i][j] == self.board[i][j + 1] == plr:
                            count += 1
                    if i <= 4:
                        if self.board[i][j] == self.board[i + 1][j] == plr:
                            count += 1
                    if j <= 5 and i <= 4:
                        if self.board[i][j] == self.board[i + 1][j + 1] == plr:
                            count += 1
                    if j >= 1 and i <= 4:
                        if self.board[i][j] == self.board[i + 1][j - 1] == plr:
                            count += 1
        return count * 2

    def winner(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j]:
                    if j <= 3:
                        if self.board[i][j] == self.board[i][j + 1] == \
                                self.board[i][j + 2] == self.board[i][j + 3]:
                            return True
                    if i <= 2:
                        if self.board[i][j] == self.board[i + 1][j] == \
                                self.board[i + 2][j] == self.board[i + 3][j]:
                            return True
                    if j <= 3 and i <= 2:
                        if self.board[i][j] == self.board[i + 1][j + 1] == \
                                self.board[i + 2][j + 2] == self.board[i + 3][j + 3]:
                            return True
                    if j >= 3 and i <= 2:
                        if self.board[i][j] == self.board[i + 1][j - 1] == \
                                self.board[i + 2][j - 2] == self.board[i + 3][j - 3]:
                            return True
        return False

from Connect4_AI.Connect4 import *




def main():
    game = Game()





    #num = iter([0,6,3,1,2,3,0,1,5,5,3,1,2,3,4,1])
    col = -1

    while not game.board_full():
        # PLAYER
        game.display()
        while not game.valid_move(col):
            col = int(input(BOLD + "Enter pos: " + END))
            #print(BOLD + "Enter pos: " + END)
            #col = next(num)
        game.player_turn(col)
        # print("Heuristic: ", game.heuristic(game.board, col))
        col = -1
        if game.winner():
            print(BLUE + "Player 1 Wins" + END)
            break



        # AI
        game.display()
        game.ai_turn()
        if game.winner():
            print(RED + "Player 2 Wins" + END)
            break
        # print(game.streaks3(1), game.streaks3(2), game.streaks2(1), game.streaks2(2))

    game.display()


if __name__ == "__main__":
    main()

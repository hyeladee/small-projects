class TicTacToe:
    def __init__(self) -> None:
        self.player1 = ''
        self.player2 = ''
        self.mark1 = ''
        self.mark2 = ''
        self.turn = True
        self.board = [1,2,3,4,5,6,7,8,9]
        self.winner = ''
        self.score = {}
        self.replay = False

    def get_players(self):
        self.player1 = input('Enter name for player one: ')
        self.player1 = self.player1.title()
        self.mark1 = 0
        while True:
            self.mark1 = input(f'{self.player1}, choose your mark (\'X\' or \'O\'): ')
            if self.mark1.lower() == 'x' or self.mark1.lower() == 'o':
                break
            else:
                print('Invalid input! Please choose \'X\' or \'O\': ')
        self.mark1 = self.mark1.upper()
        self.player2 = input('Enter name for player two: ')
        self.player2 = self.player2.title()
        if self.mark1 == 'O':
            self.mark2 = 'X'
        else:
            self.mark2 = 'O'
        print(f'{self.mark2} is assigned to {self.player2}')

    def print_board(self):
        print()
        for i in range(0, 9, 3):
            print(f'{self.board[i]} | {self.board[i+1]} | {self.board[i+2]}')
            if i < 6:
                print('---------')

    def check_win(self):
        #Horizontal Wins        
        for i in range(0, 7, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2]:
                return self.board[i]

        #Vertical Wins
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6]:
                return self.board[i]

        #Diagonal Wins
        if self.board[0] == self.board[4] == self.board[8]:
            return self.board[0]
        if self.board[2] == self.board[4] == self.board[6]:
            return self.board[2]

        return None

    def check_int(self, value):
        try:
            int(value)
            return True
        except:
            return False
    
    def check_bound(self, value):
        if value < 1 or value > 9:
            return False
        else:
            return True
    
    def check_cell(self, value):
        if type(self.board[value - 1]) == int:
            return True
        else:
            return False

    def make_move(self):
        name = ''
        mark = ''
        valid = False

        if self.turn:
            name = self.player1
            mark = self.mark1
        else:
            name = self.player2
            mark = self.mark2
        
        self.print_board()
        move = input(f'Your turn {name}, make a move between 1 and 9: ')
        while not valid:
            if self.check_int(move):
                move = int(move)
                if self.check_bound(move):
                    if self.check_cell(move):
                        self.board[move - 1] = mark
                        valid = True
                    else:
                        self.print_board()
                        move = input('Invalid move. Enter value between 1 and 9: ')
                else:
                    self.print_board()
                    move = input('Invalid move. Enter value between 1 and 9: ')
            else:
                self.print_board()
                move = input('Invalid move. Enter value between 1 and 9: ')

        self.turn = not self.turn

    def game_play(self):
        if self.replay == False:
            print('\nWelcome to the amazing TicTacToe game')
            self.get_players()
            self.score = {self.player1:0, self.player2:0}
            print(f'Starting score {self.score}')
        else:
            print(f'\nWelcome back {self.player1} and {self.player2}.')
            self.board = [1,2,3,4,5,6,7,8,9]

        win = None
        
        for x in range(9):
            self.make_move()
            win = self.check_win()
            if win == self.mark1:
                self.winner = self.player1
                self.score[self.player1] += 1
                break
            elif win == self.mark2:
                self.winner = self.player2
                self.score[self.player2] += 1
                break
        
        if win == None:
            self.print_board()
            print('Out of moves, no winner')
            print(f'Score is {self.score}')
        else:
            self.print_board()
            print(f'{self.winner} has won this round')
            print(f'Score is {self.score}')

        replay = input('do you want to play again ("Y" or "N"): ')

        if replay.lower() == 'y':
            self.replay = True
            self.game_play()

game = TicTacToe()
game.game_play()

print(f'\nThank you {game.player1} and {game.player2} for trying out this game')
print('Hope to see you soon')
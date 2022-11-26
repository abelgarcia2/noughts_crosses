class Player():
    def __init__(self, token, name):
        self.token = token
        self.name = name

class Shift():

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

        self.shift = self.player1
    
    def next_shift(self):
        if self.shift == self.player1:
            self.shift = self.player2
        else:
            self.shift = self.player1
    
    def get_shift(self):
        return f'{self.shift.name} shift'

class Board:

    def __init__(self, rows_columns, player1, player2):
        self.board = list()

        self.rows = rows_columns
        self.columns = rows_columns

        self.player1 = player1
        self.player2 = player2

        self._player1_winner_row = self._create_winner_row(self.player1)
        self._player2_winner_row= self._create_winner_row(self.player2)

        self._initialize_board()

    def _create_winner_row(self, player):
        return [player.token for i in range(self.columns)]

    def _initialize_board(self):
        for i in range(self.rows):
            row = list()
            for z in range(self.columns):
                row.append(None)
            self.board.append(row)

    def is_board_full(self):
        for row in self.board:
            for value in row:
                if value is None:
                    return False
        return True

    def token_move(self, pos_x, pos_y, player):
        self.board[pos_x][pos_y] = player.token

    def getBoard(self):
        for row in self.board:
            print(row)
    
    def there_is_winner(self):
        main_diagonal_row = self._get_main_diagonal()
        secondary_diagonal_row = self._get_secondary_diagonal()

        for index, horizontal_row in enumerate(self.board):

            vertical_row = [row[index] for row in self.board]
            if self._check_row_match(vertical_row):
                return True

            if self._check_row_match(horizontal_row):
                return True

        if self._check_row_match(main_diagonal_row):
            return True

        if self._check_row_match(secondary_diagonal_row):
            return True

        return False

    def _get_main_diagonal(self):
        return [row[index] for index, row in enumerate(self.board)]

    def _get_secondary_diagonal(self):
        reversed_board = reversed(self.board)
        return [row[index] for index, row in enumerate(reversed_board)]

    def _check_row_match(self, row):
        return True if row == self._player1_winner_row or row == self._player2_winner_row else False

class Game():
    def __init__(self, board):
        self.board = board
    
    def game_finished(self):
        return self.board.there_is_winner() or self.board.is_board_full()
    
    

if __name__ == '__main__':
    print('+++++++ NOUGHTS AND CROSSES GAME ++++++\n')

    while True:
        try:
            rows_columns = int(input('Type the board size: '))
            break
        except ValueError:
            print('Type a number!!!!')
    
    token_player1 = input('Type the player1 token: ')
    token_player2 = input('Type the player2 token: ')

    print()

    player1 = Player(token_player1, 'Player 1')
    player2 = Player(token_player2, 'Player 2')

    board = Board(rows_columns, player1, player2)
    game = Game(board)

    shift = Shift(player1, player2)

    while not game.game_finished():
        print(shift.get_shift())


        while True:
            try:
                entrada = input('Type where you want to move the token (x,y): ').split(',')
                board.token_move(int(entrada[0]), int(entrada[1]), shift.shift)
                break
            except ValueError:
                print('Please check your format')

        board.getBoard()

        print()

        shift.next_shift()
from noughts_crosses import Board, Player

player1_4x4 = Player('Y', 'Player 1')
player2_4x4 = Player('Ñ', 'Player 2')

player1_3x3 = Player('0', 'Player 1')
player2_3x3 = Player('X', 'Player 2')

board_4x4 = Board(rows_columns=4, player1=player1_4x4, player2=player2_4x4)
board_3x3 = Board(rows_columns=3, player1=player1_3x3, player2=player2_3x3)

def test_create_winner_row():
    assert board_4x4._create_winner_row(player1_4x4) == ['Y', 'Y', 'Y', 'Y']
    assert board_3x3._create_winner_row(player2_3x3) == ['X', 'X', 'X']

def test_init_board():
    assert board_4x4.columns == 4
    assert board_4x4.rows == 4
    assert board_4x4.player1.token == 'Y'
    assert board_4x4.player2.token == 'Ñ'

    assert board_4x4._player1_winner_row == ['Y', 'Y', 'Y', 'Y']
    assert board_4x4._player2_winner_row == ['Ñ', 'Ñ', 'Ñ', 'Ñ']

    assert board_3x3.columns == 3
    assert board_3x3.rows == 3
    assert board_3x3.player1.token == '0'
    assert board_3x3.player2.token == 'X'

    assert board_3x3._player1_winner_row == ['0', '0', '0']
    assert board_3x3._player2_winner_row == ['X', 'X', 'X']

def test_has_winners():
    # Horizontal row (1)
    board_3x3.board = [
        ['X', 'X','X'],
        ['0', 'X', '0'],
        ['X', 'X', '0']
    ]
    assert board_3x3.there_is_winner() == True

    # Horizontal row (2)
    board_3x3.board = [
        ['X', 'X','0'],
        ['0', '0', '0'],
        ['X', 'X', '0']
    ]
    assert board_3x3.there_is_winner() == True

    # Horizontal row (3)
    board_3x3.board = [
        ['X', '0','X'],
        ['0', '0', 'X'],
        ['X', 'X', 'X']
    ]
    assert board_3x3.there_is_winner() == True

    # Main diagonal
    board_3x3.board = [
        ['X', '0','X'],
        ['X', 'X', '0'],
        ['X', '0', 'X']
    ]
    assert board_3x3.there_is_winner() == True

    # Secondary diagonal
    board_3x3.board = [
        ['X', '0','0'],
        ['0', '0', 'X'],
        ['0', 'X', '0']
    ]
    assert board_3x3.there_is_winner() == True

    # Vertical row (1)
    board_3x3.board = [
        ['X', '0','0'],
        ['X', '0', 'X'],
        ['X', 'X', '0']
    ]
    assert board_3x3.there_is_winner() == True

    # Vertical row (2)
    board_3x3.board = [
        ['X', '0','X'],
        ['X', '0', '0'],
        ['0', '0', 'X']
    ]
    assert board_3x3.there_is_winner() == True

    # Vertical row (3)
    board_3x3.board = [
        ['X', '0','X'],
        ['X', '0', 'X'],
        ['0', 'X', 'X']
    ]
    assert board_3x3.there_is_winner() == True

    # No winner cases
    board_3x3.board = [
        ['X', '0','X'],
        ['X', 'X', '0'],
        ['0', 'X', '0']
    ]
    assert board_3x3.there_is_winner() == False

    board_3x3.board = [
        ['X', '0','X'],
        ['X', '0', 'X'],
        ['0', 'X', '0']
    ]
    assert board_3x3.there_is_winner() == False

    board_3x3.board = [
        ['X', '0','X'],
        ['X', 'X', '0'],
        ['0', 'X', '0']
    ]
    assert board_3x3.there_is_winner() == False
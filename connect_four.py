player_1 = True

if player_1:
    first_symbol = 'O'
    second_symbol = 'X'
    turn_index = 0
else:
    first_symbol = 'X'
    second_symbol = 'O'
    turn_index = 1


def wins(board, player):

    """Return True if the input player has four in a row"""

    # Row wins
    for i in range(6):
        for r in range(4):
            if (board[7 * i + r] == player and board[7 * i + 1 + r] == player and
                board[7 * i + 2 + r] == player) and board[7 * i + 3 + r] == player :
                return True

    # Column wins
    for i in range(7):
        for r in range(3):
            if (board[i + (r*7)] == player and board[i + 7 + (r*7)] == player and
                board[i + 14 + (r*7)] == player and board[i + 21 + (r*7)] == player):
                return True

    #Diagonal wins
    for r in range(3):
        for i in range(4):
            if (board[i + (r*7)] == player and board[i+8 + (r*7)] == player and board[i+16 + (r*7)] == player
            and board[i+24 + (r*7)] == player):
                return True

    for r in range(3):
        for i in range(3,7):
            if (board[i + (r*7)] == player and board[i+6 + (r*7)] == player and board[i+12 + (r*7)] == player
            and board[i+18 + (r*7)] == player):
                return True

    # No win
    return False

def score(board):
    """Score a given board from the computer's perspective.

       Computer wins score 1 (best outcome for the computer)
       Human wins score -1 (worst outcome for the computer)
       Ties and incomplete games are 0
    """

    if wins(board, second_symbol):
        return 1
    elif wins(board, first_symbol):
        return -1
    else:
        return 0



def minimax(board, depth, alpha, beta, is_max_player):

    """Execute the minimax algorithm by exploring the subtree, identifying the
       move at each level that yields the best outcome for its player

       Returns:
           the best score that the player can obtain in this subtree
           the move yielding that best score
    """

    # Base conditions: return a score
    current_score = score(board)
    if current_score != 0 or depth == 0:
        return current_score, None

    if is_max_player:
        best_value = -40
        best_move = None

        for move in range(6):
            if board[move] != None:
                continue
            else:
                for v in range(5):
                    if board[move]== None and board[move + 7] == None:
                        move = move + 7

            board[move] = second_symbol

            value, response = minimax(board, depth - 1, alpha, beta, False)

            board[move] = None  # Reset the board

            alpha = max(alpha, value)

            if value > best_value:
                best_value = value
                best_move = move

            if beta <= alpha:
                break

    if not is_max_player:
        best_value = 40
        best_move = None

        for move in range(6):
            if board[move] != None:
                continue
            else:
                for v in range(5):
                    if board[move]== None and board[move + 7] == None:
                        move = move + 7

            board[move] = first_symbol
            value, response = minimax(board, depth - 1, alpha, beta, True)
            board[move] = None

            beta = min(beta, value)

            if value < best_value:
                best_value = value
                best_move = move

            if beta <= alpha:
                break

    return best_value, best_move


def display(board):
    print ''

    for i in range(42):
        if board[i] is None:
            print '.  ',
        else:
            print board[i], ' ',

        if i == 6 or i == 13 or i == 20 or i == 27 or i == 34 or i == 41:
            print ''

    print ''


def get_move(board):
    looping = True;

    while looping:
        looping = False

        print 'Enter a column, 0-6: ',
        move = int(raw_input())

        if (board[move] != None) or move < 0 or move > 6:
            print 'Choose a different column.'
            looping = True

        else:
            for v in range(5):
                if board[move + 7] == None:
                    move = move + 7


    return move


def play():
    board = {0: None, 1: None, 2: None, 3: None, 4: None, 5: None, 6: None,
             7: None, 8: None, 9: None, 10: None, 11: None, 12: None, 13: None,
             14: None, 15: None, 16: None, 17: None, 18: None, 19: None, 20: None,
             21: None, 22: None, 23: None, 24: None, 25: None, 26: None, 27: None,
             28: None, 29: None, 30: None, 31: None, 32: None, 33: None, 34: None,
             35: None, 36: None, 37: None, 38: None, 39: None, 40: None, 41: None,}

    for i in range(7):
        print('0   1   2   3   4   5   6')

    turn = 0

    while turn < 42:

        # Human turn
        if turn % 2 == turn_index:
            move = get_move(board)
            board[move] = first_symbol

        # second player turn
        else:
            #best_move = get_move(board)
            best_value, best_move = minimax(board, 12, -40, 40, True)
            print "computer played: "
            print best_move

            if board[best_move] == None:
                board[best_move] = second_symbol

        display(board)

        # Check for wins
        if wins(board, first_symbol):
            print 'Man triumphs over machine!'
            turn = 41
        elif wins(board, second_symbol):
            print 'A dark day for humanity...'
            turn = 41

        turn += 1

    if turn == 41:
        print 'The only winning move is not to play.'

if __name__ == '__main__':
    play()

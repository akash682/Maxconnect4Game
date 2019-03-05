from MaxConnect4Game import *
import copy


class Minimax:
    def __init__(self, game, init_next, depth):
        self.currentTurn = game.currentTurn
        self.game = game
        self.maxdepth = int(depth)
        self.init_next = init_next

    def maximizer(self, state, alpha, beta):
        if state.pieceCount == 42 or state.NODEDEPTH == self.maxdepth:
            return self.utility(state)
        v = -9999999

        for poss_column in branch_state(state.gameBoard):
            # Create maxConnect4Game class object
            next_state = create_state(state, poss_column)

            v = max(v, self.minimizer(next_state, alpha, beta))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v

    def minimizer(self, state, alpha, beta):
        if state.pieceCount == 42 or state.NODEDEPTH == self.maxdepth:
            return self.utility(state)
        v = 9999999

        for poss_column in branch_state(state.gameBoard):
            # Create maxConnect4Game class object
            next_state = create_state(state, poss_column)

            v = min(v, self.maximizer(next_state, alpha, beta))
            if v <= alpha:
                return v
            beta = min(beta,v)
        return v

    def utility(self, state):
        if self.init_next == 'computer-next' and state.currentTurn == 1 and self.game.init_turn == 1:
            utility = 2 * state.player1Score - state.player2Score

        elif self.init_next == 'computer-next' and state.currentTurn == 1 and self.game.init_turn == 2:
            utility = 2 * state.player1Score - state.player2Score

        elif self.init_next == 'computer-next' and state.currentTurn == 2 and self.game.init_turn == 1:
            utility = 2 * state.player2Score - state.player1Score

        elif self.init_next == 'computer-next' and state.currentTurn == 2 and self.game.init_turn == 2:
            utility = 2 * state.player2Score - state.player1Score

        elif self.init_next == 'human-next' and state.currentTurn == 1 and self.game.init_turn == 1:
            utility = 2 * state.player1Score - state.player2Score

        elif self.init_next == 'human-next' and state.currentTurn == 1 and self.game.init_turn == 2:
            utility = 2 * state.player1Score - state.player2Score

        elif self.init_next == 'human-next' and state.currentTurn == 2 and self.game.init_turn == 1:
            utility = 2 * state.player2Score - state.player1Score

        elif self.init_next == 'human-next' and state.currentTurn == 2 and self.game.init_turn == 2:
            utility = 2 * state.player2Score - state.player1Score

        return utility

    def final_decision(self):
        # Utility values of the min branch
        minValues = []
        poss_moves = branch_state(self.game.gameBoard)

        for poss_column in poss_moves:
            # Create maxConnect4Game class object
            next_state = create_state(self.game, poss_column)

            # Append utility value of the minimizer
            minValues.append(self.minimizer(next_state, 9999999, -9999999))

        # Get index
        index_move = minValues.index(max(minValues))

        # Get finally decieded column
        final_move = branch_state(self.game.gameBoard)[index_move]

        return final_move

def branch_state(gameboard):
    branch_state = []
    # Check the column of the first row
    for column, column_value in enumerate(gameboard[0]):
        # If there is no piece then append the column number to brance_state
        if column_value ==0:
            branch_state.append((column))
    return branch_state

def create_state(current_state, column):
    next_state = maxConnect4Game()

    try:
        next_state.NODEDEPTH = current_state.NODEDEPTH +1
    except AttributeError:
        next_state.NODEDEPTH = 1

    next_state.pieceCount = current_state.pieceCount
    next_state.gameBoard = copy.deepcopy(current_state.gameBoard)

    if not next_state.gameBoard[0][column]:
        for i in range(5, -1, -1):
            if not next_state.gameBoard[i][column]:
                next_state.gameBoard[i][column] = current_state.currentTurn
                next_state.pieceCount += 1
                break

    if current_state.currentTurn == 1:
        next_state.currentTurn = 2
    elif current_state.currentTurn == 2:
        next_state.currentTurn = 1

    next_state.checkPieceCount()
    next_state.countScore()

    return next_state








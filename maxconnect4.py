#!/usr/bin/env python

# Written by Chris Conly based on C++
# code provided by Dr. Vassilis Athitsos
# Written to be Python 2.4 compatible for omega

import sys
from MaxConnect4Game import *
from Minimax import *
import sys

def oneMoveGame(currentGame, fname, depth):
    # Is the board full already?
    if currentGame.pieceCount == 42:
        print 'BOARD FULL\n\nGame Over!\n'
        sys.exit(0)

    # Make a move (Minimax algorithm implemented)
    aiPlay(currentGame, 'computer-next', depth)


    fname = fname;

    try:
        # open human.txt with write mode
        currentGame.gameFile = open(fname, 'w')
    except:
        sys.exit('Error opening output file, computer.txt')

    #SavetoFile
    currentGame.printGameBoardToFile()
    currentGame.gameFile.close()

def interactiveGame(currentGame, init_next, depth):
    print('Interactive mode selected.')

    while currentGame.pieceCount !=42:
        if init_next == 'computer-next' and currentGame.currentTurn == 1 and currentGame.init_turn == 1:
            # --COMPUTER PROCESS--
            aiPlay(currentGame, init_next, depth)

        if init_next == 'computer-next' and currentGame.currentTurn == 1 and currentGame.init_turn == 2:
            # --HUMAN INTERFACE-
            humaninterface(currentGame)

        elif init_next == 'computer-next' and currentGame.currentTurn == 2 and currentGame.init_turn ==1:
            # --HUMAN INTERFACE-
            humaninterface(currentGame)

        elif init_next == 'computer-next' and currentGame.currentTurn == 2 and currentGame.init_turn == 2:
            # --COMPUTER PROCESS--
            aiPlay(currentGame, init_next, depth)

        elif init_next == 'human-next' and currentGame.currentTurn == 1 and currentGame.init_turn == 1:
            # --HUMAN INTERFACE-
            humaninterface(currentGame)

        elif init_next == 'human-next' and currentGame.currentTurn == 1 and currentGame.init_turn == 2:
            # --COMPUTER PROCESS--
            aiPlay(currentGame, init_next, depth)

        elif init_next == 'human-next' and currentGame.currentTurn == 2 and currentGame.init_turn == 1:
            # --COMPUTER PROCESS--
            aiPlay(currentGame, init_next, depth)

        elif init_next == 'human-next' and currentGame.currentTurn == 2 and currentGame.init_turn == 2:
            # --HUMAN INTERFACE-
            humaninterface(currentGame)

    # -----------------------------------RESULT------------------------------------------------------------
    if currentGame.player1Score > currentGame.player2Score:
        if currentGame.init_turn == 1 and sys.argv[3] == 'computer-next':
            print('Computer won')
        else:
            print('You won')
        if currentGame.init_turn == 1 and sys.argv[3] == 'human-next':
            print('You won')
        else:
            print('Computer won.')
    elif currentGame.player1Score < currentGame.player2Score:
        if currentGame.init_turn == 1 and sys.argv[3] == 'computer-next':
            print('You won.')
        else:
            print('Computer won')

        if currentGame.init_turn == 1 and sys.argv[3] == 'human-next':
            print('Computer won')
        else:
            print('You won.')
    else:
        print('Draw game.')
    print('Thank you for playing MaxConnect4Game')


#----HUMAN INTERFACE-----
def humaninterface(currentGame):
    print('---------------HUMAN TURN------------------')
    while True:
        # column input
        user_move = input('Choose the column number between [1-7].')

        # column input check
        if not 1 <= user_move <= 7:
            print('Invalid number.')
            continue
        elif currentGame.gameBoard[0][user_move - 1] != 0:
            print('This column is already filled up.')
            continue
        else:
            break

    # Play with requested column
    currentGame.playPiece(user_move - 1)
    print 'Game state after move:'

    # Print GameBoard
    currentGame.printGameBoard()

    # Print Score
    currentGame.countScore()
    print('Score: Player 1 = %d, Player 2 = %d' % (currentGame.player1Score, currentGame.player2Score))

    try:
        # open human.txt with write mode
        currentGame.gameFile = open("human.txt", 'w')
    except:
        sys.exit('Error opening output file, human.txt')

    # write currentGameBoard to human.txt
    currentGame.printGameBoardToFile()

#----COMPUTER PROCESS-----
#AI section. Creates Minimax object and starts method.
def aiPlay(currentGame, init_next, depth):
    print ('---------------COMPUTER TURN---------------')
    #Minimax object
    miniobj = Minimax(currentGame, init_next, depth)

    #Result of next move(column) using minimax algorithm
    dec_col = miniobj.final_decision()

    #Play with result column
    currentGame.playPiece(dec_col)
    print('move %d: Player %d, column %d' % (currentGame.pieceCount, currentGame.currentTurn, dec_col + 1))

    # Print GameBoard
    print 'Game state after move:'
    currentGame.printGameBoard()

    # Print Score
    currentGame.countScore()
    print('Score: Player 1 = %d, Player 2 = %d' % (currentGame.player1Score, currentGame.player2Score))

    try:
        # open computer.txt with write mode
        currentGame.gameFile = open("computer.txt", 'w')
    except:
        sys.exit('Error opening output file, computer.txt')

    # write currentGameBoard to computer.txt
    currentGame.printGameBoardToFile()

    # human.txt computer.txt close
    currentGame.gameFile.close()

def main(argv):
    # Make sure we have enough command-line arguments
    if len(argv) != 5:
        print 'Four command-line arguments are needed:'
        print('Usage: %s interactive [input_file] [computer-next/human-next] [depth]' % argv[0])
        print('or: %s one-move [input_file] [output_file] [depth]' % argv[0])
        sys.exit(2)

    game_mode, inFile = argv[1:3]

    if not game_mode == 'interactive' and not game_mode == 'one-move':
        print('%s is an unrecognized game mode' % game_mode)
        sys.exit(2)

    currentGame = maxConnect4Game() # Create a game

    # Try to open the input file
    try:
        currentGame.gameFile = open(inFile, 'r')
    except IOError:
        sys.exit("\nError opening input file.\nCheck file name.\n")

    # Read the initial game state from the file and save in a 2D list
    file_lines = currentGame.gameFile.readlines()
    currentGame.gameBoard = [[int(char) for char in line[0:7]] for line in file_lines[0:-1]]
    currentGame.currentTurn = int(file_lines[-1][0])
    currentGame.init_turn = currentGame.currentTurn
    currentGame.gameFile.close()

    print '\nMaxConnect-4 game\n'
    print 'Game state before move:'
    currentGame.printGameBoard()

    # Update a few game variables based on initial state and print the score
    currentGame.checkPieceCount()
    currentGame.countScore()
    print('Score: Player 1 = %d, Player 2 = %d' % (currentGame.player1Score, currentGame.player2Score))

    if game_mode == 'interactive':
        interactiveGame(currentGame, argv[3], argv[4]) # Be sure to pass whatever else you need from the command line
    else: # game_mode == 'one-move'
        # Set up the output file
        outFile = argv[3]
        try:
            currentGame.gameFile = open(outFile, 'w')
        except:
            sys.exit('Error opening output file.')
        oneMoveGame(currentGame,argv[3], argv[4]) # Be sure to pass any other arguments from the command line you might need.

if __name__ == '__main__':
    main(sys.argv)
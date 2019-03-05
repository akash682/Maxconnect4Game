# Maxconnect4Game_GamePlaying
This software implements maxconnect4game. Computer decides its next move by using Minimax algorithm.

Created by: Akash Lohani 1001661458
Programming language: Python2.7

How the code is tructured:

*Abstract
	This software implements maxconnect4game.Computer decides its next move by using Minimax algorithm.
	Details for how to play the game are stated in the link below.
	https://omega.uta.edu/~gopikrishnav/classes/2019/spring/4308_5360/assmts/assmt4.html
	

*Argument/Game mode
	Argument to run the program takes as follows.

	Interactive mode:
	python maxconnect.py interactive [input_file] [computer-next/human-next] [depth]
	i.e. python maxconnect.py interactive input1.txt computer-next 20
	
	--components--
	interactive:			specifies that the program runs in interactive mode.
	[input_file]:			specifies an input file that contains an initial board state. 
					This way we can start the program from a non-empty board state.
					If the input file does not exist, the program should just create an empty board state and start again from there.
	[computer-first/human-first]: 	specifies whether the computer should make the next move or the human.
	[depth]:			specifies the number of moves in advance that the computer should consider while searching for its next move.
					In other words, this argument specifies the depth of the search tree.
					Essentially, this argument will control the time takes for the computer to make a move. 
	
	One-move mode:
	python maxconnect.py one-move [input_file] [output_file] [depth]
	i.e. python maxconnect.py one-move input1.txt output1.txt 20

	--components--
	one-move:			specifies that the program runs in one-move mode.
	[input_file]:			specifies an input file that contains an initial board state. 
					This way we can start the program from a non-empty board state.
					If the input file does not exist, the program should just create an empty board state and start again from there.
	[output_file]:		 	specifies an output file for writeing the result after move.
	[depth]:			specifies the number of moves in advance that the computer should consider while searching for its next move.
					In other words, this argument specifies the depth of the search tree.
					Essentially, this argument will control the time takes for the computer to make a move. 

*Computation vs depth
Computation time is proportional to minimax depth. 
However computation time relatively stays constant after reaching the maximum depth limit 42.
Please check the [Minimax depth vs Computation time.docx] file for more detail.

***Result***
[1]python maxconnect.py interactive input2.txt computer-next 20

MaxConnect-4 game

Game state before move:
 -----------------
 | 0 0 0 0 0 0 0 | 
 | 0 0 0 0 0 0 0 | 
 | 0 2 0 0 0 0 0 | 
 | 0 1 0 0 0 0 2 | 
 | 0 2 0 0 1 1 1 | 
 | 1 1 0 0 2 2 2 | 
 -----------------
Score: Player 1 = 0, Player 2 = 0
Interactive mode selected.
---------------COMPUTER TURN---------------
move 13: Player 2, column 5
Game state after move:
 -----------------
 | 0 0 0 0 0 0 0 | 
 | 0 0 0 0 0 0 0 | 
 | 0 2 0 0 0 0 0 | 
 | 0 1 0 0 1 0 2 | 
 | 0 2 0 0 1 1 1 | 
 | 1 1 0 0 2 2 2 | 
 -----------------
Score: Player 1 = 0, Player 2 = 0
---------------HUMAN TURN------------------
Choose the column number between [1-7].2
Game state after move:
 -----------------
 | 0 0 0 0 0 0 0 | 
 | 0 2 0 0 0 0 0 | 
 | 0 2 0 0 0 0 0 | 
 | 0 1 0 0 1 0 2 | 
 | 0 2 0 0 1 1 1 | 
 | 1 1 0 0 2 2 2 | 
 -----------------
Score: Player 1 = 0, Player 2 = 0
---------------COMPUTER TURN---------------
move 15: Player 2, column 1
Game state after move:
 -----------------
 | 0 0 0 0 0 0 0 | 
 | 0 2 0 0 0 0 0 | 
 | 0 2 0 0 0 0 0 | 
 | 0 1 0 0 1 0 2 | 
 | 1 2 0 0 1 1 1 | 
 | 1 1 0 0 2 2 2 | 
 -----------------
Score: Player 1 = 0, Player 2 = 0
---------------HUMAN TURN------------------
Choose the column number between [1-7].
....


[2]python maxconnect.py one-move input1.txt output1.txt 20

MaxConnect-4 game

Game state before move:
 -----------------
 | 0 0 0 0 0 0 0 | 
 | 0 0 0 0 0 0 0 | 
 | 0 0 0 0 0 0 0 | 
 | 0 0 0 0 0 0 0 | 
 | 0 0 0 0 0 0 0 | 
 | 0 0 0 0 0 0 0 | 
 -----------------
Score: Player 1 = 0, Player 2 = 0
---------------COMPUTER TURN---------------
move 1: Player 2, column 1
Game state after move:
 -----------------
 | 0 0 0 0 0 0 0 | 
 | 0 0 0 0 0 0 0 | 
 | 0 0 0 0 0 0 0 | 
 | 0 0 0 0 0 0 0 | 
 | 0 0 0 0 0 0 0 | 
 | 1 0 0 0 0 0 0 | 
 -----------------
Score: Player 1 = 0, Player 2 = 0

Process finished with exit code 0
 

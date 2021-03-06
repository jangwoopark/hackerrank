Bidding Tic-Tac-Toe is a modified version of the regular Tic-Tac-Toe where players bid to make their move on the board. Each player is given 4 bidding chips to start with. Both players make a secret bid. The player who has a higher bid gets to make the move on the board. The loser then collects the winning bid.

The first player starts with the draw advantage and it alternates henceforth. The first player is represented by X (ascii value:88) and the second player by O (ascii value:79) respectively. An unoccupied cell is represented by _ (ascii value:95).

The player who succeeds in placing 3 respective marks horizontally, vertically or diagonally wins the game. A minimum of one bidding chip must be used at every bid and you can bid zero only when there are no chips left with the player.

Complete the functions next_move to bid or play your next move depending on whether the move is to BID or to PLAY on the board respectively.

Input Format

The first line of the input represents the player who is supposed to play (X or O)
The second line indicates whether the player bids or the player has to make a move on the Tic-Tac-Toe board. BID indicates that its a bid and PLAY indicates that its a move.
The third and the fourth line contains space separated integers which are all the previous bids made by player X and player O respectively.
Next three lines shows the current Tic-Tac-Toe board.

Output Format

If the move is a BID print a single integer which is the number of chips you are willing to bid to make a move.
If the move is PLAY print 2 single spaced integers which is the position of an empty slot you want to mark.

Sample Input

X
BID
1 2
2 1
__O
_X_
___
Sample Output

4

The first line of input says that its the 1st player's move. 2nd line says that he has to bid. 3rd line indicates that first bid resulted in O as the winner. X gets 2 bidding chips from the winning bidder O and in return O gets to make a move on the Tic-Tac-Toe board. X has 6 chips and O has only 2. O makes a move at (0,2). The next bid X wins the bid and the bidding chips of X goes to O. Xs chips reduces back to 4 and Os chips are now 4. X makes a move on the board at position (1,1). Now Xs turn, X makes a bid of 4.

GamePlay

X goes first and O goes second. The third move on the board is made by the winning bidder who can be either X or O. The game ends when one of the end configurations of Tic-Tac-Toe is reached.

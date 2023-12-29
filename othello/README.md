# Assignment 3

## Goals
The goals of this assignment are:
- Understanding adversarial search
- Implementing minimax and alpha-beta pruning

## Background
Othello, also known by its non-trademark name _reversi_, is a strategy game for two players. You can find the [rules for the game on wikipedia](https://en.wikipedia.org/wiki/Reversi). There are also numerous sites to play online, and many free versions that you can download and play on your own computer.

We will be playing a variation of the game. At the game's start, we will choose a random square in the top row and a random square in the bottom row and block those out as unplayable locations.
I (Prof Andrew Exley) have written a working version in python3 Download written a working version in python3 (The skeleton file if required, can be downloaded from [here](https://github.com/hardikkgupta/csci5511/blob/main/othello/randothellogame_skeleton.py). If you want to use a different language, that's fine, feel free to adapt my classes and methods. The game rules themselves are a little tricky to implement, and I don't want you to spend too much time debugging those.

You can run the game as-is by running **python3 randothellogame_skeleton.py** on your command line. It will begin a game with two human players, who must take their moves by typing into the terminal.

## Tasks
### RandomPlayer
To help you understand the structure of the code, start by building a RandomPlayer class that will choose a random move from among all legal moves on its turn. Take a look at my OthelloPlayerTemplate class for guidance. This player will also come in handy when you design your "smarter" agents. If you can't beat random.... then you know something is not right.

### Utility Function
Step one in building a **good** agent to play a game is to create a utility function. I have left that out of the code, and it is up to you to decide what a good utility is for this game. A very basic utility function might count the number of pieces you have and subtract the number of pieces the opponent has. This way, the more pieces you have on the board, the higher the utility. Additionally, you would want the utility function to report a terminal state with a win as a very high number utility and a terminal state with a loss as a very low number utility.

You will almost certainly want to redesign your utility function once you understand more about the game, so I recommend starting with something simple then coming back to it later.

### Minimax Agent
Now that you have those pieces, create a **MinimaxPlayer** class that implements the minimax search algorithm to decide its moves. Have the depth limit of your MinimaxPlayer class be set as a parameter when the object is created. If you follow the python template, we should be able to create a player with the code
```
p1 = MinimaxPlayer(WHITE, 4)
```
that plays as white and has a search depth limit of 4 plies.

### Alpha-Beta Agent
Finally, create an **AlphabetaPlayer** class that implements minimax search with alpha-beta pruning to decide its moves. Again, have the depth limit be set as a parameter when an object is created. It is possible that the only difference between results of Alpha-beta and Minimax will be the difference in time to arrive at a solution, but that means that it should be reasonable to run alpha-beta with a larger depth limit.

## Output and Submission
Set up your code so that by default it plays your AlphabetaPlayer (with a reasonable depth limit that doesn't take too long) against RandomPlayer, then swaps colors and does it again.

## How to Run
### Sample Input
```
python3 randothello.py
```
### Sample Output
```
AlphaBeta is Black and RandomPlayer is White
Legal moves are [(2, 3), (3, 2), (4, 5), (5, 4)]
White Action,  (2, 3)
Legal moves are [(2, 2), (2, 4), (4, 2)]
Black Action,  (2, 2)
Legal moves are [(2, 1), (3, 2), (4, 5), (5, 4)]
White Action,  (2, 1)
Legal moves are [(1, 1), (1, 3), (2, 4), (3, 5), (4, 2), (5, 3)]
Black Action,  (4, 2)
Legal moves are [(3, 2), (5, 2), (5, 3), (5, 4), (5, 5)]
White Action,  (5, 4)
Legal moves are [(1, 1), (1, 3), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5)]
Black Action,  (5, 5)
Legal moves are [(3, 2), (5, 2), (5, 3), (5, 6), (6, 6)]
White Action,  (6, 6)
Legal moves are [(1, 3), (2, 4), (2, 5), (4, 5), (6, 5)]
Black Action,  (1, 3)
Legal moves are [(0, 4), (1, 2), (2, 4), (3, 2), (4, 1), (5, 2)]
White Action,  (0, 4)
Legal moves are [(0, 3), (1, 1), (2, 0), (2, 5), (3, 5), (4, 5), (6, 5), (7, 7)]
Black Action,  (0, 3)
Legal moves are [(0, 2), (1, 2), (2, 4), (3, 2), (4, 1), (5, 2)]
White Action,  (0, 2)
Legal moves are [(1, 1), (2, 0), (2, 5), (3, 1), (3, 5), (4, 5), (6, 5), (7, 7)]
Black Action,  (2, 5)
Legal moves are [(2, 4), (3, 2), (4, 1), (5, 3)]
White Action,  (5, 3)
Legal moves are [(1, 2), (2, 4), (3, 2), (4, 5), (5, 2), (6, 4)]
Black Action,  (1, 2)
Legal moves are [(1, 1), (1, 6), (2, 4), (3, 1), (3, 5), (4, 1), (5, 1)]
White Action,  (4, 1)
Legal moves are [(1, 4), (2, 0), (3, 0), (3, 2), (5, 2), (6, 3), (6, 4)]
Black Action,  (3, 0)
Legal moves are [(1, 1), (1, 6), (2, 0), (2, 4), (3, 5)]
White Action,  (2, 4)
Legal moves are [(1, 4), (3, 2), (4, 5), (5, 2)]
Black Action,  (4, 5)
Legal moves are [(1, 1), (1, 6), (2, 0), (2, 6), (3, 5), (3, 6), (4, 6)]
White Action,  (3, 6)
Legal moves are [(1, 4), (3, 2), (4, 7), (5, 2), (5, 6), (6, 3), (6, 4)]
Black Action,  (6, 3)
Legal moves are [(0, 1), (1, 1), (1, 4), (2, 0), (2, 6), (3, 2), (5, 2), (6, 2), (6, 4), (7, 2), (7, 3)]
White Action,  (7, 3)
Legal moves are [(1, 4), (3, 2), (4, 7), (5, 2), (5, 6), (6, 4)]
Black Action,  (6, 4)
Legal moves are [(0, 1), (1, 1), (1, 4), (1, 6), (2, 0), (2, 6), (3, 5), (6, 5), (7, 4), (7, 5)]
White Action,  (3, 5)
Legal moves are [(1, 4), (2, 7), (3, 1), (3, 2), (4, 6), (4, 7), (5, 2), (5, 6), (6, 2), (6, 5), (7, 2)]
Black Action,  (5, 2)
Legal moves are [(0, 1), (1, 1), (1, 4), (1, 5), (2, 0), (2, 6), (4, 0), (5, 1), (6, 2), (6, 5), (7, 4), (7, 5)]
White Action,  (0, 1)
Legal moves are [(1, 4), (2, 6), (2, 7), (3, 1), (3, 2), (4, 6), (4, 7), (5, 6), (6, 2), (6, 5), (7, 2), (7, 4)]
Black Action,  (7, 2)
Legal moves are [(1, 4), (1, 5), (2, 0), (2, 6), (4, 0), (5, 1), (6, 2), (7, 1), (7, 4), (7, 5)]
White Action,  (5, 1)
Legal moves are [(1, 4), (2, 7), (3, 1), (3, 2), (4, 6), (4, 7), (5, 6), (6, 1), (6, 5), (7, 4)]
Black Action,  (7, 4)
Legal moves are [(1, 4), (1, 5), (1, 6), (2, 0), (2, 6), (3, 1), (3, 2), (4, 0), (7, 5)]
White Action,  (1, 5)
Legal moves are [(1, 4), (1, 6), (2, 6), (2, 7), (3, 1), (3, 2), (4, 6), (5, 6), (6, 1), (6, 5)]
Black Action,  (3, 1)
Legal moves are [(1, 1), (2, 0), (3, 2), (4, 0), (6, 2)]
White Action,  (1, 1)
Legal moves are [(0, 6), (1, 4), (1, 6), (2, 0), (2, 6), (2, 7), (3, 2), (4, 0), (4, 6), (5, 0), (5, 6), (6, 0), (6, 1), (6, 2), (6, 5)]
Black Action,  (6, 0)
Legal moves are [(3, 2), (5, 0), (6, 1), (6, 2), (7, 5)]
White Action,  (7, 5)
Legal moves are [(0, 6), (1, 4), (1, 6), (2, 7), (3, 2), (4, 0), (4, 6), (5, 6), (6, 1), (6, 5), (7, 6)]
Black Action,  (1, 4)
Legal moves are [(0, 5), (3, 2), (5, 0), (6, 1), (6, 2), (7, 1)]
White Action,  (3, 2)
Legal moves are [(0, 6), (1, 0), (1, 6), (2, 0), (2, 6), (2, 7), (4, 6), (4, 7), (5, 0), (5, 6), (6, 1), (6, 5), (7, 6)]
Black Action,  (1, 0)
Legal moves are [(0, 5), (2, 0), (5, 0), (6, 1), (6, 2), (7, 1)]
White Action,  (7, 1)
Legal moves are [(0, 6), (1, 6), (2, 0), (2, 6), (2, 7), (4, 0), (4, 6), (4, 7), (5, 0), (5, 6), (6, 1), (6, 2), (6, 5), (7, 7)]
Black Action,  (4, 6)
Legal moves are [(0, 5), (2, 0), (2, 6), (4, 7), (5, 0), (5, 6), (5, 7), (6, 1), (6, 2)]
White Action,  (2, 0)
Legal moves are [(0, 5), (0, 6), (1, 6), (2, 6), (2, 7), (4, 0), (4, 7), (5, 0), (5, 6), (6, 1), (6, 2), (6, 5)]
Black Action,  (5, 6)
Legal moves are [(0, 5), (2, 6), (4, 0), (4, 7), (5, 7), (6, 1), (6, 2), (6, 5), (6, 7)]
White Action,  (4, 7)
Legal moves are [(0, 5), (0, 6), (1, 6), (2, 6), (2, 7), (4, 0), (5, 0), (5, 7), (6, 5), (7, 6), (7, 7)]
Black Action,  (1, 6)
Legal moves are [(0, 5), (0, 6), (0, 7), (1, 7), (2, 6), (4, 0), (6, 1), (6, 2), (6, 5), (6, 7)]
White Action,  (0, 7)
Legal moves are [(1, 7), (2, 6), (2, 7), (4, 0), (5, 0), (5, 7), (6, 5), (7, 6), (7, 7)]
Black Action,  (5, 7)
Legal moves are [(0, 5), (0, 6), (2, 6), (4, 0), (6, 1), (6, 2), (6, 5), (6, 7)]
White Action,  (6, 1)
Legal moves are [(1, 7), (2, 6), (2, 7), (4, 0), (5, 0), (6, 2), (6, 5), (7, 6), (7, 7)]
Black Action,  (5, 0)
Legal moves are [(0, 5), (0, 6), (2, 6), (4, 0), (6, 2), (6, 5), (6, 7)]
White Action,  (6, 2)
Legal moves are [(1, 7), (2, 6), (2, 7), (4, 0), (6, 5), (7, 6), (7, 7)]
Black Action,  (1, 7)
Legal moves are [(0, 5), (0, 6), (2, 6), (2, 7), (4, 0), (6, 5), (6, 7)]
White Action,  (4, 0)
Legal moves are [(2, 6), (2, 7), (6, 5), (7, 0), (7, 6), (7, 7)]
Black Action,  (2, 7)
Legal moves are [(0, 5), (0, 6), (2, 6), (6, 5), (6, 7), (7, 0)]
White Action,  (7, 0)
Legal moves are [(2, 6), (7, 6), (7, 7)]
Black Action,  (2, 6)
Legal moves are [(0, 5), (0, 6), (6, 5), (6, 7)]
White Action,  (0, 5)
Legal moves are [(7, 6), (7, 7)]
Black Action,  (7, 7)
Legal moves are [(0, 6), (6, 5), (6, 7)]
White Action,  (0, 6)
Legal moves are ['SKIP']
Black Action,  SKIP
Legal moves are [(6, 5), (6, 7), (7, 6)]
White Action,  (6, 7)
Legal moves are ['SKIP']
Black Action,  SKIP
Legal moves are [(6, 5), (7, 6)]
White Action,  (6, 5)
Legal moves are [(7, 6)]
Black Action,  (7, 6)
Game Over
  01234567
0 XWBBBBBB
1 BBWBBBBB
2 BWBWBBBB
3 BWBBWBBB
4 BBBBBWBB
5 BBWWBBWB
6 BWWWWWWW
7 BWWXBBBW
Black: 42
White: 20
Black wins
AlphaBeta is White and RandomPlayer is Black
Legal moves are [(2, 3), (3, 2), (4, 5), (5, 4)]
White Action,  (4, 5)
Legal moves are [(3, 5), (5, 3), (5, 5)]
Black Action,  (3, 5)
Legal moves are [(2, 2), (2, 3), (2, 4), (2, 5), (2, 6)]
White Action,  (2, 2)
Legal moves are [(3, 2), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6)]
Black Action,  (3, 2)
Legal moves are [(2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (4, 2)]
White Action,  (2, 1)
Legal moves are [(1, 1), (3, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6)]
Black Action,  (1, 1)
Legal moves are [(0, 0), (0, 1), (1, 2), (2, 3), (2, 4), (2, 5), (2, 6), (3, 6)]
White Action,  (0, 1)
Legal moves are [(0, 0), (2, 0), (3, 1), (4, 2), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6)]
Black Action,  (0, 0)
Legal moves are [(1, 2), (2, 3), (2, 4), (2, 5), (2, 6), (3, 6)]
White Action,  (2, 3)
Legal moves are [(0, 2), (3, 1), (5, 3), (5, 5)]
Black Action,  (0, 2)
Legal moves are [(2, 5), (2, 6), (3, 6)]
White Action,  (3, 6)
Legal moves are [(3, 1), (5, 5)]
Black Action,  (3, 1)
Legal moves are [(1, 0), (2, 0), (3, 0), (4, 0)]
White Action,  (4, 0)
Legal moves are [(2, 4), (4, 1), (5, 4), (5, 5)]
Black Action,  (2, 4)
Legal moves are [(1, 0), (1, 2), (1, 3), (1, 4), (1, 5)]
White Action,  (1, 4)
Legal moves are [(2, 5), (4, 1), (4, 2), (5, 4), (5, 5)]
Black Action,  (2, 5)
Legal moves are [(1, 0), (1, 2), (1, 3), (1, 5), (1, 6)]
White Action,  (1, 0)
Legal moves are [(0, 3), (0, 4), (0, 5), (2, 0), (4, 1), (4, 2), (4, 6), (4, 7), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6)]
Black Action,  (0, 3)
Legal moves are [(0, 4), (0, 5), (1, 2), (1, 3), (1, 5), (1, 6), (2, 6)]
White Action,  (1, 6)
Legal moves are [(2, 0), (2, 6), (4, 1), (4, 2), (4, 6), (4, 7), (5, 3), (5, 4), (5, 5), (5, 6)]
Black Action,  (2, 0)
Legal moves are [(0, 4), (0, 5), (1, 2), (1, 3), (1, 5)]
White Action,  (0, 5)
Legal moves are [(0, 4), (2, 6), (4, 1), (4, 2), (4, 6), (4, 7), (5, 4), (5, 5)]
Black Action,  (4, 7)
Legal moves are [(0, 4), (1, 2), (1, 3), (1, 5), (2, 6), (2, 7), (3, 7)]
White Action,  (0, 4)
Legal moves are [(0, 6), (0, 7), (3, 0), (4, 1), (4, 2), (5, 2), (5, 4), (5, 5)]
Black Action,  (3, 0)
Legal moves are [(1, 3), (1, 5), (2, 6), (2, 7), (4, 1), (4, 2), (4, 6)]
White Action,  (4, 2)
Legal moves are [(0, 6), (0, 7), (1, 2), (1, 3), (5, 0), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6)]
Black Action,  (5, 3)
Legal moves are [(1, 3), (1, 5), (2, 6), (2, 7), (3, 7), (4, 1), (4, 6), (5, 1), (5, 4), (5, 5), (6, 3)]
White Action,  (6, 3)
Legal moves are [(0, 6), (0, 7), (1, 2), (1, 3), (1, 5), (4, 6), (5, 0), (5, 2), (5, 4), (5, 5), (5, 6), (6, 2), (6, 4)]
Black Action,  (0, 7)
Legal moves are [(1, 3), (1, 5), (2, 6), (2, 7), (3, 7), (4, 1), (4, 6), (5, 1), (5, 4), (5, 5)]
White Action,  (2, 6)
Legal moves are [(0, 6), (1, 2), (1, 5), (2, 7), (4, 6), (5, 0), (5, 2), (5, 4), (5, 5), (5, 6), (6, 4)]
Black Action,  (0, 6)
Legal moves are [(1, 3), (2, 7), (3, 7), (4, 1), (4, 6), (5, 1)]
White Action,  (4, 6)
Legal moves are [(1, 2), (1, 5), (2, 7), (3, 7), (5, 0), (5, 2), (5, 4), (5, 5), (5, 6), (6, 4)]
Black Action,  (5, 0)
Legal moves are [(4, 1), (5, 1)]
White Action,  (5, 1)
Legal moves are [(1, 2), (2, 7), (3, 7), (4, 1), (5, 2), (5, 4), (5, 5), (5, 6), (6, 2), (6, 4)]
Black Action,  (2, 7)
Legal moves are [(1, 2), (1, 3), (1, 5), (4, 1)]
White Action,  (1, 3)
Legal moves are [(1, 2), (3, 7), (4, 1), (5, 2), (5, 4), (5, 5), (5, 6), (5, 7), (6, 2), (6, 4), (7, 3)]
Black Action,  (3, 7)
Legal moves are [(1, 2), (1, 5), (4, 1)]
White Action,  (1, 5)
Legal moves are [(1, 2), (4, 1), (5, 2), (5, 4), (5, 5), (5, 6), (5, 7), (6, 2), (6, 4), (7, 3)]
Black Action,  (1, 2)
Legal moves are ['SKIP']
White Action,  SKIP
Legal moves are [(4, 1), (5, 2), (5, 4), (5, 5), (5, 6), (5, 7), (6, 2), (6, 4), (7, 3)]
Black Action,  (5, 2)
Legal moves are [(4, 1), (6, 1)]
White Action,  (4, 1)
Legal moves are [(5, 4), (5, 5), (5, 6), (5, 7), (6, 1), (6, 2), (6, 4), (7, 3), (7, 4)]
Black Action,  (5, 7)
Legal moves are [(6, 1)]
White Action,  (6, 1)
Legal moves are [(5, 4), (5, 5), (5, 6), (6, 2), (6, 4), (7, 0), (7, 1), (7, 2), (7, 3), (7, 4)]
Black Action,  (5, 4)
Legal moves are [(5, 5), (6, 2), (6, 4)]
White Action,  (6, 2)
Legal moves are [(7, 0), (7, 1), (7, 2), (7, 3), (7, 4)]
Black Action,  (7, 0)
Legal moves are [(5, 5), (6, 4), (7, 1)]
White Action,  (6, 4)
Legal moves are [(6, 5), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5)]
Black Action,  (6, 5)
Legal moves are [(5, 5), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5)]
White Action,  (7, 1)
Legal moves are [(7, 2), (7, 3)]
Black Action,  (7, 2)
Legal moves are [(5, 5), (7, 3), (7, 4), (7, 5)]
White Action,  (7, 3)
Legal moves are [(7, 4)]
Black Action,  (7, 4)
Legal moves are [(5, 5), (6, 6), (7, 5)]
White Action,  (7, 5)
Legal moves are [(5, 5), (7, 6)]
Black Action,  (5, 5)
Legal moves are [(5, 6), (6, 6)]
White Action,  (5, 6)
Legal moves are [(6, 6), (6, 7), (7, 6)]
Black Action,  (6, 7)
Legal moves are [(6, 6), (7, 6)]
White Action,  (7, 6)
Legal moves are [(6, 6), (7, 7)]
Black Action,  (7, 7)
Legal moves are ['SKIP']
White Action,  SKIP
Legal moves are [(6, 6)]
Black Action,  (6, 6)
Game Over
  01234567
0 WWWWWWXW
1 WWWWBBWW
2 WWWWBWBW
3 WWWBWBWW
4 WWWWWBWW
5 WWBWWWWW
6 WWWWWWWW
7 WXWWWWWW
Black: 8
White: 54
White wins
```

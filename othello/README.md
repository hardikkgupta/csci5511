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
Finally, create an **AlphabetaPlayer** class that implements minimax search with alpha-beta pruning to decide its moves. Again, have the depth limit be set as a parameter when an object is created. It is possible that the only difference between results of Alpha-beta and Minimax will be the difference in time to arrive at a solution, but that means that it should be reasonable to run alpha-beta with a larger depth limit. I **strongly recommend** that you closely follow the book's algorithm or code when implementing alpha-beta pruning. It is a tricky algorithm.

## Output and Submission
Set up your code so that by default it plays your AlphabetaPlayer (with a reasonable depth limit that doesn't take too long) against RandomPlayer, then swaps colors and does it again.

## How to 

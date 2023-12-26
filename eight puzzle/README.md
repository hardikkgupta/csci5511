# Assignment 1

## Background
The 8-Puzzle is a type of sliding tile puzzle, the most common of which is the 15-puzzleLinks to an external site.
The 8-Puzzle consists of a 3x3 grid of numbered tiles, with one tile (#9) missing. The object of the puzzle is to get the tiles in a particular order, subject to the constraints of physically sliding one tile at a time into the open space.

For our puzzle, we will consider that the following state is our goal:

1 2 3 <br>
8 . 4 <br>
7 6 5 <br>

## Tasks
### State Representation
One important thing you need to think about is how to represent a state of the tile puzzle. A simple way is to use a list or tuple to keep track of what number is in each of the nine positions. Because the 8-puzzle is a simple toy problem, this solution will work. However, for more complex problems, memory might become an issue. If you want to stretch yourself a bit, consider how to represent each state of the 8-puzzle as a single integer. (There are a few reasonable ways to do this.)

Additionally, you will want to write a function that translates from your internal state representation to a visual representation (like the grid above) for debugging purposes. Name this function `visualize` and have it take a state and display a simple grid of the numbers that corresponds to the given state.

### Problem Setup
I recommend (but do not require) using the book's structure for building the problem:

Build a Node class with state, parent, action, and path_cost as member variables
Write a function or method child_node that takes a node and an action and returns the child that is generated when the given action is taken
Use the actions Right, Left, Up, and Down, which correspond to how a tile is moved into the blank space to generate the next state
 

### Uninformed Search
- Breadth-First Search <br>
Write a function `breadth_first` that takes an initial state as input and returns a solution using breadth-first search for this problem. Note that testing this might be tricky... how big is the state space? Make sure you have short solution paths in your testing.

- Depth-Limited Search <br>
Write depth-first search and add a depth limit to create depth-limited search.

- Iterative Deepening <br>
Finally, write a function `iterative_deepening` that takes an initial state as input and returns a solution using iterative-deepening depth-first search by repeatedly calling your depth-limited search function. The solution should be returned as a list of a sequence of actions, starting from the start state, to arrive at the goal state.

### Informed Search
- Heuristics <br>
Write two heuristics, implemented as functions named `num_wrong_tiles` (which counts the number of tiles in the wrong location) and `manhattan_distance` (which calculates the total manhattan distance for all tiles to move to their correct locations), each of which take a state as input and return an integer.

- A* Search <br>
Write A* search for this problem. Name the function `astar` and have it take two parameters: an initial state, and which heuristic function to use as an argument.

## Running your program
Name your program `eight_puzzle.py`

Your program should be runnable from the command line and accept exactly one command-line argument: The initial state, given as a single integer, where "0" corresponds to the blank. Thus, the integer 120843765 would correspond to the initial state

1	2	. <br>
8	4	3 <br>
7	6	5 <br>
 
For which the solution is: Up, Right

Your program should then solve from this given state using breadth-first, iterative deepening, A* with num_wrong_tiles, and A* with manhattan_distance, reporting its answer and time taken for each. 

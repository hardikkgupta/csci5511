# Assignment 2

You are scheduling weekly games for a board game league. This particular board game is a 4-player game, and you have 13 players in your league. To keep things consistent, we shall name the players A, B, C, D, E, F, G, H, I, J, K, L and M. So, for 13 weeks, each week one player will get a "bye" (that is, not play) and the other 12 players will participate in 3 games (each player playing one game.) The goal is to set a league schedule for 13 weeks, 3 games a week.

Here are some desired characteristics for fairness of a full league schedule:

- Each player should play each other player at least once
- Each player should play different opponents as much as possible
- No games with the exact same 4 players should occur, if possible

In a program named `game_schedule.py`, decide on a way to represent a full 13-week league schedule (we will use a complete-state formulation), and then build an objective function that gives a score using the various fairness metrics above. Consider what an "action" or "move" should look like to navigate between different complete-state formulations.

- Implement one of the versions of hill-climbing to find a "good" league schedule.
- Implement one of the versions of simulated annealing to find a "good" league schedule.

Have your program output each algorithm's best league schedule after as much time as you want to give them.

In addition to the actual league schedule for the 13 weeks, have your program also print out a short summary of how many times each player plays each other player.

## How to run

### Sample Input
`python3 scheduling.py`

### Sample Output
```
**** Final result from Hill-Climbing ****
Bye for Player  A :  [['B', 'C', 'L', 'E'], ['J', 'G', 'H', 'I'], ['F', 'K', 'D', 'M']]
Bye for Player  B :  [['A', 'C', 'L', 'E'], ['F', 'K', 'H', 'I'], ['J', 'G', 'D', 'M']]
Bye for Player  C :  [['F', 'B', 'D', 'I'], ['A', 'G', 'L', 'E'], ['J', 'K', 'H', 'M']]
Bye for Player  D :  [['F', 'B', 'C', 'M'], ['A', 'G', 'H', 'I'], ['J', 'K', 'L', 'E']]
Bye for Player  E :  [['J', 'B', 'H', 'D'], ['F', 'G', 'C', 'I'], ['A', 'K', 'L', 'M']]
Bye for Player  F :  [['A', 'B', 'H', 'D'], ['E', 'K', 'C', 'I'], ['J', 'G', 'L', 'M']]
Bye for Player  G :  [['A', 'F', 'L', 'D'], ['E', 'B', 'H', 'M'], ['J', 'K', 'C', 'I']]
Bye for Player  H :  [['E', 'K', 'C', 'D'], ['A', 'F', 'L', 'I'], ['J', 'B', 'G', 'M']]
Bye for Player  I :  [['A', 'B', 'C', 'D'], ['E', 'K', 'G', 'M'], ['J', 'F', 'L', 'H']]
Bye for Player  J :  [['A', 'K', 'G', 'D'], ['E', 'F', 'C', 'H'], ['I', 'B', 'L', 'M']]
Bye for Player  K :  [['A', 'F', 'C', 'M'], ['I', 'B', 'G', 'H'], ['E', 'J', 'L', 'D']]
Bye for Player  L :  [['I', 'J', 'C', 'D'], ['E', 'F', 'G', 'H'], ['A', 'B', 'K', 'M']]
Bye for Player  M :  [['A', 'J', 'C', 'H'], ['E', 'F', 'G', 'D'], ['I', 'B', 'K', 'L']]
**** Replay Summary from Hill-Climbing ****
A :  {'B': 3, 'C': 4, 'D': 4, 'E': 2, 'F': 3, 'G': 3, 'H': 3, 'I': 2, 'J': 1, 'K': 3, 'L': 5, 'M': 3}
B :  {'A': 3, 'C': 3, 'D': 4, 'E': 2, 'F': 2, 'G': 2, 'H': 4, 'I': 4, 'J': 2, 'K': 2, 'L': 3, 'M': 5}
C :  {'A': 4, 'B': 3, 'D': 3, 'E': 5, 'F': 4, 'G': 1, 'H': 2, 'I': 4, 'J': 3, 'K': 3, 'L': 2, 'M': 2}
D :  {'A': 4, 'B': 4, 'C': 3, 'E': 3, 'F': 4, 'G': 3, 'H': 2, 'I': 2, 'J': 4, 'K': 3, 'L': 2, 'M': 2}
E :  {'A': 2, 'B': 2, 'C': 5, 'D': 3, 'F': 3, 'G': 4, 'H': 3, 'I': 1, 'J': 2, 'K': 4, 'L': 5, 'M': 2}
F :  {'A': 3, 'B': 2, 'C': 4, 'D': 4, 'E': 3, 'G': 3, 'H': 4, 'I': 4, 'J': 1, 'K': 2, 'L': 3, 'M': 3}
G :  {'A': 3, 'B': 2, 'C': 1, 'D': 3, 'E': 4, 'F': 3, 'H': 4, 'I': 4, 'J': 4, 'K': 2, 'L': 2, 'M': 4}
H :  {'A': 3, 'B': 4, 'C': 2, 'D': 2, 'E': 3, 'F': 4, 'G': 4, 'I': 4, 'J': 5, 'K': 2, 'L': 1, 'M': 2}
I :  {'A': 2, 'B': 4, 'C': 4, 'D': 2, 'E': 1, 'F': 4, 'G': 4, 'H': 4, 'J': 3, 'K': 4, 'L': 3, 'M': 1}
J :  {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 2, 'F': 1, 'G': 4, 'H': 5, 'I': 3, 'K': 3, 'L': 4, 'M': 4}
K :  {'A': 3, 'B': 2, 'C': 3, 'D': 3, 'E': 4, 'F': 2, 'G': 2, 'H': 2, 'I': 4, 'J': 3, 'L': 3, 'M': 5}
L :  {'A': 5, 'B': 3, 'C': 2, 'D': 2, 'E': 5, 'F': 3, 'G': 2, 'H': 1, 'I': 3, 'J': 4, 'K': 3, 'M': 3}
M :  {'A': 3, 'B': 5, 'C': 2, 'D': 2, 'E': 2, 'F': 3, 'G': 4, 'H': 2, 'I': 1, 'J': 4, 'K': 5, 'L': 3}
**** Final result from Simulated-Annealing ****
Bye for Player  A :  [['J', 'C', 'L', 'I'], ['B', 'G', 'H', 'E'], ['F', 'K', 'D', 'M']]
Bye for Player  B :  [['A', 'K', 'H', 'I'], ['F', 'C', 'D', 'M'], ['J', 'G', 'L', 'E']]
Bye for Player  C :  [['F', 'B', 'L', 'M'], ['A', 'G', 'D', 'I'], ['J', 'K', 'H', 'E']]
Bye for Player  D :  [['F', 'G', 'C', 'M'], ['J', 'B', 'L', 'I'], ['A', 'K', 'H', 'E']]
Bye for Player  E :  [['F', 'G', 'C', 'D'], ['A', 'B', 'L', 'I'], ['J', 'K', 'H', 'M']]
Bye for Player  F :  [['A', 'B', 'H', 'D'], ['J', 'K', 'L', 'M'], ['E', 'G', 'C', 'I']]
Bye for Player  G :  [['J', 'B', 'H', 'D'], ['A', 'K', 'L', 'I'], ['E', 'F', 'C', 'M']]
Bye for Player  H :  [['J', 'B', 'G', 'I'], ['A', 'F', 'L', 'M'], ['E', 'K', 'C', 'D']]
Bye for Player  I :  [['J', 'F', 'C', 'M'], ['E', 'K', 'G', 'D'], ['A', 'B', 'L', 'H']]
Bye for Player  J :  [['E', 'B', 'G', 'M'], ['A', 'F', 'L', 'D'], ['I', 'K', 'C', 'H']]
Bye for Player  K :  [['A', 'B', 'G', 'D'], ['I', 'J', 'C', 'M'], ['E', 'F', 'L', 'H']]
Bye for Player  L :  [['A', 'J', 'K', 'M'], ['I', 'F', 'G', 'H'], ['E', 'B', 'C', 'D']]
Bye for Player  M :  [['A', 'J', 'C', 'L'], ['I', 'B', 'K', 'H'], ['E', 'F', 'G', 'D']]
**** Replay Summary from Simulated-Annealing ****
A :  {'B': 4, 'C': 1, 'D': 4, 'E': 1, 'F': 2, 'G': 2, 'H': 4, 'I': 4, 'J': 2, 'K': 4, 'L': 6, 'M': 2}
B :  {'A': 4, 'C': 1, 'D': 4, 'E': 3, 'F': 1, 'G': 4, 'H': 5, 'I': 4, 'J': 3, 'K': 1, 'L': 4, 'M': 2}
C :  {'A': 1, 'B': 1, 'D': 4, 'E': 4, 'F': 5, 'G': 3, 'H': 1, 'I': 4, 'J': 4, 'K': 2, 'L': 2, 'M': 5}
D :  {'A': 4, 'B': 4, 'C': 4, 'E': 4, 'F': 5, 'G': 5, 'H': 2, 'I': 1, 'J': 1, 'K': 3, 'L': 1, 'M': 2}
E :  {'A': 1, 'B': 3, 'C': 4, 'D': 4, 'F': 3, 'G': 6, 'H': 4, 'I': 1, 'J': 2, 'K': 4, 'L': 2, 'M': 2}
F :  {'A': 2, 'B': 1, 'C': 5, 'D': 5, 'E': 3, 'G': 4, 'H': 2, 'I': 1, 'J': 1, 'K': 1, 'L': 4, 'M': 7}
G :  {'A': 2, 'B': 4, 'C': 3, 'D': 5, 'E': 6, 'F': 4, 'H': 2, 'I': 4, 'J': 2, 'K': 1, 'L': 1, 'M': 2}
H :  {'A': 4, 'B': 5, 'C': 1, 'D': 2, 'E': 4, 'F': 2, 'G': 2, 'I': 4, 'J': 3, 'K': 6, 'L': 2, 'M': 1}
I :  {'A': 4, 'B': 4, 'C': 4, 'D': 1, 'E': 1, 'F': 1, 'G': 4, 'H': 4, 'J': 4, 'K': 4, 'L': 4, 'M': 1}
J :  {'A': 2, 'B': 3, 'C': 4, 'D': 1, 'E': 2, 'F': 1, 'G': 2, 'H': 3, 'I': 4, 'K': 4, 'L': 5, 'M': 5}
K :  {'A': 4, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 1, 'G': 1, 'H': 6, 'I': 4, 'J': 4, 'L': 2, 'M': 4}
L :  {'A': 6, 'B': 4, 'C': 2, 'D': 1, 'E': 2, 'F': 4, 'G': 1, 'H': 2, 'I': 4, 'J': 5, 'K': 2, 'M': 3}
M :  {'A': 2, 'B': 2, 'C': 5, 'D': 2, 'E': 2, 'F': 7, 'G': 2, 'H': 1, 'I': 1, 'J': 5, 'K': 4, 'L': 3}
```


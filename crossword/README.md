# Final Project

## Introduction
A Constraint Satisfaction Problem is characterized by:
1. a set of variables $x_1$, $x_2$, .., $x_n$
2. for each variable $x_i$ a domain $D_i$ denotes the possible values, and
3. a set of constraints, i.e., relations, that denotes the relations between the values of the variables. This will help in determining the values for each variable.

We will only consider constraints involving one or two variables. Searching can be made easier in cases where the solution, instead of corresponding to an optimal path, is only required to satisfy local consistency conditions. We call such problems Constraint Satisfaction Problems (CSP). For example, in a crossword puzzle it is only required that words that cross each other have the same letter in the location where they cross.

## Problem Formulation
### Variables
Each variable represents a word in the crossword puzzle. For each variable, we need to decide its value, which is the specific word from the vocabulary list.
### Domain
The domain of each variable is the set of possible words it can take from the given vocabulary list. 
### Constraint
_Unary constraints_ on each variable are given by the length of the word.
Binary constraints arise from the overlap between neighboring variables. Overlap is represented as a pair of indices (i, j) indicating that the ith character of one variable must be the same as the jth character of another variable. All words must be different; the same word should not be repeated in the puzzle.
### Objective
Find a satisfying assignment, i.e., a different word for each variable such that all unary and binary constraints are met.

### Approach
_Enforce Node Consistency_: Ensure that every value in a variable’s domain satisfies its unary constraints (length). <br>
_Enforce Arc Consistency (AC3)_: Ensure that binary constraints (overlaps) are satisfied. Backtracking: Use backtracking to explore possible assignments until a solution is found.

## Literature Review
_Solving Crossword Puzzles as Probabilistic Constraint Satisfaction_ by Noam M. Shazeer, Michael L. Littman, and Greg A. Keim is a paper that describes a formal model of constraint satisfaction with probabilistic preferences on variable values The authors define two natural optimization problems for this model: maximizing the probability of a correct solution and maximizing the number of correct words (variable values) in the solution. They provide an efficient iterative approximation for the latter based on dynamic programming and present very encouraging results on a collection of real and artificial crossword puzzles. Also the review _Crossword Puzzles and Constraint Satisfaction_ by James Connor, John Duchi, and Bruce Lo from Stanford University, describes how to solve crossword puzzles using a basic backtracking algorithm with a few modifications. The paper also investigates different constraint satisfaction problem (CSP) algorithms, including forward checking, dynamic variable ordering, conflict-directed backjumping, and arc consistency. The authors suggest that these algorithms make for significantly more efficient CSP solvers.

## Software
We will write this AI in python3, utilising standard libraries for representation and algorithms. The user interface will be a command-line-based interface for simplicity and compatibility.

## Instructions on how to run your project
The terminal command is:
```
python3 crossword.py <skeleton_file> <word_file>
```
To run directly with skeleton0.txt and words0.txt, run the code using:
```
python3 crossword.py data/skeleton0.txt data/dictionary0.txt
```
You can change the `skeleton file(0/1/2).txt` and `dictionary(0/1/2).txt`. All the skeleton files should be paired with the respective dictionary files.
Four files are provided to check how well it performs on the crossword from external sources. These files: `easy.txt`, `med.txt`, `med2.txt` and `diff.txt`, all uses the same word list file: `word list.txt`.

## Limitations
One limitation is that CSPs can be computationally expensive to solve, especially for large puzzles. Another limitation is that CSPs may not be able to capture all of the constraints that are present in a crossword puzzle. For example, CSPs may not be able to capture the fact that certain words are more likely to appear in certain positions in the puzzle than others.

## Functions
_grid_: Return 2D array representing a given assignment. <br>
_show_: Print crossword assignment to the terminal. <br>
_solution_: Enforce node and arc consistency, and then solve the CSP. <br>
_node consistency_: Remove any values that are inconsistent with a variable’s unary constraints; in this case, the length of the word. <br>
_revise_: Make variable x arc consistent with variable y. To do so, remove values from `self.domains[x]` for which there is no possible corresponding value for y in `self.domains[y]`. Return True if a revision was made to the domain of x; return False if no revision was made. <br>
_ac3_: Perform ac3 algorithm <br>
_assignment_: Return True if assignment is complete (i.e., assigns a value to each crossword variable); return False otherwise. <br>
_consistent_: Return True if assignment is consistent (i.e., words fit in crossword puzzle without con- flicting characters); return False otherwise. <br>
_order domain values_: Return a list of values in the domain of var, in order by the number of values they rule out for neighboring variables. The first value in the list, for example, should be the one that rules out the fewest values among the neighbors of var. <br>
_unassigned variable_: Return an unassigned variable not already part of assignment. Choose the variable with the minimum number of remaining values in its domain. If there is a tie, choose the variable with the highest degree. If there is a tie, any of the tied variables are acceptable return values. <br>
_backtrack_: Using Backtracking Search, take as input a partial assignment for the crossword and return a complete assignment if possible to do so. assignment is a mapping from variables (keys) to words (values). If no assignment is possible, return None.


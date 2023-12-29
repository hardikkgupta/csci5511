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
Approach
_Enforce Node Consistency_: Ensure that every value in a variable’s domain satisfies its unary constraints (length).
_Enforce Arc Consistency (AC3)_: Ensure that binary constraints (overlaps) are satisfied. Backtracking: Use backtracking to explore possible assignments until a solution is found.

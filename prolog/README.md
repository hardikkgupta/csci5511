# Assignment 6

This assignment will use First Order Logic in the form of prolog programs in order to represent knowledge.

Prolog is a language that you can install on your home computer (download from [here](https://www.swi-prolog.org/download/stable)), or you can build small programs online at: (https://swish.swi-prolog.org/) which has an interactive online IDE.

Using prolog, we'll build a few different knowledge bases and see if we're able to resolve queries about them. Put all of your code in a file named `prologhw.pl` and submit that.

## Kinship Domain
Let's redo the kinship predicates that we talked about in lecture. 

Start with the following knowledge:
```
parent(charles, william).
parent(charles, harry).
parent(elizabeth, charles).
parent(george, elizabeth).
parent(george, margaret).
parent(elizabeth, anne).
parent(elizabeth, andrew).
parent(elizabeth, edward).
parent(anne, peter).
parent(anne, zara).
parent(andrew, beatrice).
parent(andrew, eugenie).
parent(edward, louise).
parent(edward, james).
```
_(It's like I've been watching the most old seasons of The Crown or something.)_

Encode into your program the following predicates:

`child(X,Y)` in terms of the `parent` predicate.
`sibling(X,Y)` in terms of the `parent` predicate.
When finished, the query `sibling(anne, X).` should resolve to:
- X = charles
- X = andrew
- X = edward <br>

`cousin(X,Y)` in terms of other predicates (assuming we mean specifically first cousin, not anything removed, etc.)
When finished, the query `cousin(beatrice, X).` should resolve to:
- X = william 
- X = harry
- X = peter
- X = zara
- X = louise
- X = james <br>

`ancestor(X,Y)` in terms of other predicates.
When finished the query ancestor(X, louise). should resolve to:
- X = edward
- X = george
- X = elizabeth
- false.
- ... and not result in an infinite loop!

## Maze Solving
The following knowledge base describes a maze:
```
connected(1,2).
connected(3,4).
connected(5,6).
connected(7,8).
connected(9,10).
connected(11,13).
connected(13,14).
connected(15,16).
connected(17,18).
connected(19,20).
connected(4,1).
connected(6,3).
connected(4,7).
connected(6,12).
connected(14,9).
connected(12,15).
connected(16,11).
connected(14,17).
connected(16,19).
```
The maze consists of 20 points, (named 1 - 20,) some of which are connected to others by one-way paths. Thus, you can travel from 1 to 2, but not from 2 to 1.

Write predicates as follows:
- `path(X,Y)` that can determine which points you can get to from other points in the maze.
- `path_length(X,Y,N)` that adds a length parameter to the path predicate. (I.e. it is true if there is a path from X to Y via N edges.)
 
These predicates should be resolvable when any of the inputs is a variable. I.e. path_length(6,10,N) should give N=8, and path_length(6, X, 2) should give X = 4 and X = 15, and path_length(X,10,8) should give X=6.

## How to Run
Visit the [link](https://www.swi-prolog.org/download/stable) to run the online IDE or you can download the software.

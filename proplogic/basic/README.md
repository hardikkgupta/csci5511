# Assignment 4

This is a short assignment that has the goal of getting you familiar with using a propositional logic as a knowledge representation language in order to solve some problems.

You will need to download and unzip the code in `proplogic_sat.zip`. This zip file contains a few python modules that you can use to help determine satisfiability for propositional logic knowledge bases. The module that you will use is sat_interface, and an example of using it is in the writeup below.

The code included there is adapted from [here](https://github.com/sahands/simple-satLinks).

Note: If you really don't want to use python, you are welcome to find a sat solver for your language of choice and use that instead, but make sure that you include all the necessary code to be able to run your program when you submit.

## An Example Problem
Suppose that liars always speak what is false, and truth-tellers always speak what is true. Further suppose that Amy, Bob, and Cal are each either a liar or truth-teller. Amy says, "Bob is a liar." Bob says, "Cal is a liar." Cal says, "Amy and Bob are liars." Which, if any, of these people are truth-tellers?

To solve this using propositional logic, we need to define this problem in those terms. Let us consider the following three boolean variables to use in our knowledge base:

- A Amy is a truth-teller
- B Bob is a truth-teller
- C Cal is a truth-teller
  
With these three variables, we will build sentences from logical connectives that fully encompass all the relationships described in the problem.

Let us consider the first piece of information:

_Amy says, "Bob is a liar."_

Amy is making the claim that Bob is not a truth-teller. If Amy is a truth-teller, then Bob must be a liar. But conversely, if Bob is a truth-teller, then Amy must be a liar. Therefore, we can encode this piece of information as:

A ↔ B

Similarly, the second and third sequences can be encoded as <br>
B ↔ ~C

and <br>
C ↔ (~A Ʌ ~B)

Next, we'll need to convert this to conjunctive normal form. After some work, you would get the following clauses:

~A V ~B <br>
B V A <br>
~B V ~C <br>
C V B <br>
~C V ~A <br>
~C V ~B <br>
A V B V C <br>

To represent this information in our python sat interface, you would create a list of strings, with each string representing a separate clause, "or" symbols left as spaces, and "not" symbols replaced with "~", as follows:

(Note: this example uses the python interactive shell, you'll probably want to write your code inside an actual module.)

```
>>> import sat_interface
>>> example_prob = sat_interface.KB(["~A ~B", "B A", "~B ~C", "C B", "~C ~A", "~C ~B", "A B C"])
>>> example_prob.is_satisfiable()
True
```


So this would create the knowledge base, and then test its satisfiability. Great! Except I am interested in knowing specifics! So, to check a specific piece of knowledge, I can try using the test_literal() method:
```
>>> example_prob.test_literal("A")
False
>>> example_prob.test_literal("~A")
True
```
This pair of tests tells me that the knowledge base is unsatisfiable when I add the clause A, and remains satisfiable when I add the clause ~A, so I can conclude that Amy is, in fact, a liar. 

Note: I may need to test both A and ~A to draw conclusions! (Why?)

## Your Task
Write a python module named `proplogic.py` that uses the `sat_interface` module to create and solve each of the following logic problems. Your "solution" should be contained in a function that, when called, creates the appropriate clauses, then tests each of the literals in the problem, then prints out its results.

### Liars and Truth-tellers II
Three people, Amy, Bob, and Cal, are each either a liar or a truth-teller. Assume that liars always lie, and truth-tellers always tell the truth.

- Amy says, "Cal and I are truthful."
- Bob says, "Cal is a liar."
- Cal says, "Bob speaks the truth or Amy lies."
What can you conclude about the truthfulness of each?

Write your answer in a function named `tt2`, and have it return a tuple with the three T/F values for proposition symbols A, B, and C.

### Liars and Truth-tellers III
Three people, Amy, Bob, and Cal, are each either a liar or a truth-teller. Assume that liars always lie, and truth-tellers always tell the truth.

- Amy says, "Cal is not honest."
- Bob says, "Amy and Cal never lie."
- Cal says, "Bob is correct."
What can you conclude about the truthfulness of each?

Write your answer in a function named `tt3`, and have it return a tuple with the three T/F values for proposition symbols A, B, and C. 

### Robbery and a Salt
The salt has been stolen! Well, it was found that the culprit was either the Caterpillar, Bill the Lizard or the Cheshire Cat. The three were tried and made the following statements in court:

CATERPILLAR: Bill the Lizard stole the salt.

BILL THE LIZARD: That is true!

CHESHIRE CAT: I never stole the salt.

As it happened, at least one of them lied and at least one told the truth. Who stole the salt?
Write your answer in a function named `salt`, and have it return a dictionary with keys that are string descriptions of a proposition symbol, and values that are the T/F value that you can infer about that proposition symbol.

### An honest name
Three golfers named Tom, Dick, and Harry are walking to the clubhouse.
The first man in line says, "The guy in the middle is Harry."
The man in the middle says, "I’m Dick."
The last man says, "The guy in the middle is Tom."
Tom, the best golfer of the three, always tells the truth.
Dick sometimes tells the truth, while Harry, the worst golfer, never does.

### Figure out who is who.
Write your answer in a function named `golf`, and have it return a dictionary with keys that are string descriptions of a proposition symbol, and values that are the T/F value that you can infer about that proposition symbol.

## How to run
_**Note: Remember to put `proplogic.py` file inside the proplogic_sat directory before running**_
### Sample Input
```
python3 proplogic.py
```
### Sample Output
```
Liars and Truth-tellers II 
(False, False, True) 
-------------------------
Liars and Truth-tellers III 
(True, False, False) 
-------------------------
Robbery and a Salt 
{'Caterpillar stole the salt': True, 'Bill the Lizard stole the salt': False, 'Cheshire Cat stole the salt': False, 'Caterpillar is Truthful': False, 'Bill the Lizard is Truthful': False, 'Cheshire Cat is Truthful': True} 
-------------------------
An honest name 
{'Tom is in 1st place': True, 'Tom is in 2nd place': False, 'Tom is in 3rd place': False, 'Harry is in 1st place': False, 'Harry is in 2nd place': True, 'Harry is in 3rd place': False, 'Dick is in 1st place': False, 'Dick is in 2nd place': False, 'Dick is in 3rd place': True}
```

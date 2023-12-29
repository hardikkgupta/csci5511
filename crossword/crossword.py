import sys
import time

class Variable():
    ACROSS = "across"
    DOWN = "down"

    def __init__(self, i, j, direction, length):
        self.i = i
        self.j = j
        self.direction = direction
        self.length = length
        self.cells = []
        for k in range(self.length):
            self.cells.append(
                (self.i + (k if self.direction == Variable.DOWN else 0),
                 self.j + (k if self.direction == Variable.ACROSS else 0))
            )

    def __hash__(self):
        return hash((self.i, self.j, self.direction, self.length))

    def __eq__(self, other):
        return (
            (self.i == other.i) and
            (self.j == other.j) and
            (self.direction == other.direction) and
            (self.length == other.length)
        )

    def __str__(self):
        return f"({self.i}, {self.j}) {self.direction} : {self.length}"

    def __repr__(self):
        direction = repr(self.direction)
        return f"Variable({self.i}, {self.j}, {direction}, {self.length})"


class Crossword():

    def __init__(self, skeleton_file, dictionary_file):

        with open(skeleton_file) as f:

            contents = f.read().splitlines()
            self.height = len(contents)
            self.width = max(len(line) for line in contents)

            # If the contents are:
            # contents = [
            #     "_____",  # Row 1
            #     "__#__",  # Row 2
            #     "_###_",  # Row 3
            #     "__#__",  # Row 4
            #     "_____"  # Row 5
            # ]

            # then the output is:
            # self.skeleton = [
            #     [True, True, True, True, True],  # Row 1
            #     [True, True, False, True, True],  # Row 2
            #     [True, False, False, False, True],  # Row 3
            #     [True, True, False, True, True],  # Row 4
            #     [True, True, True, True, True]  # Row 5
            # ]
            self.skeleton = []
            for i in range(self.height):
                row = []
                for j in range(self.width):
                    if j >= len(contents[i]):
                        row.append(False)
                    elif contents[i][j] == "_":
                        row.append(True)
                    else:
                        row.append(False)
                self.skeleton.append(row)

        # Save vocabulary list
        # If the dictionary file contains
        # apple
        # banana
        # orange
        # apple
        # grape

        # self.dictionary = {'APPLE', 'BANANA', 'ORANGE', 'GRAPE'}
        with open(dictionary_file) as f:
            self.dictionary = set(f.read().upper().splitlines())

        self.variables = set()
        for i in range(self.height):
            for j in range(self.width):

                starts_word = (
                    self.skeleton[i][j]
                    and (i == 0 or not self.skeleton[i - 1][j])
                )
                if starts_word:
                    length = 1
                    for k in range(i + 1, self.height):
                        if self.skeleton[k][j]:
                            length += 1
                        else:
                            break
                    if length > 1:
                        self.variables.add(Variable(
                            i=i, j=j,
                            direction=Variable.DOWN,
                            length=length
                        ))

                starts_word = (
                    self.skeleton[i][j]
                    and (j == 0 or not self.skeleton[i][j - 1])
                )
                if starts_word:
                    length = 1
                    for k in range(j + 1, self.width):
                        if self.skeleton[i][k]:
                            length += 1
                        else:
                            break
                    if length > 1:
                        self.variables.add(Variable(
                            i=i, j=j,
                            direction=Variable.ACROSS,
                            length=length
                        ))
        # Compute overlaps for each word
        # For any pair of variables v1, v2, their overlap is either:
        #    None, if the two variables do not overlap; or
        #    (i, j), where v1's ith character overlaps v2's jth character

        # self.overlaps
        # {(Variable(1, 4, 'down', 4), Variable(4, 1, 'across', 4)): (3, 3),
        #  (Variable(1, 4, 'down', 4), Variable(0, 1, 'down', 5)): None,
        #  (Variable(1, 4, 'down', 4), Variable(0, 1, 'across', 3)): None,
        #  (Variable(4, 1, 'across', 4), Variable(1, 4, 'down', 4)): (3, 3),
        #  (Variable(4, 1, 'across', 4), Variable(0, 1, 'down', 5)): (0, 4),
        #  (Variable(4, 1, 'across', 4), Variable(0, 1, 'across', 3)): None,
        #  (Variable(0, 1, 'down', 5), Variable(1, 4, 'down', 4)): None,
        #  (Variable(0, 1, 'down', 5), Variable(4, 1, 'across', 4)): (4, 0),
        #  (Variable(0, 1, 'down', 5), Variable(0, 1, 'across', 3)): (0, 0),
        #  (Variable(0, 1, 'across', 3), Variable(1, 4, 'down', 4)): None,
        #  (Variable(0, 1, 'across', 3), Variable(4, 1, 'across', 4)): None,
        #  (Variable(0, 1, 'across', 3), Variable(0, 1, 'down', 5)): (0, 0)}

        self.overlaps = dict()
        for v1 in self.variables:
            for v2 in self.variables:
                if v1 == v2:
                    continue
                cells1 = v1.cells
                cells2 = v2.cells
                intersection = set(cells1).intersection(cells2)
                if not intersection:
                    self.overlaps[v1, v2] = None
                else:
                    intersection = intersection.pop()
                    self.overlaps[v1, v2] = (
                        cells1.index(intersection),
                        cells2.index(intersection)
                    )

    def neighbors(self, var):
        return set(
            v for v in self.variables
            if v != var and self.overlaps[v, var]
        )

class Game():
    def __init__(self, crossword):
        self.crossword = crossword
        self.domains = {
            var: self.crossword.dictionary.copy()
            for var in self.crossword.variables
        }

    def grid(self, assignment):
        letters = [[None] * self.crossword.width for _ in range(self.crossword.height)]

        for variable, word in assignment.items():
            direction = variable.direction
            for k, (di, dj) in enumerate(
                    [(0, 1) if direction == Variable.ACROSS else (1, 0) for _ in range(len(word))]):
                i, j = variable.i + k * di, variable.j + k * dj
                letters[i][j] = word[k]
        return letters

    def show(self, assignment):
        letters = self.grid(assignment)
        for i in range(self.crossword.height):
            print("".join(
                letters[i][j] or " " if self.crossword.skeleton[i][j] else "-" for j in range(self.crossword.width)))

    def solution(self):
        self.node_consistency()
        self.ac3()
        return self.backtrack(dict())

    def node_consistency(self):
        for var in self.domains:
            for word in set(self.domains[var]):
                if len(word) != var.length:
                    self.domains[var].remove(word)

    def revise(self, x, y):
        revised = False
        i, j = self.crossword.overlaps[x, y]

        for x_word in set(self.domains[x]):
            if all(x_word[i] != y_word[j] for y_word in self.domains[y]):
                self.domains[x].remove(x_word)
                revised = True

        return revised

    def ac3(self, arcs=None):
        if arcs is None:
            arcs = list()
            for x in self.domains:
                for y in self.crossword.neighbors(x):
                    arcs.append((x, y))
        while arcs:
            x, y = arcs.pop()
            if self.revise(x, y):
                if not self.domains[x]:
                    return False
                for z in self.crossword.neighbors(x) - self.domains[y]:
                    arcs.append((z, x))
        return True

    def assignment(self, assignment):
        return not bool(self.crossword.variables - set(assignment))

    def consistent(self, assignment):
        used_dictionary = set()
        for var in assignment:
            if assignment[var] in used_dictionary or len(assignment[var]) != var.length:
                return False
            used_dictionary.add(assignment[var])
            for neighbor in self.crossword.neighbors(var):
                if neighbor in assignment:
                    i, j = self.crossword.overlaps[var, neighbor]
                    if assignment[var][i] != assignment[neighbor][j]:
                        return False
        return True

    def unassigned_variable(self, assignment):
        best = None
        for var in self.crossword.variables - set(assignment):
            if (
                best is None or
                len(self.domains[var]) < len(self.domains[best]) or
                len(self.crossword.neighbors(var)) > len(self.crossword.neighbors(best))
            ):
                best = var
        return best

    def backtrack(self, assignment):
        if self.assignment(assignment):
            return assignment
        var = self.unassigned_variable(assignment)
        for value in self.domains[var]:
            assignment[var] = value
            if self.consistent(assignment) and (result := self.backtrack(assignment)) is not None:
                return result
            assignment.pop(var)
        return None


def main():
    skeleton = sys.argv[1]
    dictionary = sys.argv[2]
    start_time = time.time()

    crossword = Crossword(skeleton, dictionary)
    game = Game(crossword)
    assignment = game.solution()

    if assignment is None:
        print("Cannot find solution")
    else:
        game.show(assignment)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time taken: {elapsed_time} seconds")

if __name__ == "__main__":
    main()

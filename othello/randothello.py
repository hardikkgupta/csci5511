'''
randothellogame module

sets up a RandOthello game closely following the book's framework for games

RandOthelloState is a class that will handle our state representation, then we've 
got stand-alone functions for player, actions, result and terminal_test

Differing from the book's framework, is that utility is *not* a stand-alone 
function, as each player might have their own separate way of calculating utility


'''
import random
import copy

# Representation Purposes
WHITE = 1
BLACK = -1
EMPTY = 0
BLOCKED = -2
SIZE = 8
SKIP = "SKIP"


class OthelloPlayerTemplate:
    '''Template class for an Othello Player

    An othello player *must* implement the following methods:

    get_color(self) - correctly returns the agent's color

    make_move(self, state) - given the state, returns an action that is the agent's move
    '''
    def __init__(self, mycolor):
        self.color = mycolor

    def get_color(self):
        return self.color

    def make_move(self, state):
        '''Given the state, returns a legal action for the agent to take in the state
        '''
        return None

class MinimaxPlayer(OthelloPlayerTemplate):
    def __init__(self, mycolor, d):
        self.color = mycolor
        self.depth = d

    def get_color(self):
        return self.color

    def make_move(self,state):
        # print(state)
        # curr_move = None
        legals = actions(state)
        # while curr_move == None:
        # display(state)
        # if self.color == 1:
        #     print("White ", end='')
        # else:
        #     print("Black ", end='')
        # print(" to play.")
        print("Legal moves are " + str(legals))
        move = self.minimax(state, self.depth)
        return move

    def minimax(self, state, depth):
        # print("depth", depth)
        # player = self.color
        value, move = self.maxValue(state, depth)
        return move

    def maxValue(self, state, depth):
        if terminal_test(state) or depth == 0:
            return self.UtilityFunc(state), None
            # print("true")
        v = float('-inf')
        for action in actions(state):
            v2, a2 = self.minValue(result(state, action), depth - 1)
            if v2 > v:
                v, move = v2, action
        # print("move inside maxValue", move)
        return v, move

    def minValue(self, state, depth):
        if terminal_test(state) or depth == 0:
            return self.UtilityFunc(state), None
        v = float('inf')
        for action in actions(state):
            v2, a2 = self.maxValue(result(state, action), depth - 1)
            if v2 < v:
                v, move = v2, action
        # print("move inside minValue", move)
        return v, move

    def UtilityFunc(self, state):
        mycolor = self.color
        opponent = mycolor * -1
        B, W = 0, 0
        job = 0

        for i in range(8):
            for j in range(8):
                if state.board_array[i][j] == 1:
                    W += 1
                elif state.board_array[i][j] == -1:
                    B += 1
        if W > B:
            lead = 1
        elif W < B:
            lead = -1
        else:
            lead = 0
        # Corner
        for i in range(8):
            for j in range(8):
                if (i == 0 or i == 7) and (j == 0 or j == 7) and state.board_array[i][j] == mycolor:
                    job += 50
                elif (i == 0 or i == 7) and (j == 0 or j == 7) and state.board_array[i][j] == opponent:
                    job -= 50
        # Edge
        for i in range(8):
            for j in range(8):
                if (i == 0 or i == 7) or (j == 0 or j == 7) and state.board_array[i][j] == mycolor:
                    job += 20
                elif (i == 0 or i == 7) or (j == 0 or j == 7) and state.board_array[i][j] == opponent:
                    job -= 40

        if lead == mycolor:
            # print("Winning")
            return 100 + job
        elif lead == 0:
            # print("Losing")
            return -100
        else:
            return -500

class AlphabetaPlayer(OthelloPlayerTemplate):
    def __init__(self, mycolor, d):
        self.color = mycolor
        self.depth = d

    def get_color(self):
        return self.color

    def make_move(self,state):
        # print(state)
        # curr_move = None
        legals = actions(state)
        # while curr_move == None:
        # display(state)
        # if self.color == 1:
        #     print("White ", end='')
        # else:
        #     print("Black ", end='')
        # print(" to play.")
        print("Legal moves are " + str(legals))
        move = self.minimax(state, self.depth)
        return move

    def minimax(self, state, depth):
        # print("depth", depth)
        # player = self.color
        value, move = self.maxValue(state, float('-inf'), float('inf'), depth)
        return move

    def maxValue(self, state, alpha, beta, depth):
        # print("inside")
        # print("Terminal", terminal_test(state))
        if terminal_test(state) or depth == 0:
            return self.UtilityFunc(state), None
            # print("true")
        v = float('-inf')
        for action in actions(state):
            v2, a2 = self.minValue(result(state, action), float('-inf'), float('inf'), depth - 1)
            if v2 > v:
                v, move = v2, action
                alpha = max(alpha, v)
            if v >= beta:
                return v, move
        # print("move inside maxValue", move)
        return v, move

    def minValue(self, state, alpha, beta, depth):
        if terminal_test(state) or depth == 0:
            return self.UtilityFunc(state), None
        v = float('inf')
        for action in actions(state):
            v2, a2 = self.maxValue(result(state, action), alpha, beta, depth - 1)
            if v2 < v:
                v, move = v2, action
                beta = min(beta, v)
            if v <= alpha:
                return v, move
        # print("move inside minValue", move)
        return v, move

    def UtilityFunc(self, state):
        mycolor = self.color
        opponent = mycolor * -1
        B, W = 0, 0
        job = 0

        for i in range(8):
            for j in range(8):
                if state.board_array[i][j] == 1:
                    W += 1
                elif state.board_array[i][j] == -1:
                    B += 1
        if W > B:
            lead = 1
        elif W < B:
            lead = -1
        else:
            lead = 0
        # Corner
        for i in range(8):
            for j in range(8):
                if (i == 0 or i == 7) and (j == 0 or j == 7) and state.board_array[i][j] == mycolor:
                    job += 50
                elif (i == 0 or i == 7) and (j == 0 or j == 7) and state.board_array[i][j] == opponent:
                    job -= 50
        # Edge
        for i in range(8):
            for j in range(8):
                if (i == 0 or i == 7) or (j == 0 or j == 7) and state.board_array[i][j] == mycolor:
                    job += 20
                elif (i == 0 or i == 7) or (j == 0 or j == 7) and state.board_array[i][j] == opponent:
                    job -= 40

        if lead == mycolor:
            # print("Winning")
            return 100 + job
        elif lead == 0:
            # print("Losing")
            return -100
        else:
            return -500

class RandomPlayer(OthelloPlayerTemplate):
    def __init__(self, mycolor):
        self.color = mycolor

    def get_color(self):
        return self.color

    def make_move(self,state):
        curr_move = None
        legals = actions(state)
        print("Legal moves are " + str(legals))
        move = random.choice(legals)
        return move
        #     # move = input("Enter your move as a r,c pair:")
        #     move = str(random.choice(legals)).replace("(", "").replace(")", "")
        #     if move == "":
        #         return legals[0]
        #
        #     if move == SKIP and SKIP in legals:
        #         return move
        #
        #     try:
        #         movetup = int(move.split(',')[0]), int(move.split(',')[1])
        #     except:
        #         movetup = None
        #     if movetup in legals:
        #         curr_move = movetup
        #     else:
        #         print("That doesn't look like a legal action to me")
        # return curr_move

class HumanPlayer(OthelloPlayerTemplate):
    def __init__(self, mycolor):
        self.color = mycolor

    def get_color(self):
        return self.color

    def make_move(self, state):
        curr_move = None
        legals = actions(state)
        while curr_move == None:
            display(state)
            if self.color == 1:
                print("White ", end='')
            else:
                print("Black ", end='')
            print(" to play.")
            print("Legal moves are " + str(legals))
            move = input("Enter your move as a r,c pair:")
            if move == "":
                return legals[0]

            if move == SKIP and SKIP in legals:
                return move

            try:
                movetup = int(move.split(',')[0]), int(move.split(',')[1])
            except:
                movetup = None
            if movetup in legals:
                curr_move = movetup
            else:
                print("That doesn't look like a legal action to me")
        return curr_move

class RandOthelloState:
    '''A class to represent an othello game state'''

    def __init__(self, currentplayer, otherplayer, board_array = None, num_skips = 0):
        if board_array != None:
            self.board_array = board_array
        else:
            self.board_array = [[EMPTY] * SIZE for i in range(SIZE)]
            self.board_array[3][3] = WHITE
            self.board_array[4][4] = WHITE
            self.board_array[3][4] = BLACK
            self.board_array[4][3] = BLACK
            x1 = random.randrange(8)
            x2 = random.randrange(8)
            self.board_array[x1][0] = BLOCKED
            self.board_array[x2][7] = BLOCKED
        self.num_skips = num_skips
        self.current = currentplayer
        self.other = otherplayer


def player(state):
    return state.current

def actions(state):
    '''Return a list of possible actions given the current state
    How?
    Checks if result(state, (i, j))! = None
    '''
    legal_actions = []
    for i in range(SIZE):
        for j in range(SIZE):
            if result(state, (i,j)) != None:
                legal_actions.append((i,j))
    if len(legal_actions) == 0:
        legal_actions.append(SKIP)
    return legal_actions

def result(state, action):
    '''Returns the resulting state after taking the given action

    (This is the workhorse function for checking legal moves as well as making moves)

    If the given action is not legal, returns None

    '''
    # first, special case! an action of SKIP is allowed if the current agent has no legal moves
    # in this case, we just skip to the other player's turn but keep the same board
    '''
    If the action is "SKIP", then the person is skipping their turn.
    New State = State with playing player swapped and board remains same, skips += 1 
    '''
    if action == SKIP:
        newstate = RandOthelloState(state.other, state.current, copy.deepcopy(state.board_array), state.num_skips + 1)
        return newstate

    '''
    If the move is done on the board, which is non-empty: that move is illegal
    return None
    '''
    if state.board_array[action[0]][action[1]] != EMPTY:
        return None

    '''
    If all the above is false:
        It creates a New State with players swapped, copy the board
        The selected place is updated with the color 
    '''
    color = state.current.get_color()
    # create new state with players swapped and a copy of the current board
    newstate = RandOthelloState(state.other, state.current, copy.deepcopy(state.board_array))

    newstate.board_array[action[0]][action[1]] = color
    
    flipped = False
    # Directions is the list of tuples
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    for d in directions:
        i = 1
        count = 0
        while i <= SIZE:
            x = action[0] + i * d[0]
            y = action[1] + i * d[1]
            if x < 0 or x >= SIZE or y < 0 or y >= SIZE:
                count = 0
                break
            elif newstate.board_array[x][y] == -1 * color:
                count += 1
            elif newstate.board_array[x][y] == color:
                break
            else:
                count = 0
                break
            i += 1

        if count > 0:
            flipped = True

        for i in range(count):
            x = action[0] + (i+1) * d[0]
            y = action[1] + (i+1) * d[1]
            newstate.board_array[x][y] = color

    if flipped:
        return newstate
    else:  
        # if no pieces are flipped, it's not a legal move
        return None

def terminal_test(state):
    '''Simple terminal test
    '''
    # if both players have skipped
    if state.num_skips == 2:
        return True

    # if there are no empty spaces
    empty_count = 0
    for i in range(SIZE):
        for j in range(SIZE):
            if state.board_array[i][j] == EMPTY:
                empty_count += 1
    if empty_count == 0:
        return True
    return False

def display(state):
    '''Displays the current state in the terminal window
    '''
    print('  ', end='')
    for i in range(SIZE):
        print(i,end='')
    print()
    for i in range(SIZE):
        print(i, '', end='')
        for j in range(SIZE):
            if state.board_array[j][i] == WHITE:
                print('W', end='')
            elif state.board_array[j][i] == BLACK:
                print('B', end='')
            elif state.board_array[j][i] == BLOCKED:
                print('X', end='')
            else:
                print('-', end='')
        print()

def display_final(state):
    '''Displays the score and declares a winner (or tie)
    '''
    wcount = 0
    bcount = 0
    for i in range(SIZE):
        for j in range(SIZE):
            if state.board_array[i][j] == WHITE:
                wcount += 1
            elif state.board_array[i][j] == BLACK:
                bcount += 1

    print("Black: " + str(bcount))
    print("White: " + str(wcount))
    if wcount > bcount:
        print("White wins")
    elif wcount < bcount:
        print("Black wins")
    else:
        print("Tie")

def play_game(p1 = None, p2 = None):
    '''Plays a game with two players. By default, uses two humans
    '''
    if p1 == None:
        p1 = HumanPlayer(BLACK)
        # p1 = RandomPlayer(BLACK)
    if p2 == None:
        p2 = HumanPlayer(WHITE)

    s = RandOthelloState(p1, p2)
    while True:
        action = p1.make_move(s)
        print("White Action, " ,action)
        if action not in actions(s):
            print("Illegal move made by Black")
            print("White wins!")
            return
        s = result(s, action)
        if terminal_test(s):
            print("Game Over")
            display(s)
            display_final(s)
            return
        # print("State at Rand:")
        action = p2.make_move(s)
        print("Black Action, ", action)
        if action not in actions(s):
            print("Illegal move made by White")
            print("Black wins!")
            return
        s = result(s, action)
        if terminal_test(s):
            print("Game Over")
            display(s)
            display_final(s)
            return


def main():
    print("AlphaBeta is Black and RandomPlayer is White")
    play_game(p1 = AlphabetaPlayer(BLACK, 4), p2 = RandomPlayer(WHITE))
    print("AlphaBeta is White and RandomPlayer is Black")
    play_game(p1=RandomPlayer(BLACK), p2=AlphabetaPlayer(WHITE, 4))


if __name__ == '__main__':
    main()
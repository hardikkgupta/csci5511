import copy
import random
import math

class Node:

    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def next_step(self):
        n_list = []
        # print(self.state)
        for key in (self.state).keys():
            for g in range(3):
                for i in range(g + 1, 3):
                    for j in range(4):
                        for k in range(4):
                            copy_dict = copy.deepcopy(self.state)
                            copy_dict[key][g][k], copy_dict[key][i][k] = copy_dict[key][i][k], copy_dict[key][g][k]
                            n_list.append(copy_dict)
        return n_list

# Matrix Build which gives each game between each player
def matrix_build(schedule_dict):
    # Prepares a matrix with rows and columns of players and have entries as matches played between them
    matchup_count = {player: {opponent: 0 for opponent in players if opponent != player} for player in schedule_dict.keys()}
    def update_matchup_count(players_in_game):
        for player1 in players_in_game:
            for player2 in players_in_game:
                if player1 != player2:
                    matchup_count[player1][player2] += 1
    for week_game in schedule_dict.values():
        for match in week_game:
            update_matchup_count(match)
    return matchup_count
# print(matchup_count)

# Count the number of zeros in matchup_count
def count_zeros(matchup_count):
    count = 0
    for key in matchup_count.keys():
        for set in matchup_count[key]:
            if matchup_count[key][set] == 0:
                count += 1
    return (count*1000)
# print(count)

# Give length of copied configurations of each match
def unique_lists(schedule_dict):
    lists = []
    for key in schedule_dict.keys():
        for match in schedule_dict[key]:
            lists.append(match)
    unique_lists = set(tuple(sorted(lst)) for lst in lists)
    return (39 - (len(unique_lists)))*100

def maxValue(matchup_count):
    max = 0
    min = 100
    sum = 100
    for key, value in matchup_count.items():
        for k,curr in value.items():
            sum += math.pow(curr,2)

    return math.sqrt(sum)

def valued(schedule_dict):
    countzeros = count_zeros(matrix_build(schedule_dict))
    rep_value = unique_lists(schedule_dict)
    max_value = maxValue(matrix_build(schedule_dict))
    return countzeros + rep_value + max_value



def hill_climbing(problem):
    current = problem
    current_value = valued(problem)
    # i = 100
    while True:
        # i -= 1
        prob = Node(current)
        # print(prob)
        neighbors = prob.next_step()
        neighbor_value = [valued(x) for x in neighbors]
        min_value, index = min([value, index] for index, value in enumerate(neighbor_value))
        # print(f"Index of minimum: {index}")
        # print(f"Minimum value is: {min_value}")
        # print(f'Len of neighbours: {len(neighbors)}')
        if not neighbors:
            return current

        if min_value < current_value:
            current = neighbors[index]
            current_value = valued(current)
            # print(current_value)
            # print(i)
        else:
            return current

# Initialization
players = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
schedule_dict = {}
for bye_player in players:
    # Prepare a new list removing the bye player (12 - member)
    new_players = [player for player in players if player != bye_player]
    # Prepare a lists of tuple acting like a schedule for a week
    schedule = [list(new_players[i:i + 4]) for i in range(0, len(new_players), 4)]
    schedule_dict[bye_player] = schedule

def simulated_annealing(problem):
    current = problem
    v = 1000
    for t in range(v + 1):
        # print("this is t: ",t)
        prob1 = Node(current)
        T = v - t
        if T == 0:
            return current
        neighbors = prob1.next_step()
        neighbor_value = [1/valued(x) for x in neighbors]
        if not neighbors:
            return current
        next_choice = random.choices(neighbors, neighbor_value)[0]
        delta_e = valued(next_choice) - valued(current)
        if delta_e < 0 or random.random() < math.pow(2.7,delta_e / T):
            current = next_choice
    return current


schedule_dict = Node(schedule_dict)
schedule_dict1 = schedule_dict
best = hill_climbing(schedule_dict.state)

print("**** Final result from Hill-Climbing ****")
for key in best.keys():
        print("Bye for Player ", key, ": ",best[key])

print("**** Replay Summary from Hill-Climbing ****")
# print(matrix_build(best))
replay = matrix_build(best)
for key in replay:
    print(key, ": ", replay[key])

best1 = simulated_annealing(schedule_dict1.state)
print("**** Final result from Simulated-Annealing ****")
for key in best1.keys():
        print("Bye for Player ", key, ": ",best1[key])

print("**** Replay Summary from Simulated-Annealing ****")
# print(matrix_build(best))
replay = matrix_build(best1)
for key in replay:
    print(key, ": ", replay[key])

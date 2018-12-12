from collections import deque

class Plants:
    def __init__(self, state, grow_rules, death_rules):
        self.state = state
        self.grow_rules = grow_rules
        self.death_rules = death_rules
        self.shift_spaces = 0

    def evolve(self):
        self.shift_spaces += 2
        self.state = [0, 0] + self.state + [0, 0, 0]
        next_state = [0, 0]
        pot = 0
        while pot <= len(self.state) - 5:
            if self.state[pot:pot + 5] in self.grow_rules:
                next_state.append(1)
            else:
                next_state.append(0)
            pot += 1
        self.state = next_state + [0, 0, 0]

    def plant_value(self):
        values = list()
        values += list(map(lambda x: x * -1, range(self.shift_spaces, 0, -1)))
        values += list(range(len(self.state) - self.shift_spaces))
        return sum([x for x, y in zip(values, self.state) if y == 1])


def day12(inputs):
    state = hash_to_bin(inputs[0].split(':')[1].strip(' '))
    grow_rules = list()
    death_rules = list()
    for i in inputs[2:]:
        if i[-1] == '#':
            grow_rules.append(hash_to_bin(i.split(' => ')[0]))
        elif i[-1] == '.':
            death_rules.append(hash_to_bin(i.split(' => ')[0]))
    plants = Plants(state, grow_rules, death_rules)
    for _ in range(20):
        plants.evolve()
    answer_1 = plants.plant_value()
    # for i in range(50000000000 - 20):
    #     if i % 1000 == 0:
    #         print(i)
    #     plants.evolve()
    answer_2 = plants.plant_value()

    return answer_1, answer_2


def hash_to_bin(state):
    state_array = list()
    char_map = {'#': 1, '.': 0}
    for s in state:
        state_array.append(char_map[s])
    return state_array

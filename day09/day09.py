from itertools import cycle


class Game:
    def __init__(self, players, turns):
        self.players = players
        self.scores = self._init_scores()
        self.turns = turns
        self.current_marble_location = 0
        self.state = [0]

    def _init_scores(self):
        scores = dict()
        for i in range(self.players):
            scores[i+1] = 0
        return scores

    def add(self, player, turn):
        # print(player, turn)
        if turn % 23 == 0 and turn != 0:
            pop_location = self.current_marble_location - 7 if self.current_marble_location > 6 else len(self.state) - abs(self.current_marble_location - 7)
            # print(player, turn, pop_location)
            self.scores[player] += turn + self.state.pop(pop_location)
            self.current_marble_location = pop_location if pop_location <= len(self.state) else 0
        else:
            if self.current_marble_location < len(self.state) - 2:
                self.state.insert(self.current_marble_location + 2, turn)
                self.current_marble_location += 2
            elif self.current_marble_location == len(self.state) - 2:
                self.state.append(turn)
                self.current_marble_location += 2
            else:
                self.state.insert(1, turn)
                self.current_marble_location = 1
        # print(self.state)


def day09(players, turns):
    player = cycle(range(1, players + 1))

    game = Game(players, turns)
    for turn in range(1, turns + 1):
        if turn % 1000 == 0:
            print('.', end='', flush=True)
        game.add(next(player), turn)
    # print(game.scores)
    ret = sorted(game.scores.items(), key=lambda x: x[1], reverse=True)
    return ret[0][1]


if __name__ == "__main__":
    print(day09(404, 7185200))

import random
from abc import ABC, abstractmethod


class Strategy(ABC):
    name = ""

    @abstractmethod
    def pass_the_ball(self, formation):
        pass


class TikiTaka(Strategy):
    name = "TikiTaka"

    def pass_the_ball(self, formation):
        defenders = formation[0]
        midfielder_forwards = [*formation[1], *formation[2]]

        random.shuffle(defenders)
        random.shuffle(midfielder_forwards)
        return [*defenders, *midfielder_forwards]


class CounterAttack(Strategy):
    name = "CounterAttack"

    def pass_the_ball(self, formation):
        defenders = random.choice(formation[0])
        midfielders = random.choice(formation[1])
        forwards = random.choice(formation[2])
        return [defenders, midfielders, forwards]


class FootballClub:
    def __init__(self, strategy):
        self._strategy = strategy

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        self._strategy = strategy

    def attack(self):
        formation = [
            ["LB", "CB", "CB", "CB"],
            ["LCM", "CDM", "RCM"],
            ["LW", "CF", "RW"],
        ]
        result = self._strategy.pass_the_ball(formation)
        result.append("GOAAAALLL!!!")
        print(" >> ".join(result))


if __name__ == "__main__":
    strategy = CounterAttack()
    football_club = FootballClub(strategy)
    print(f"Manager: Hey team! apply {strategy.name}")
    football_club.attack()

    strategy = TikiTaka()
    print(f"Manager: Hey team! apply {strategy.name}")
    football_club.strategy = strategy
    football_club.attack()

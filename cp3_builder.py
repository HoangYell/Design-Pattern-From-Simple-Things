from abc import abstractmethod


class Builder:
    @property
    @abstractmethod
    def house(self):
        pass

    @abstractmethod
    def build_roof(self):
        pass

    @abstractmethod
    def build_ground_floor(self):
        pass

    @abstractmethod
    def build_first_floor(self):
        pass


class NormalHouseBuilder(Builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._house = NormalHouse()

    @property
    def house(self):
        house = self._house
        self.reset()
        return house

    def build_roof(self):
        roof = "^"
        self._house.add(roof)

    def build_ground_floor(self):
        ground = "U"
        self._house.add(ground)

    def build_first_floor(self):
        first_floor = "O"
        self._house.add(first_floor)


class NormalHouse:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def show_off(self):
        print("\n".join(self.parts[::-1]))


class Director:
    def __init__(self, builder):
        self.builder = builder

    def build_simple_house(self):
        self.builder.build_ground_floor()
        self.builder.build_roof()

    def build_advanced_house(self):
        self.builder.build_ground_floor()
        self.builder.build_first_floor()
        self.builder.build_roof()


if __name__ == "__main__":
    builder = NormalHouseBuilder()
    builder.build_ground_floor()
    builder.build_first_floor()
    builder.house.show_off()
    print("--")
    director = Director(builder)
    director.build_simple_house()
    builder.house.show_off()
    print("--")
    director.build_advanced_house()
    builder.house.show_off()

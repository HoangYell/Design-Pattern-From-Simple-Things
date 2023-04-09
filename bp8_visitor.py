from abc import abstractmethod


class NorthKorea:
    def __init__(self):
        self.secret = None

    @abstractmethod
    def accept(self, visitor):
        pass


class NuclearFacility(NorthKorea):
    def __init__(self):
        self.secret = "North Korea tests nuclear drones and builds uranium facility."

    def accept(self, visitor):
        visitor.visit(self)


class MilitaryBase(NorthKorea):
    def __init__(self):
        self.secret = "North Korea hides 16 missile bases and builds new one."

    def accept(self, visitor):
        visitor.visit(self)


class Spy:
    def __init__(self):
        self.diary = []

    def visit(self, location):
        if isinstance(location, NuclearFacility):
            self.diary.append(location.secret)
        elif isinstance(location, MilitaryBase):
            self.diary.append(location.secret)


# Example usage
if __name__ == "__main__":
    locations = [NuclearFacility(), MilitaryBase()]
    spy = Spy()
    for location in locations:
        location.accept(spy)
    print(spy.diary)

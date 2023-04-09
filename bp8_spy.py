class NorthKorea:
    def __init__(self):
        self.secret = None

    def accept(self, visitor):
        visitor.visit(self)


class NuclearFacility(NorthKorea):
    def __init__(self):
        self.secret = "North Korea tests nuclear drones and builds uranium facility."


class MilitaryBase(NorthKorea):
    def __init__(self):
        self.secret = "North Korea hides 16 missile bases and builds new one."


class Spy:
    def __init__(self):
        self.diary = []

    def visit(self, location):
        self.diary.append(location.secret)


# Example usage
if __name__ == "__main__":
    locations = [NuclearFacility(), MilitaryBase()]
    spy = Spy()
    for location in locations:
        location.accept(spy)
    print(spy.diary)

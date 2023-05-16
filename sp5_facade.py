# Subsystem classes
class Elevator:
    def move(self, floor):
        print(f"Moving to floor {floor}...")


class Security:
    def check(self, id):
        print(f"Checking id {id}...")
        return True


class Reception:
    def greet(self, name):
        print(f"Hello {name}, welcome to our building!")


# Facade class
class BuildingFacade:
    def __init__(self):
        self.elevator = Elevator()
        self.security = Security()
        self.reception = Reception()

    def enter(self, id, name, floor):
        if self.security.check(id):
            self.reception.greet(name)
            self.elevator.move(floor)


if __name__ == "__main__":
    building = BuildingFacade()
    building.enter(1234, "Nancy", 5)

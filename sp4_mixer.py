class Dog:
    # Abstraction
    def __init__(self, coat):
        # Reference to an object of type Coat
        self.coat = coat

    def bark(self):
        pass

    def shed(self):
        # Delegate to the Coat object
        self.coat.shed()


class Labrador(Dog):
    # Refined Abstraction
    def bark(self):
        print("The labrador barks loudly.")


class Poodle(Dog):
    # Refined Abstraction
    def bark(self):
        print("The poodle barks softly.")


class Coat:
    # Implementer
    def shed(self):
        # Abstract method
        pass


class Curly(Coat):
    # Concrete Implementation
    def shed(self):
        print("The curly coat sheds little hair.")


class Straight(Coat):
    # Concrete Implementation
    def shed(self):
        print("The straight coat sheds moderate hair.")


if __name__ == "__main__":
    # Create a labrador with a straight coat
    lab_straight = Labrador(Straight())
    lab_straight.bark()
    lab_straight.shed()

    # Create a poodle with a curly coat
    poo_curly = Poodle(Curly())
    poo_curly.bark()
    poo_curly.shed()

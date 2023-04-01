from abc import ABC, abstractmethod


class Volkswagen(ABC):
    """The Abstract Class defines a template method that contains a skeleton of
    some algorithm, composed of calls to (usually) abstract primitive operations.

    Concrete subclasses should implement these operations, but leave the template
    method itself intact.
    """

    def manufacture_car(self) -> None:
        """The template method defines the skeleton of an algorithm."""
        self.install_engine()
        self.assemble_chassis()
        self.paint_body()

    @abstractmethod
    def install_engine(self) -> None:
        pass

    def assemble_chassis(self) -> None:
        print("Assembling a Volkswagen chassis")

    def paint_body(self) -> None:
        print("Painting the body with Volkswagen color")


class Lamborghini(Volkswagen):
    def install_engine(self) -> None:
        print("Installing a powerful and loud engine")

    def assemble_chassis(self) -> None:
        print("Assembling a lightweight and aerodynamic chassis")


class Porsche(Volkswagen):
    def install_engine(self) -> None:
        print("Installing a fast and smooth engine")


if __name__ == "__main__":
    print("Manufacturing Lamborghini:")
    lamborghini = Lamborghini()
    lamborghini.manufacture_car()
    print("\n")

    print("Manufacturing Porsche:")
    porsche = Porsche()
    porsche.manufacture_car()

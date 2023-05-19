class Plane:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def get_flight_distance(self, speed, time):
        flight_distance = speed * time
        return flight_distance


class PlaneFactory:
    def __init__(self):
        self.plane_pool = {}
        self.color = {"Boeing 747": "white", "Airbus A380": "blue"}

    def get_plane(self, model):
        if model not in self.plane_pool:
            color = self.color.get(model, "gray")
            plane = Plane(model, color)
            self.plane_pool[model] = plane
        else:
            plane = self.plane_pool[model]
        return plane


if __name__ == "__main__":
    factory = PlaneFactory()

    white_plane = factory.get_plane("Boeing 747")
    blue_plane = factory.get_plane("Airbus A380")
    another_white_plane = factory.get_plane("Boeing 747")
    print(white_plane is another_white_plane)
    print(white_plane.color)
    print(blue_plane.color)
    print(white_plane.get_flight_distance(800, 10))
    print(blue_plane.get_flight_distance(900, 12))

import random
from abc import ABC, abstractmethod


class Handler(ABC):
    _next = None

    def set_next(self, handler):
        self._next = handler
        return handler

    def pass_to_next(self, data):
        return self._next.handle(data) if self._next else None

    @abstractmethod
    def handle(self, data):
        pass


class EAHandler(Handler):
    def handle(self, data):
        if "Gamer" in data:
            return f"EA: I'll hire this {data}"
        else:
            return self.pass_to_next(data)


class GoogleHandler(Handler):
    def handle(self, data):
        if "Python" in data:
            return f"Google: I'll hire this {data}"
        else:
            return self.pass_to_next(data)


class AmazonHandler(Handler):
    def handle(self, data):
        if "Java" in data:
            return f"Amazon: I'll hire this {data}"
        else:
            return self.pass_to_next(data)


class FacebookHandler(Handler):
    def handle(self, data):
        if random.choice([True, False]):
            return f"Facebook: I'll hire this {data}"
        else:
            return self.pass_to_next(data)


if __name__ == "__main__":
    ea = EAHandler()
    google = GoogleHandler()
    amazon = AmazonHandler()
    facebook = FacebookHandler()

    # build chain
    ea.set_next(google).set_next(amazon).set_next(facebook)

    devs = ["Python Dev", "Java Dev", "Golang Dev"]
    for dev in devs:
        print(f"\nWho wants a {dev}?")
        result = google.handle(dev)
        if result:
            print(f"  {result}", end="")
        else:
            print(f"  The {dev} failed all the interviews.", end="")

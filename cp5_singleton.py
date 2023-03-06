from threading import Lock
from time import sleep


class PhoneLineSingleton(type):
    _instances = {}
    _lock = Lock()

    def __call__(cls, *args, **kwargs):
        """
        __call__ is defined in this metaclass(SingletonMeta), not in the normal_class(Singleton) itself.
        When you create an instance of the Singleton class using Singleton(), Python internally calls the __call__ method of the SingletonMeta metaclass, not the __call__ method of the Singleton class.
        In this way, the __call__ method in the metaclass is used to control the creation of instances of the Singleton class, while the __call__ method in the Singleton class can be used for other purposes, if needed.
        This separation of concerns between the metaclass and the class itself is a key feature of the singleton pattern implementation in the given code. It allows us to enforce the singleton pattern without modifying the interface or behavior of the Singleton class itself.
        """
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class PhoneLine(metaclass=PhoneLineSingleton):
    def __init__(self):
        sleep(10)

    def talk(self):
        print(f"talking on the {id(self)} line")


# Example usage:
phone_line_1 = PhoneLine()
phone_line_2 = PhoneLine()

# Both objects refer to the same instance
phone_line_1.talk()
phone_line_2.talk()

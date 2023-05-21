import datetime
from abc import ABC, abstractmethod


class InternetAccess(ABC):
    @abstractmethod
    def grant_access(self):
        pass


class FreeInternetAccess(InternetAccess):
    def grant_access(self):
        print("Access granted. You can browse the free internet now!")


class CompanyProxyInternetAccess(InternetAccess):
    def __init__(self):
        self.free_internet_access = FreeInternetAccess()

    def grant_access(self):
        current_time = datetime.datetime.now().time()
        start_time = datetime.time(8, 0)
        end_time = datetime.time(17, 30)
        if start_time <= current_time <= end_time:
            print(
                "Sorry, access to the free internet is restricted during working hours!"
            )
        else:
            self.free_internet_access.grant_access()


if __name__ == "__main__":
    # current time is 9:00 AM
    origin = FreeInternetAccess()
    origin.grant_access()
    # current time is 6:00 PM
    proxy = CompanyProxyInternetAccess()
    proxy.grant_access()

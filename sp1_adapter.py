# Input 2: Having incompatible (non-USB type C) devices:
class Printer:
    name = "Printer"

    def connect_usb_b(self):
        return f"{self.name} is connected: Printing..."


# Input 2: Having incompatible (non-USB type C) devices:
class Flash:
    name = "Flash"

    def connect_usb_a(self):
        return f"{self.name} is connected: Copying..."


# Input 2: Having incompatible (non-USB type C) devices:
class Monitor:
    name = "Monitor"

    def connect_hdmi(self):
        return f"{self.name} is connected: Displaying..."


class Adapter:
    def __init__(self, obj, **adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        return getattr(self.obj, attr)


if __name__ == "__main__":
    devices = []
    printer = Printer()
    # Expected Output 1: Making that non-USB type C devices have USB type C port
    devices.append(Adapter(printer, connect=printer.connect_usb_b))
    flash = Flash()
    # Expected Output 1: Making that non-USB type C devices have USB type C port
    devices.append(Adapter(flash, connect=flash.connect_usb_a))
    monitor = Monitor()
    # Expected Output 1: Making that non-USB type C devices have USB type C port
    devices.append(Adapter(monitor, connect=monitor.connect_hdmi))
    for device in devices:
        # Expected Output 2: MacBook is able to connect to those incompatible devices
        print(device.connect())

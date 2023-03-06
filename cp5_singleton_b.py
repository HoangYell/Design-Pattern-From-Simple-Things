from time import sleep


class PhoneLine:
    def __init__(self):
        sleep(10)

    def talk(self):
        print(f"talking on the {id(self)} line")


class Employee:
    def __init__(self, phone_line):
        self.phone_line = phone_line

    def call_data_center(self):
        self.phone_line.talk()


# Example usage:
phone_line = PhoneLine()
employee1 = Employee(phone_line)
employee2 = Employee(phone_line)

# Both employees use the same phone line object but not the same instance
employee1.call_data_center()
employee2.call_data_center()

from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class NonSoldierCommand(Command):
    def __init__(self, payload):
        self._payload = payload

    def execute(self):
        print(f"    💣NonSoldierCommand.executing: ({self._payload})")


class SoldierCommand(Command):
    def __init__(self, soldier, resource):
        self._soldier = soldier
        self._resource = resource

    def execute(self):
        print(
            f"    💣SoldierCommand.executing: ({type(self._soldier)}, {self._resource})"
        )
        self._soldier.do_something(self._resource)


class Soldier:
    def do_something(self, resource):
        print(f"        Soldier.do_something with: ({resource})")


class Commander:
    _first_task = None
    _last_task = None

    def init_first_command(self, command):
        self._first_task = command

    def init_last_command(self, command):
        self._last_task = command

    def execute_main_command(self):
        print("Commander: the first task is:")
        if isinstance(self._first_task, Command):
            self._first_task.execute()

        print("Commander: the main task is:")
        print(f"    🧨Commander.executing: (Resource for the Main Task)")

        print("Commander: the last task is:")
        if isinstance(self._last_task, Command):
            self._last_task.execute()


if __name__ == "__main__":
    commander = Commander()

    # commander init: a command encapsulating needed information(resource) to execute the task at a later time.
    non_soldier_command = NonSoldierCommand("Resource for the First Task")
    commander.init_first_command(non_soldier_command)

    # commander init: a command encapsulating needed information(soldier, resource) to execute the task at a later time.
    soldier = Soldier()
    soldier_command = SoldierCommand(soldier, "Resource for the Last Task")
    commander.init_last_command(soldier_command)

    # after planning, this is the later time, time to execute the tasks initiated by the commander
    commander.execute_main_command()

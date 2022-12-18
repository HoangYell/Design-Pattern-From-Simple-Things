import copy


class MemoryRobot:
    def __init__(self):
        self.who_am_i = None

    def set_memory(self, who_am_i):
        self.who_am_i = who_am_i


class Robot:
    def __init__(self, age, body_parts, memory):
        self.age = age
        self.body_parts = body_parts
        self.memory = memory

    @property
    def id(self):
        # https://www.digitalocean.com/community/tutorials/python-id
        return str(id(self))[-3:]


if __name__ == "__main__":

    def init_robot():
        robot_body_parts = [
            "head",
            {"left hand", "chest", "right hand"},
            ["left foot", "butt", "right foot"],
        ]
        memory_robot = MemoryRobot()
        robot = Robot(18, robot_body_parts, memory_robot)
        memory_robot.set_memory(robot)
        return robot

    def copy_robot(origin_robot, copy_method):
        wing = "wing"
        tail = "tail"
        tab = "    "
        tab_2 = "    " * 2
        tab_3 = "    " * 3
        print(f"\nCoping by {copy_method.__name__}:")
        copied_robot = copy_method(origin_robot)
        copied_robot.body_parts.append(tail)
        is_origin_robot_changed = origin_robot.body_parts[-1] == tail
        print(f"{tab}Question: update copied_robot changes origin_robot?")
        print(f"{tab_2}Answer: {is_origin_robot_changed}")

        origin_robot.body_parts[1].add(wing)
        is_copied_robot_changed = wing in copied_robot.body_parts[1]
        print(f"{tab}Question: update origin_robot changes copied_robot?")
        print(f"{tab_2}Answer: {is_copied_robot_changed}")

        print(f"{tab}How about reference?")
        print(f"{tab_2}origin_robot's reference:")
        print(f"{tab_3}{origin_robot.id} is the ID of origin_robot")
        print(
            f"{tab_3}{origin_robot.memory.who_am_i.id} is the ID of origin_robot.memory.who_am_i"
        )
        print(f"{tab_2}copied_robot's reference:")
        print(f"{tab_3}{copied_robot.id} is the ID of copied_robot")
        print(
            f"{tab_3}{copied_robot.memory.who_am_i.id} is the ID of copied_robot.memory.who_am_i"
        )
        return copied_robot

    origin_robot_1 = init_robot()
    shallow_copied_robot = copy_robot(origin_robot_1, copy.copy)

    origin_robot_2 = init_robot()
    deep_copied_robot = copy_robot(origin_robot_2, copy.deepcopy)

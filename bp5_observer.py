from __future__ import annotations

from abc import ABC, abstractmethod


class Teacher:
    """A class that represents a teacher who can change their state and notify their students."""

    def __init__(self) -> None:
        self._state: str = None
        self._students: list[Student] = []

    @property
    def state(self) -> str:
        return self._state

    @state.setter
    def state(self, value: str) -> None:
        self._state = value

    @property
    def students(self) -> list[Student]:
        return self._students

    def attach(self, student: Student) -> None:
        """Add a new student to the list of observers."""
        print(f"Teacher said: Hello new student '{id(student)}' to my class")
        self.students.append(student)

    def detach(self, student: Student) -> None:
        """Remove a student from the list of observers."""
        print(f"Teacher said: GoodBye student '{id(student)}'")
        self.students.remove(student)

    def notify_students(self) -> None:
        """Notify all the students about the current state of the teacher."""
        print(f"- TEACHER ACT: I'm {self.state}")
        for student in self.students:
            student.react(self)

    def act(self, action: str) -> None:
        """Change the state of the teacher and notify the students."""
        self.state = action
        self.notify_students()


class Student(ABC):
    """An abstract class that represents a student who can react to a teacher's state."""

    @abstractmethod
    def react(self, teacher: Teacher) -> None:
        pass


class BadStudent(Student):
    """A class that represents a bad student who gossips when the teacher goes out."""

    def react(self, teacher: Teacher) -> None:
        if teacher.state == "going out":
            print(f"  - BAD_STUDENT REACT: 😃 I'm gossiping in the class")
        else:
            print(f"  - BAD_STUDENT REACT: I don't care!")


class GoodStudent(Student):
    """A class that represents a good student who focuses when the teacher speaks."""

    def react(self, teacher: Teacher) -> None:
        if teacher.state == "speaking":
            print(f"  - GOOD_STUDENT REACT: 😃 I'm focusing on what the teacher says")
        else:
            print(f"  - GOOD_STUDENT REACT: I don't care!")


if __name__ == "__main__":
    # Create a teacher object
    teacher = Teacher()

    # Create two student objects
    bad_student = BadStudent()
    good_student = GoodStudent()

    # Attach both students to observe the teacher
    teacher.attach(bad_student)
    teacher.attach(good_student)

    # Perform some actions as a teacher
    teacher.act("replying husband's SMS")
    teacher.act("going out")
    teacher.act("speaking")

    # Detach one student from observing the teacher
    teacher.detach(bad_student)

    # Perform another action as a teacher
    teacher.act("going out")

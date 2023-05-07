class Student:
    def __init__(self, name):
        self.name = name
        self.loudspeaker = None

    def speak(self, message):
        self.loudspeaker.broadcast(message, self)

    def listen(self, message, sender):
        print(f'{self.name} hears {sender.name} say: "{message}".')


class LoudSpeaker:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        student.loudspeaker = self
        self.students.append(student)

    def broadcast(self, message, sender):
        for student in self.students:
            if student != sender:
                student.listen(message, sender)


if __name__ == "__main__":
    loudspeaker = LoudSpeaker()

    guido = Student("Guido van Rossum")
    linus = Student("Linus Torvald")
    elon = Student("Elon Musk")

    loudspeaker.add_student(guido)
    loudspeaker.add_student(linus)
    loudspeaker.add_student(elon)

    guido.speak("Talk is cheap. Show me the code.")
    linus.speak("Software is like sex: It’s better when it’s free.")

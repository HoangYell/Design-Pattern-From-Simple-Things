# File class for saving the file data
class File:
    def __init__(self, content):
        self._content = content

    # Make the content attribute read-only
    @property
    def content(self):
        return self._content

    # Define how the file object is printed
    def __str__(self):
        return self.content


# Photoshop class for editing images
class Photoshop:
    def __init__(self):
        self._content = ""

    # Make the content attribute read-only
    @property
    def content(self):
        return self._content

    # Edit the image by adding some text
    def edit(self, text):
        self._content += text

    # Save the current state of the image inside a file
    def save(self):
        return File(self.content)

    # Load the previous state of the image from a file
    def load(self, file):
        self._content = file.content

    # Define how the photoshop object is printed
    def __str__(self):
        return self.content


# SSDStorage class for managing files
class SSDStorage:
    def __init__(self):
        self.file_history = []

    # Save a file to the history list
    def save(self, file):
        self.file_history.append(file)

    # Get the last file from the history list and remove it
    def pop_previous_file(self):
        try:
            return self.file_history.pop()
        except IndexError:
            print("No more files to pop.")
            return None


if __name__ == "__main__":
    ssd_storage = SSDStorage()
    photoshop = Photoshop()

    photoshop.edit("Red")
    _file = photoshop.save()
    ssd_storage.save(_file)

    photoshop.edit("Green")
    _file = photoshop.save()
    ssd_storage.save(_file)

    photoshop.edit("Blue")
    _file = photoshop.save()
    ssd_storage.save(_file)

    print(f"Current: {photoshop}")  # Current: RedGreenBlue

    _file = ssd_storage.pop_previous_file()
    photoshop.load(_file)
    print(f"Undo: {photoshop}")  # Undo: RedGreen

    _file = ssd_storage.pop_previous_file()
    photoshop.load(_file)
    print(f"Undo: {photoshop}")  # Undo: Red


class Conditional:
    def __init__(self, value=0):
        self.value = value

    def isEven(self):
        return self.value % 2 == 0

    def isOdd(self):
        return self.value % 2 == 1

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

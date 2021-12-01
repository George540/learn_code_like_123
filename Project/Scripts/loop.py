
class Loop:
    def __init__(self):
        self.count = 1

    def checkcondition(self):
        if self.getcounter() <= self.getEnd():
            self.increment()
            return True
        else:
            return False
        
    def increment(self):
        self.count += 1

    def getcounter(self):
        return self.count

    def getEnd(self):
        return self.end
    
    def setEnd(self, num):
        if num <= 1 :
            print('Invalid loop times!')
        else:
            self.end=num

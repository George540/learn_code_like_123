
class Loop:
    def __init__(self):
        pass

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

    def setcounter(self):
        self.count=1

    def getEnd(self):
        return self.end
    
    def setEnd(self, num):
        #if num<0 :
        #    print('Invalid loop times!')
        #else:
        self.end=int(num)


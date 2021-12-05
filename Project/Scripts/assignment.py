class Assignment:
    def __init__(self, variables: dict = {}):
        self.variables = variables

    def setVariable(self, name, value):
        self.variables[name] = value

    def deleteVariable(self, name):
        del self.variables[name]

    def getVariable(self, name):
        try:
            return self.variables[name]
        except KeyError:
            print("No such value in dictionary")
            return None
    
    def getKeyValuePair(self, name):
        return (name, self.getVariable(name))
class Assignment:
    def __init__(self, variables: dict = {}):
        self.variables = variables

    def setVariable(self, name : str, value):
        self.variables[name] = value

    def deleteVariable(self, name : str):
        del self.variables[name]

    def getVariable(self, name : str):
        try:
            return self.variables[name]
        except KeyError:
            print("No such value in dictionary")
            return None
    
    def getKeyValuePair(self, name):
        return (name, self.getVariable(name))
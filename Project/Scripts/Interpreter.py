class Interpreter:
    # Constructor:
    def __init__(self, cur_sent="", cur_claus=[]):
        self.current_sentense = cur_sent
        self.current_clauses = cur_claus

    # Sentense Accessor
    # return type: string
    def getCurrentSentense(self):
        return self.current_sentense

    # Sentense Mutator
    # return type: void
    def setCurrentSentence(self, s):
        self.current_sentense = s

    # Current Clauses Accessor
    # return type: list of strings
    def getCurrentClauses(self):
        return self.current_clauses

    # Current Clauses Mutator
    # return type: void
    def setCurrentClauses(self, clauses):
        self.current_clauses = clauses

    # Splits string sentense with the comma-space delimiter
    # return type: void
    def splitSentense(self):
        clauses =  self.current_sentense.split(", ")
        self.current_clauses = clauses
    
    # Splits string clause with the space delimiter
    # return type: list of strings
    def splitClause(self, c):
        return c.split(" ")
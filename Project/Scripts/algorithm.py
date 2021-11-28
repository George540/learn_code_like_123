import calculate
# import loop
# import conditional

calculate = calculate.Calculate()
# loop = loop.Loop()
# conditional = conditional.Conditional()

# some global declared in driver, we will need to import
VARIABLES = {'X': 10, 'Y': 5} # JUST AN EXAMPLE

class Algorithm:
    def __init__(self, curr_words=[], vals=[], result=0):
        self.curr_words = curr_words    # list of strings
        self.values = vals              # list of values (at most 2)
        self.result = result
    
    def getCurr_words(self):
        return self.curr_words

    def setCurr_words(self, word):
        self.curr_words.append(word)

    def getValues(self):
        return self.values
    
    def setValues(self, val):
        self.values.append(val)
    
    def resetValues(self):
        self.values = []
        
    def getResult(self):
        return self.result
    
    def setResult(self, result):
        self.result = result


    def isVariable(self, string):
        # in the case the string is a digit
        if string.isdigit() == True:
            self.convertStringToFloat(string)
        # in the case the string is not a digit
        else:
            check = self.doesVariableExist(string)
            if check == False:
                # we must stop execution because we are trying to access a variable that has not been initialized
                print('VARIABLE NOT DEFINED! PLEASE ENTER A NEW SENTENCE OR DEFINE ' + string)

    def doesVariableExist(self, word):
        # in the case the variable exists, return the value
        if word in VARIABLES:
            self.getVariableValue(word)
            return True
        # in the case the variable DOES NOT exist, we terminate
        else:
            return False

    def getVariableValue(self, key):
        self.setValues(VARIABLES[key]) 

    def convertStringToFloat(self, word):
        self.setValues(int(word)) 

# the cases:
# 1. string is digit, we convert to float and store value
# 2. string is a variable, and doesn't exist, we terminate execution and prompt for re-entry
# 3. string is a variable, and does exist, we store value at that key
# ...

# originally, we wanted to directly call each class, but i dont was to repeat this process twice
# we are already checking here so, unless each class will handle determining which function to call,
# it was only calculate which had a helper function so idk

# also indexing is at risk of getting fucked, depending on interpreter class, right now im thinking
        # wasn't sure how we are defining loop
        # iterate? loop? '10' times?
# curr_words = ['add', '10', 'and', '2']
# curr_words = ['subtract', '5', 'and', '7']
# curr_words = ['square 'root', '144']
# curr_words = ['is 'X', 'odd']
# curr_words = ['add '5', '10', 'times']

    def findAlgorithm(self):
        if self.curr_words[0].lower() == 'add':
            # WE NEED TO MODIFY LOOP CLASS, ADD A METHOD
            # WE ASSUME START IS ALWAYS 1
            # if self.curr_words[-1].lower() == 'times':
            #     # make sure our end value is a positive integer
            #     loop.checkCondition(self.values[1])
            #     # loop.increment( # pass through calculate function call  )
            # else:    
            #     self.result = calculate.add(self.values[0], self.values[1])
            self.result = calculate.add(self.values[0], self.values[1])
        elif self.curr_words[0].lower() == 'subtract':
            # if self.curr_words[-1].lower() == 'times':
            #     # make sure our end value is a positive integer
            #     loop.checkCondition(self.values[1])
            #     # loop.increment( # pass through calculate function call  )
            # else:    
            #     self.result = calculate.subtract(self.values[0], self.values[1])
            self.result = calculate.subtract(self.values[0], self.values[1])
        elif self.curr_words[0].lower() == 'multiply':
            # if self.curr_words[-1].lower() == 'times':
            #     # make sure our end value is a positive integer
            #     loop.checkCondition(self.values[1])
            #     # loop.increment( # pass through calculate function call  )
            # else:    
            #     self.result = calculate.multiply(self.values[0], self.values[1])
            self.result = calculate.divide(self.values[0], self.values[1])
        elif self.curr_words[0].lower() == 'divide':
            # if self.curr_words[-1].lower() == 'times':
            #     # make sure our end value is a positive integer
            #     loop.checkCondition(self.values[1])
            #     # loop.increment( # pass through calculate function call  )
            # else:    
            #     self.result = calculate.divide(self.values[0], self.values[1])
            self.result = calculate.divide(self.values[0], self.values[1])
        # will this be parsed as 2 seperate words?
        elif self.curr_words[0].lower() == 'square root':
            self.result = calculate.squareRoot(self.values[0])
        # elif self.curr_words[-1].lower() == 'odd':
        #     self.result = conditional.isOdd()
        # elif self.curr_words[-1].lower() == 'even':
        #     self.result = conditional.isEven()

algo = Algorithm(curr_words=['Add', '5', 'to', '10'])
algo.resetValues()
print("Intial algorithm values: " , algo.getValues())
algo.isVariable(algo.curr_words[1])
algo.isVariable(algo.curr_words[3])
print("Updated algorithm values: " , algo.getValues())
algo.findAlgorithm()
print("Result : ", algo.getResult())
###########################################################################################
algo = Algorithm(curr_words=['Square root', '144'])
algo.resetValues()
print("Intial algorithm values: " , algo.getValues())
algo.isVariable(algo.curr_words[1])
print("Updated algorithm values: " , algo.getValues())
algo.findAlgorithm()
print("Result : ", algo.getResult())
###########################################################################################
# ASSUMING X = 10
algo = Algorithm(curr_words=['Square root', 'X'])
algo.resetValues()
print("Intial algorithm values: " , algo.getValues())
algo.isVariable(algo.curr_words[1])
print("Updated algorithm values: " , algo.getValues())
algo.findAlgorithm()
print("Result : ", algo.getResult())


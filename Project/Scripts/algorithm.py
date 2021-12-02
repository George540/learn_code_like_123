import calculate
import loop
import conditional
import assignment

calculate = calculate.Calculate()
loop = loop.Loop()
conditional = conditional.Conditional()
assignment_class = assignment.Assignment()

# some global declared in driver, we will need to import
#VARIABLES = {'X': 10, 'Y': 5} # JUST AN EXAMPLE

class Algorithm:
	def __init__(self, curr_words=[], vals=[], result=0):
		self.curr_words = curr_words    # list of strings
		self.values = vals              # list of values (at most 2)
		self.result = result
	
	def getCurr_words(self):
		return self.curr_words

	def setCurr_words(self, words):
		self.curr_words = words

	def getValues(self):
		return self.values
	
	def addValue(self, val):
		self.values.append(val)
	
	def resetValues(self):
		self.values = []
		
	def getResult(self):
		return self.result
	
	def setResult(self, result):
		self.result = result


	def isNumber(self, string: str):
		# in the case the string is a digit
		if string.isdigit():
			return True
		# in case string is a float
		try:
			float(string)
			return True
		except ValueError:
			return False

	def addStringValueToList(self, string):
		self.addValue(float(string))

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
		# Declare variable X with value 5
		if self.curr_words[0].lower() == 'declare' and self.curr_words[1].lower() == 'variable':
			name = self.curr_words[2]
			if (self.isNumber(self.curr_words[-1])):
				value = float(self.curr_words[-1])
			else:
				value = self.curr_words[-1]
			assignment_class.addVariable(name, value)
			print("Variable " + str(name) + " has been declared")
			self.result = assignment_class.getKeyValuePair(name)
		elif self.curr_words[0].lower() == 'add':
			# calculate.setValueX(self.values[0])
			# calculate.setValueY(self.values[1])
			self.result = calculate.add(self.values[0], self.values[1])

		elif self.curr_words[0].lower() == 'subtract':
			self.result = calculate.subtract(self.values[0], self.values[1])

		elif self.curr_words[0].lower() == 'multiply': 
			self.result = calculate.multiply(self.values[0], self.values[1])

		elif self.curr_words[0].lower() == 'divide':
			self.result = calculate.divide(self.values[0], self.values[1])

		# will this be parsed as 2 seperate words?
		elif self.curr_words[0].lower() == 'square' & self.curr_words[1].lower() == 'root':
			self.result = calculate.squareRoot(self.values[0])
		
		elif self.curr_words[-1].lower() == 'odd':
			conditional.setValue(self.values[0])
			self.result = conditional.isOdd()
		
		elif self.curr_words[-1].lower() == 'even':
			conditional.setValue(self.values[0])
			self.result = conditional.isEven()
		
		else:
			self.result = None

# ###########################################################################################
# algo = Algorithm(curr_words=['Add', '5', 'to', '10'])
# algo.resetValues()
# print("Intial algorithm values: " , algo.getValues())
# algo.isVariable(algo.curr_words[1])
# algo.isVariable(algo.curr_words[3])
# print("Updated algorithm values: " , algo.getValues())
# algo.findAlgorithm()
# print("Result : ", algo.getResult())

# ###########################################################################################
# algo = Algorithm(curr_words=['Square', 'root', '144'])
# algo.resetValues()
# print("Intial algorithm values: " , algo.getValues())
# algo.isVariable(algo.curr_words[2])
# print("Updated algorithm values: " , algo.getValues())
# algo.findAlgorithm()
# print("Result : ", algo.getResult())

# ###########################################################################################
# # ASSUMING X = 10
# algo = Algorithm(curr_words=['Square', 'root', 'X'])
# algo.resetValues()
# print("Intial algorithm values: " , algo.getValues())
# algo.isVariable(algo.curr_words[2])
# print("Updated algorithm values: " , algo.getValues())
# algo.findAlgorithm()
# print("Result : ", algo.getResult())



# # ###########################################################################################
# LOOP
# ###########################################################################################
# algo = Algorithm(curr_words=['add','100','by', '5', '2','times'])
# algo.isVariable(algo.curr_words[1])
# algo.isVariable(algo.curr_words[3])
# algo.isVariable(algo.curr_words[4])
# algo.findAlgorithm()
# print(['add','100','by', '5', '2','times'])
# print("Result : ", algo.getResult())

# # algo.resetValues()
# algo = Algorithm(curr_words=['subtract','100','by', '5', '2','times'])
# print(algo.getValues())
# algo.isVariable(algo.curr_words[1])
# algo.isVariable(algo.curr_words[3])
# algo.isVariable(algo.curr_words[4])
# algo.findAlgorithm()
# print(['subtract','100','by', '5', '2','times'])
# print("Result : ", algo.getResult())

# algo = Algorithm(curr_words=['multiply','100','by', '5', '2','times'])
# algo.resetValues()
# algo.isVariable(algo.curr_words[1])
# algo.isVariable(algo.curr_words[3])
# algo.isVariable(algo.curr_words[4])
# algo.findAlgorithm()
# print(['multiply','100','by', '5', '2','times'])
# print("Result : ", algo.getResult())

# algo = Algorithm(curr_words=['divide','100','by', '5', '2','times'])
# algo.resetValues()
# algo.isVariable(algo.curr_words[1])
# algo.isVariable(algo.curr_words[3])
# algo.isVariable(algo.curr_words[4])
# algo.findAlgorithm()
# print(['divide','100','by', '5', '2','times'])
# print("Result : ", algo.getResult())

# ['Subtract','5', 'from', '100', '10','times']
# index 1 = val1
# index 3 = val2
# index 4 = upper bound for loop

# # ###########################################################################################
# CONDITIONAL
# # ###########################################################################################
# algo = Algorithm(curr_words=['Is','5','even'])
# algo.resetValues()
# print("Intial algorithm values: " , algo.getValues())
# algo.isVariable(algo.curr_words[1])
# print("Updated algorithm values: " , algo.getValues())
# algo.findAlgorithm()
# print("Result : ", algo.getResult())


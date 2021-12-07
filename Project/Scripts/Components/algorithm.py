import Components.calculate as calculate
import Components.loop as loop
import Components.conditional as conditional
import Components.assignment as assignment

calculate = calculate.Calculate()
loop = loop.Loop()
conditional = conditional.Conditional()
assignment_class = assignment.Assignment()

# some global declared in driver, we will need to import
# VARIABLES = {'X': 10, 'Y': 5} # JUST AN EXAMPLE


class Algorithm:
	def __init__(self, curr_words: list[str] = [], index : int = 0, vals=[], result=0):
		self.curr_words = curr_words    # list of strings
		self.curr_clause_index = index # current clause's ordered index
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
		# in case string is a float
		try:
			if string.isdigit():
				return True
			float(string)
			return True
		except ValueError:
			return False

	def addStringValueToList(self, string):
		if self.isNumber(string):
			self.addValue(float(string))
		else:
			self.addValue(assignment_class.getVariable(string))


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

		times = self.getAmountOfRepeats() # X times will be cut if they exist
		print(times)
		self.result = 0
		listresult = []

		for i in range(1, times+1):
			# Declare X to 5
			if self.curr_words[0].lower() == 'declare' and self.curr_words[2].lower() == 'to' and len(self.curr_words) == 4:
				name = self.curr_words[1]
				if (self.isNumber(self.curr_words[-1])):
					value = float(self.curr_words[-1])
					assignment_class.setVariable(name, value)
					self.result = name + " = " + str(value)
				else:
					self.result = "Declaration Error: input value was not a number"

			# Add 5 and 2 = 5 + 2 = 7
			# Add 5 to X  = X + 5
			# Add X and Y = X + Y
			# Add X to Y = Y + X
			# Add 2 and 2 3 times = 2 + (2 + 2 + 2)
			elif self.curr_words[0].lower() == 'add':
				self.addStringValueToList(self.curr_words[1])
				self.addStringValueToList(self.curr_words[3])
				# Check if the second value is a variable, so it can be updated
				if (self.curr_words[2].lower() == 'to'):
					try:
						if (i == 1):
							self.result = calculate.add(self.values[0], self.values[1])
						else:
							self.result += self.values[0]
							assignment_class.setVariable(self.curr_words[3], self.result)
					except KeyError:
						self.result = "Value " + self.curr_words[3] + " does not exist"
				elif (self.curr_words[2].lower() == 'and'):
					listresult[i-1] = calculate.add(self.values[0], self.values[1])
					self.result = listresult

			# Subtract 5 from 2 = 2 - 5 = -3
			# Subtract X from 2 = 2 - X
			# Subtract 3 from X
			# Subtract 1 from 4 3 times = 4 - 1 - 1 - 1 = 1
			elif self.curr_words[0].lower() == 'subtract':
				self.addStringValueToList(self.curr_words[1])
				self.addStringValueToList(self.curr_words[3])
				self.result = calculate.subtract(self.values[0], self.values[1])
				if (self.isNumber(self.curr_words[3]) == False):
					assignment_class.setVariable(self.curr_words[3], self.result)

			# Multiply 5 and 2 = 10
			# Multiply X and 3 = X * 3
			# Multiply X by 3 = X * 3 (update X)
			elif self.curr_words[0].lower() == 'multiply':
				self.addStringValueToList(self.curr_words[1])
				self.addStringValueToList(self.curr_words[3])
				self.result = calculate.multiply(self.values[0], self.values[1])
				if (self.curr_words[2] == 'by'):
					assignment_class.setVariable(self.curr_words[3], self.result)

			# Divide 6 by 2 = 2
			# Divide X by Y = X / Y
			# Divide X by 2 = X / Y
			# Divide X=16 by 2 3 times = 16 / 2 / 2 / 2 = 1
			elif self.curr_words[0].lower() == 'divide' and self.curr_words[2].lower() == 'by':
				self.addStringValueToList(self.curr_words[1])
				self.addStringValueToList(self.curr_words[3])
				if (self.isNumber(self.curr_words[1]) == False):
					assignment_class.setVariable(self.curr_words[1], assignment_class.getVariable(self.curr_words[1]) / self.values[1])
				else:
					self.result = calculate.divide(self.values[0], self.values[1])

			# Square root 4 = 2
			# Square root X = sqrt(X) and update variable
			elif self.curr_words[0].lower() == 'square' and self.curr_words[1].lower() == 'root':
				self.addStringValueToList(self.curr_words[2])
				try:
					self.result = calculate.squareRoot(self.values[0])
					if (self.isNumber(self.curr_words[1]) == False):
						assignment_class.setVariable(
							self.curr_words[2], self.result)
				except TypeError:
					self.result = "Cannot square root. Either negative number or wrong variable type"

			# If 2 is odd...
			# If X is odd...
			# If 2 is even...
			# If X is even...
			elif self.curr_words[0] == 'If' and self.curr_words[2] == 'is':
				if self.curr_words[0] == 'If' and self.curr_words[-1].lower() == 'odd':
					self.addStringValueToList(self.curr_words[1])
					conditional.setValue(self.values[0])
					self.result = conditional.isOdd()
					if (self.isNumber(self.curr_words[1]) == False):
						assignment_class.setVariable(
							self.curr_words[3], self.result)

				elif self.curr_words[-1].lower() == 'even':
					self.addStringValueToList(self.curr_words[1])
					conditional.setValue(self.values[0])
					self.result = conditional.isEven()
					if (self.isNumber(self.curr_words[1]) == False):
						assignment_class.setVariable(
							self.curr_words[3], self.result)

			# Get X = 5
			# Get 2 = 2
			elif len(self.curr_words) == 2 and self.curr_words[0] == 'Get':
				try:
					self.addStringValueToList(self.curr_words[1])
					self.result = self.curr_words[1] + " = " + str(self.values[0])
				except KeyError:
					self.result = "Variable cannot be found"

			# Anything else that doesn't follow the above conditions is an invalid format
			# If result is None, it means there is a calculation error
			else:
				self.result = "Format Error: Try a new sentence"

			times += 1

	def isVariable(self, name):
		return assignment_class.getVariable(name)

	def setDecimalPlaces(self, float_value):
		return "{:.2f}".format(float(float_value))

	def getAmountOfRepeats(self):
		if self.curr_words[-1] == "times" and self.curr_words[-2].isdigit():
			times = int(self.curr_words[-2])
			del self.curr_words[-2:]
			return times
		else:
			return 1

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

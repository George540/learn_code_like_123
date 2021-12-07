import Components.calculate as calculate
import Components.conditional as conditional
import Components.assignment as assignment

calculate = calculate.Calculate()
conditional = conditional.Conditional()
assignment_class = assignment.Assignment()

# some global declared in driver, we will need to import
# VARIABLES = {'X': 10, 'Y': 5} # JUST AN EXAMPLE


class Algorithm:
	def __init__(self, curr_words: list[str] = [], vals=[], result=0):
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
		self.result = 0
		listresult = []
		print(self.curr_words)

		# If 2 is odd...
		# If X is odd...
		# If 2 is even...
		# If X is even...
		temp = True
		if self.curr_words[0].lower() == 'if' and self.curr_words[2].lower() == 'is' and len(self.curr_words) == 4:
			if self.curr_words[-1].lower() == 'odd':
				self.addStringValueToList(self.curr_words[1])
				conditional.setValue(self.values[0])
				temp = conditional.isOdd()
				if (temp == True):
					self.result = temp
					return

			elif self.curr_words[-1].lower() == 'even':
				self.addStringValueToList(self.curr_words[1])
				conditional.setValue(self.values[0])
				temp = conditional.isEven()
				if (temp == True):
					self.result = temp
					return

		# Get X = 5
		# Get 2 = 2
		elif len(self.curr_words) == 2 and self.curr_words[0].lower() == 'get':
			try:
				self.addStringValueToList(self.curr_words[1])

				if (self.values[0] == None):
					raise KeyError("Variable cannot be found")
				if (self.isNumber(self.curr_words[1]) == False):
					self.result = self.curr_words[1] + " = " + str(self.values[0])
				else:
					self.result = str(self.values[0])
				return
			except KeyError:
				self.result = "Variable cannot be found"
				return

		if temp == False:
			self.result = "False condition. Statement skipped"
			return

		for i in range(1, times+1):
			# Let X be 5
			if self.curr_words[0].lower() == 'let' and self.curr_words[2].lower() == 'be' and len(self.curr_words) == 4:
				name = self.curr_words[1]
				if (not self.isNumber(self.curr_words[1])):
					if (self.isNumber(self.curr_words[3])):
						value = float(self.curr_words[3])
						assignment_class.setVariable(name, value)
						self.result = name + " = " + str(value)
					elif (not self.isNumber(self.curr_words[3])):
						if (assignment_class.getVariable(self.curr_words[3]) == None):
							self.result = "Variable does not exist"
							return
						value = float(assignment_class.getVariable(self.curr_words[3]))
						assignment_class.setVariable(name, value)
						self.result = name + " = " + str(value)
				else:
					self.result = "Declaration Error: input value was not a number"

			# Add 5 and 2 = 5 + 2 = 7
			# Add 5 to X  = X + 5
			# Add X and Y = X + Y
			# Add X to Y = Y + X
			# Add 2 and 2 3 times = 2 + (2 + 2 + 2)
			elif self.curr_words[0].lower() == 'add' and len(self.curr_words) == 4 and (self.curr_words[2].lower() == 'and' or self.curr_words[2].lower() == 'to'):
				try:
					self.addStringValueToList(self.curr_words[1])
					self.addStringValueToList(self.curr_words[3])
					if (self.values[0] == None or self.values[1] == None):
						raise KeyError("Variable cannot be found")
					# Check if the second value is a variable, so it can be updated
					if (self.curr_words[2].lower() == 'to'):
						if (i == 1):
							self.result = calculate.add(self.values[0], self.values[1])
							if (self.isNumber(self.curr_words[3]) == False):
								assignment_class.setVariable(self.curr_words[3], self.result)
						else:
							self.result += self.values[0]
							assignment_class.setVariable(self.curr_words[3], self.result)
					elif (self.curr_words[2].lower() == 'and'):
						listresult.append(calculate.add(self.values[0], self.values[1]))
						self.result = listresult
				except KeyError:
					self.result = "Variable does not exist"

			# Subtract 5 from 2 = 2 - 5 = -3
			# Subtract X from 2 = 2 - X
			# Subtract 3 from X
			# Subtract 1 from 4 3 times = 4 - 1 - 1 - 1 = 1
			elif self.curr_words[0].lower() == 'subtract' and self.curr_words[2].lower() == 'from' and len(self.curr_words) == 4:
				try:
					self.addStringValueToList(self.curr_words[1])
					self.addStringValueToList(self.curr_words[3])
					if (self.values[0] == None or self.values[1] == None):
						raise KeyError("Variable cannot be found")
					if (self.isNumber(self.curr_words[3]) == False):
						if (i == 1):
							self.result = calculate.subtract(self.values[0], self.values[1])
						else:
							self.result -= self.values[0]
						assignment_class.setVariable(self.curr_words[3], self.result)
					else:
						if (i == 1):
							self.result = calculate.subtract(self.values[0], self.values[1])
						else:
							self.result = calculate.subtract(self.values[0], self.result)
				except KeyError:
					self.result = "Variable does not exist"

			# Multiply 5 and 2 = 10
			# Multiply X and 3 = X * 3
			# Multiply X by 3 = X * 3 (update X)
			elif self.curr_words[0].lower() == 'multiply' and len(self.curr_words) == 4 and (self.curr_words[2].lower() == 'and' or self.curr_words[2].lower() == 'by'):
				try:
					self.addStringValueToList(self.curr_words[1])
					self.addStringValueToList(self.curr_words[3])
					if (self.values[0] == None or self.values[1] == None):
							raise KeyError("Variable cannot be found")
					if (self.curr_words[2].lower() == 'by' and self.isNumber(self.curr_words[1]) == False):
						if (i == 1):
							self.result = calculate.multiply(self.values[0], self.values[1])
						else:
							assignment_class.setVariable(self.curr_words[1], calculate.multiply(self.result, self.values[1]))
							self.result = assignment_class.getVariable(self.curr_words[1])
					elif (self.curr_words[2].lower() == 'and'):
						if (i == 1):
							self.result = calculate.multiply(self.values[0], self.values[1])
							listresult.append(self.result)
						else:
							listresult.append(calculate.multiply(self.values[0], self.values[1]))
							self.result = listresult
					else:
						if (i == 1):
							self.result = calculate.multiply(self.values[0], self.values[1])
						else:
							self.result = calculate.multiply(self.result, self.values[1])
				except KeyError:
					self.result = "Variable does not exist"
			# Divide 6 by 2 = 2
			# Divide X by Y = X / Y
			# Divide X by 2 = X / Y
			# Divide X=16 by 2 3 times = 16 / 2 / 2 / 2 = 1
			elif self.curr_words[0].lower() == 'divide' and self.curr_words[2].lower() == 'by' and len(self.curr_words) == 4:
				try:
					self.addStringValueToList(self.curr_words[1])
					self.addStringValueToList(self.curr_words[3])
					if (self.values[0] == None or self.values[1] == None):
						raise KeyError("Variable cannot be found")
					if (self.values[1] == 0):
						raise ZeroDivisionError("Cannot divide by 0")
					if (self.isNumber(self.curr_words[1]) == False):
						if (i == 1):
							self.result = calculate.divide(self.values[0], self.values[1])
						else:
							self.result /= self.values[1]
						assignment_class.setVariable(self.curr_words[1], self.result)
					else:
						if (i == 1):
							self.result = calculate.divide(self.values[0], self.values[1])
						else:
							self.result = calculate.divide(self.result, self.values[1])
				except KeyError:
					self.result = "Variable does not exist"
				except ZeroDivisionError:
					self.result = "Cannot divide by 0"

			# Square root 4 = 2
			# Square root X = sqrt(X) and update variable
			elif self.curr_words[0].lower() == 'square' and self.curr_words[1].lower() == 'root' and len(self.curr_words) == 3:
				try:
					self.addStringValueToList(self.curr_words[2])
					if (self.values[0] == None):
						raise KeyError("Variable cannot be found")
					if (i == 1):
						self.result = calculate.squareRoot(self.values[0])
					else:
						self.result = calculate.squareRoot(self.result)

					if (self.result == None):
						raise ArithmeticError("Cannot square root a negative")

					if (self.isNumber(self.curr_words[1]) == False):
						assignment_class.setVariable(self.curr_words[2], self.result)
				except TypeError:
					self.result = "Cannot square root. Either negative number or wrong variable type"
				except KeyError:
					self.result = "Variable does not exist"
				except ArithmeticError:
					self.result = "Cannot square root a negative"

			# Anything else that doesn't follow the above conditions is an invalid format
			# If result is None, it means there is a calculation error
			else:
				self.result = "Format Error: Try a new sentence"

		print(self.result)
		if type(self.result) is list:
			self.result = ', '.join(map(str, self.result))
		else:
			self.result = str(self.result)

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

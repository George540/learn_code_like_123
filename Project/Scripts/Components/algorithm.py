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

# Examples of possible input words
# curr_words = ['ADD', '10', 'and', '2']
# curr_words = ['Subtract', '5', 'and', '7']
# curr_words = ['sQuAre 'rOOt', '144']
# curr_words = ['is 'X', 'odd']
# curr_words = ['Add '5', '10', 'times']
# words are tested in lower case
	def findAlgorithm(self):
    	# Find out how many times the statement will be repeated
		times = self.getAmountOfRepeats() # 'X times' will be cut from the list if they exist
		self.result = 0
		listresult = []
		print(self.curr_words)

		# If 2 is odd...
		# If X is odd...
		# If 2 is even...
		# If X is even...
		temp = True # temporary result for exiting condition when it is correct
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
				
				# If first value is a variable: X
				if (not self.isNumber(self.curr_words[1])):
    				# If second variable is just a number: X + 3
					if (self.isNumber(self.curr_words[3])):
						value = float(self.curr_words[3])
						assignment_class.setVariable(name, value)
						self.result = name + " = " + str(value)
					# If second variable is another variable: X + Y
					elif (not self.isNumber(self.curr_words[3])):
						if (assignment_class.getVariable(self.curr_words[3]) == None):
							self.result = "Variable does not exist"
							return
						value = float(assignment_class.getVariable(self.curr_words[3]))
						assignment_class.setVariable(name, value)
						self.result = name + " = " + str(value)
				# Cannot name a variable as a number
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
					# If one of the two values is a variable that does not exist, raise error
					if (self.values[0] == None or self.values[1] == None):
						raise KeyError("Variable cannot be found")
					# Add 2 to X: adds 2 to the variable or number
					if (self.curr_words[2].lower() == 'to'):
						if (i == 1):
							self.result = calculate.add(self.values[0], self.values[1])
							if (self.isNumber(self.curr_words[3]) == False):
								assignment_class.setVariable(self.curr_words[3], self.result)
						else:
							self.result += self.values[0]
							assignment_class.setVariable(self.curr_words[3], self.result)
					# Add 2 and X: adds 2 and a number/variable without changing anything in memory
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
					# If one of the two values is a variable that does not exist, raise error
					if (self.values[0] == None or self.values[1] == None):
						raise KeyError("Variable cannot be found")
					# Subtract 3 from X: second value is a variable that will be updated
					if (self.isNumber(self.curr_words[3]) == False):
						if (i == 1):
							self.result = calculate.subtract(self.values[0], self.values[1])
						else:
							self.result -= self.values[0]
						assignment_class.setVariable(self.curr_words[3], self.result)
					# Subtract 3 from 9
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
					# If one of the two values is a variable that does not exist, raise error
					if (self.values[0] == None or self.values[1] == None):
							raise KeyError("Variable cannot be found")
					# Multiply X by 3: variable will be updated
					if (self.curr_words[2].lower() == 'by' and self.isNumber(self.curr_words[1]) == False):
						if (i == 1):
							self.result = calculate.multiply(self.values[0], self.values[1])
						else:
							assignment_class.setVariable(self.curr_words[1], calculate.multiply(self.result, self.values[1]))
							self.result = assignment_class.getVariable(self.curr_words[1])
					# Multiply X and 3: variable will NOT be updated, just a random calculation that returns a result
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
					# If one of the two values is a variable that does not exist, raise error
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

			# ANYTHING ELSE that doesn't follow the above conditions is an invalid format
			# Typos and extra unecessary words will return this result as well
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

import algorithm
import calculate
import conditional
import Interpreter
import loop

sentence_interpreter = Interpreter.Interpreter()
algorithm_finder = algorithm.Algorithm()

print("--- Welcome to the testing version of the program ---")

input_sentense = ""

while True:
	input_sentense = str(input("\nEnter a sentense: "))
	sentence_interpreter.setCurrentSentence(input_sentense)
	sentence_interpreter.splitSentense()
	current_words = sentence_interpreter.splitClause(sentence_interpreter.getCurrentClauses()[0])
	print(current_words)

	algorithm_finder.setCurr_words(current_words)
	algorithm_finder.resetValues()

	if algorithm_finder.isNumber(algorithm_finder.getCurr_words()[1]):
		algorithm_finder.addStringValueToList(algorithm_finder.getCurr_words()[1])
	if algorithm_finder.isNumber(algorithm_finder.getCurr_words()[3]):
		algorithm_finder.addStringValueToList(algorithm_finder.getCurr_words()[3])
	print("Values: ", algorithm_finder.getValues())

	algorithm_finder.findAlgorithm()
	print("Result : ", algorithm_finder.getResult())

	isTerminated = str(input("\nQuit program? (y/n) "))
	if (isTerminated == 'y'):
		print('Program Terminated...\n')
		break
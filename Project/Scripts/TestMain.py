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

	for c in sentence_interpreter.getCurrentClauses():
			
		current_words = sentence_interpreter.splitClause(c)
		print(current_words)
		current_words, numberOfRepeats = sentence_interpreter.getAmountOfRepeats(current_words)
		print(current_words)

		while (numberOfRepeats > 0):
			algorithm_finder.setCurr_words(current_words)
			algorithm_finder.resetValues()
			algorithm_finder.findAlgorithm()
			print("Values: ", algorithm_finder.getValues())
			print("Result : ", algorithm_finder.getResult())
			numberOfRepeats -= 1

	isTerminated = str(input("\nQuit program? (y/n) "))
	if (isTerminated == 'y'):
		print('Program Terminated...\n')
		break
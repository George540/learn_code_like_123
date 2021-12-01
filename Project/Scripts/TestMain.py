import algorithm
import calculate
import conditional
import Interpreter
import loop

calculator = calculate.Calculate()
iteration = loop.Loop()
condition = conditional.Conditional()


print("--- Welcome to the testing version of the program ---")

input_sentense = ""

while True:
	input_sentense = str(input("\nEnter a sentense: "))
	


	isTerminated = str(input("\nQuit program? (y/n) "))
	if (isTerminated == 'y'):
		print('Program Terminated...\n')
		break
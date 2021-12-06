
# import Components.algorithm as algorithm
# import Components.Interpreter as Interpreter

# sentence_interpreter = Interpreter.Interpreter()
# algorithm_finder = algorithm.Algorithm()


# # print("--- Welcome to the testing version of the program ---")

# # input_sentense = ""

# while True:
#     input_sentense = str(input("\nEnter a sentense: "))
#     sentence_interpreter.setCurrentSentence(input_sentense)
#     sentence_interpreter.splitSentense()

#     for i, c in enumerate(sentence_interpreter.getCurrentClauses()):
#         current_words = sentence_interpreter.splitClause(c)
#         print(current_words)
#         current_words, numberOfRepeats = sentence_interpreter.getAmountOfRepeats(
#             current_words)
#         print(current_words)

#         # Check ifcondition is not followed by a statement, return error
#         # This avoids any unecessary processes afterwards
#         if current_words[0] == "If" and current_words[2] == "is" and i + 1 >= len(sentence_interpreter.getCurrentClauses()):
#             algorithm_finder.setResult("NoStatementError")
#             print("Result : ", algorithm_finder.getResult())
#             break

#         while (numberOfRepeats > 0):
#             algorithm_finder.setCurr_words(current_words)
#             algorithm_finder.resetValues()
#             algorithm_finder.findAlgorithm()
#             print("Values: ", algorithm_finder.getValues())
#             print("Result : ", algorithm_finder.getResult())
#             numberOfRepeats -= 1

#         if (algorithm_finder.getResult() == False):
#             break

#     isTerminated = str(input("\nQuit program? (y/n) "))
#     if (isTerminated == 'y'):
#         print('Program Terminated...\n')
#         break

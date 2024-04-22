from random import randint

a = randint(1, 50)
b = randint(1, 50)
answer = a + b

question = "What is " + str(a) + " + " + str(b) + "?"

ui = input(question)
if ui == a+b:
    go here
else:
    redo level

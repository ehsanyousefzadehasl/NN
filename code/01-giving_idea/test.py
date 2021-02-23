from neuron import neuron
from random import randrange

n1 = neuron(2)

print(n1.weights)
print(n1.test([98, 99]))
print(n1.test([96, 97]))

# our data that is going to be used for training our neuron
for x in range(100):
    for y in range(100):
        input_array = []
        input_array.append(x)
        input_array.append(y)

        if x >= y:
            answer = 1
        else:
            answer = -1

        print(x, y, n1.test(input_array), answer)
        n1.training(input_array, answer)
print(n1.weights)
print(n1.test([98, 99]))
print(n1.test([96, 97]))

from neuron import neuron
from random import randrange

n1 = neuron(2)

print(n1.weights)
print(n1.test([98, 99]))
print(n1.test([96, 97]))

# our data that is going to be used for training our neuron
for i in range(100000):
    input_array = []
    input_array.append(randrange(-100000, 100000))
    input_array.append(randrange(-100000, 100000))

    if input_array[0] >= input_array[1]:
        answer = 1
    else:
        answer = -1

    # print(x, y, n1.test(input_array), answer)
    n1.training(input_array, answer)

print(n1.weights)
print(n1.test([98, 99]))
print(n1.test([96, 97]))

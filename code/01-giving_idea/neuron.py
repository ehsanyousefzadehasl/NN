import random

def activation_function(number):
    if number >= 0:
        return 1
    else:
        return -1

class neuron:
    def __init__(self, num_of_inputs):
        self.weights = [None] * num_of_inputs
        for i in range(num_of_inputs):
            self.weights[i] = random.random()
        self.bias = random.random()

    def test(self, input_array):
        weighted_sum = 0
        for i in range(len(input_array)):
            weighted_sum += input_array[i] * self.weights[i]
        return activation_function(weighted_sum)
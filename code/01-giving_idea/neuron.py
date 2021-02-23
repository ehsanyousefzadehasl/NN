import random

def activation_function(number):
    if number >= 0:
        return 1
    else:
        return -1

class neuron:
    learning_rate = 0.1
    def __init__(self, num_of_inputs):
        self.weights = [None] * num_of_inputs
        for i in range(num_of_inputs):
            self.weights[i] = (random.random() - 0.5) * 2
        self.bias = random.random()
        # print(self.weights)

    def test(self, input_array):
        weighted_sum = 0
        for i in range(len(input_array)):
            weighted_sum += input_array[i] * self.weights[i]
        return activation_function(weighted_sum)

    def training(self, input_array, answer):
        tested_result = self.test(input_array)
        error = answer - tested_result
        if error != 0:
            for i in range(len(input_array)):
                self.weights[i] += error * input_array[i] * self.learning_rate

        # print(self.weights)
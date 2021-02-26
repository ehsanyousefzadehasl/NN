# Neural Networks
In this repository, I try to summarize and gather from notes and codes while I am learning about neural networks.

I started to know what the real story is in this field by watching [this](https://www.youtube.com/watch?v=ntKn5TPHHAk) on YouTube, which gave me a general idea summarized in the following concise summary.

This field of computer science tries to mimic the process happening in our brains to be able to build softwares that can be intelligent and also be able to do what our brains do. Our brains are far better than modern computers in some types of computations like pattern recognition or approximate guessing.

The very first step in this journey is to understand how a single neuron in our brains works, then try to model it to be able to implement them in an artificial way. Actually, we can look at every neuron like a function that its inputs have weights entering it, then the neuron itself has a computation formula, which based on it, produces an output. Additionally, this single neuron based on the desired output (in supervised learning, where we provide desired output for a set of inputs in training phase) and its produced one tries to change the weights of inputs which they are multiplies entering the main function. To go deeper inside, there is an activation function inside the neuron that conforms the output of aggregation of inputs multiplied by their weights to the desired range. For example, if we want to classify an input (a point), so we can use just a function like: **F(X) = u(t) - u(-t)** in which **u(t)** is a step function (**u(t) = 0 for t < 0 and = 1 for x >= 0**). In the following figure, we can see what we talked about it.

![structure of an artificial neuron](img/The-structure-of-an-artificial-neuron.png)

But, what is the bias?
Bias is for shifting the activation function in a way that it may be impossible just by changing the weights (when inputs are zero). Look at the following figures consecutively, you will catch it:

![bias1](img/bias1.gif)
![bias2](img/bias2.png)

![bias3](img/bias3.gif)
![bias4](img/bias4.png)

[Here](code/01-giving_idea/neuron.py), you can look at a very simple neuron.

In the training process (in a supervised learning), the neuron has access the answer and its generated result. So, based on the difference between the answer and the produced result (called error), it tries to update the weights (w0 = w0 + delta(w0)). The process that changes the weights is called **gradient descent**.
```
delta(w) = error * input

new weight = weight + error * input
```
---
# ML by Andrew Ng
Then, I came up with the idea of watching Machine Learning tutorial by Andrew Ng, which is available on YouTube. I will summarize what I learn in the simplest way with doing exercises in octave and a try to implement them in python.

[Arthur Samuel](https://en.wikipedia.org/wiki/Arthur_Samuel) (1959) defines ML as: "Field of study that gives computers the ability to learn without being explicitely programmed."

[Tom Mitchel](https://en.wikipedia.org/wiki/Tom_M._Mitchell) (1998) defines a well-posed learning problem as: "a computer program is said to learn from experience E with respect to some task T and some performance measure P. If its performance on T, as measured by P, improves with experience E"

(Example for Tom Mitch's definition) Supposing an email program learning from our labeling emails as spam:
- (Task): Classifying emails as spam or not spam
- (Experience): Observing our labels as spam or not
- (Performance): The number of emails correctly classified

ML learning algorithms:
- Supervised Learning (Regression (continuous values like price prediction), Classification (discrete values like yes/no classification)) | Right answer is told to the machine
- Unsupervised learning (Clustering, Google news, organizing computing clusters, social network analysis, market segmentation, astronomical data analysis, cocktail party algorithm)
- Reinforcement Learning
- Recommender Systems

## Linear Regression
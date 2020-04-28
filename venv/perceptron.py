import random

class Perceptron(object):

    def __init__(self, inputSize, bias=-1, epochs=100, learningRate=0.1):
        self.epochs = epochs
        self.learningRate = learningRate
        self.bias = bias
        self.weights = [0] * (inputSize + 1)

        for i in range(len(self.weights)):
            self.weights[i] = round(random.uniform(-0.5,0.5), 2)

    def predict(self, input):
        summation = self.bias * self.weights[0]
        for i in range(len(input)):
            summation += input[i] * self.weights[i+1]
        if summation > 0:
            return 1
        else:
            return 0

    def train(self, trainingSet, labels):
        for epoch in range(self.epochs):
            for i in range(len(trainingSet)):
                prediction = self.predict(trainingSet[i])
                input = trainingSet[i]
                self.weights[0] = round(self.weights[0] - self.learningRate * (prediction - labels[i]) * self.bias, 2)
                for j in range(len(input)):
                    self.weights[j+1] = round(self.weights[j+1] - self.learningRate * (prediction - labels[i]) * input[j],2)

    def test(self,trainingSet,trainingLabels,set,labels):
        self.train(trainingSet,trainingLabels)
        correct = 0
        for i in range(len(set)):
            if self.predict(set[i]) == labels[i]:
                correct += 1
        print("accuracy: ", (correct / len(set)) * 100, "%")
        print("Final Weights: ", self.weights, "\n")

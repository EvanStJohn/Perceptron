import random

class Perceptron(object):

    def __init__(self, inputSize, bias=-1, epochs=100, learningRate=0.01):
        self.epochs = epochs
        self.learningRate = learningRate
        self.bias = bias
        self.weights = [0] * (inputSize + 1)

        for i in range(len(self.weights)):
            self.weights[i] = random.uniform(-0.5,0.5)

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
            errors = 0
            for i in range(len(trainingSet)):
                prediction = self.predict(trainingSet[i])
                errors += (prediction - labels[i]) ** 2
                input = trainingSet[i]
                self.weights[0] = self.weights[0] - self.learningRate * (prediction - labels[i]) * self.bias
                for j in range(len(input)):
                    self.weights[j+1] = self.weights[j+1] - self.learningRate * (prediction - labels[i]) * input[j]
            #print("epoch",epoch, errors)

    def test(self,trainingSet,trainingLabels,set,labels):
        self.train(trainingSet,trainingLabels)
        correct = 0
        for i in range(len(set)):
            if self.predict(set[i]) == labels[i]:
                correct += 1
        return (correct / len(set)) * 100

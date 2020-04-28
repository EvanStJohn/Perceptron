import random
from perceptron import Perceptron

trainingInputs1 = []
trainingInputs1.append([0,1,0,0,1,0,0,1,0]) #middle i
trainingInputs1.append([0,1,0,0,1,0,0,1,1]) #middle l
trainingLabels1 = [0,1]
data1 = []
data1.append([0,0,1,0,0,1,0,0,1]) #right i
data1.append([1,0,0,1,0,0,1,1,1]) #full l
data1.append([1,0,0,1,0,0,1,1,0]) #left l
data1.append([1,0,0,1,0,0,1,0,0]) #left i
label1 = [0,1,1,0]
perceptron1 = Perceptron(9)
print("test 1: 2 training inputs")
perceptron1.test(trainingInputs1,trainingLabels1,data1,label1)

trainingInputs2 = []
trainingInputs2.append([0,1,0,0,1,0,0,1,0]) #middle i
trainingInputs2.append([0,1,0,0,1,0,0,1,1]) #middle l
trainingInputs2.append([1,0,0,1,0,0,1,1,0]) #left l
trainingInputs2.append([1,0,0,1,0,0,1,0,0]) #left i
trainingLabels2 = [0,1,1,0]
data2 = []
data2.append([0,0,1,0,0,1,0,0,1]) #right i
data2.append([1,0,0,1,0,0,1,1,1]) #full l
label2 = [0,1]
perceptron2 = Perceptron(9)
print("test 2: 4 training inputs")
perceptron2.test(trainingInputs2,trainingLabels2,data2,label2)

import random
from perceptron import Perceptron

def average(num,trainingSet,trainingLabels,set,labels):
    sum = 0
    for i in range(num):
        perceptron = Perceptron(len(set[0]))
        sum += perceptron.test(trainingSet,trainingLabels,set,labels)
    avg = round(sum / num, 2)
    print("Training Size: ", len(trainingSet))
    print("Testing Size: ", len(set))
    print("accurracy: ", avg, " %\n")

print("test 1: 3x3 grid")
trainingInputs1 = []
trainingInputs1.append([0,1,0,0,1,0,0,1,0]) #middle i
trainingInputs1.append([0,1,0,0,1,0,0,1,1]) #middle l
trainingLabels1 = [0,1]
data1 = []
data1.append([0,0,1,0,0,1,0,0,1]) #right i
data1.append([1,0,0,1,0,0,1,1,1]) #full l
data1.append([1,0,0,1,0,0,1,1,0]) #left l
data1.append([1,0,0,1,0,0,1,0,0]) #left i
data1.append([0,0,1,0,0,1,0,0,0]) #small right i, upper
data1.append([0,0,0,0,0,1,0,0,1]) #small right i, lower
data1.append([0,1,0,0,1,0,0,0,0]) #small mid i, upper
data1.append([0,0,0,0,1,0,0,1,0]) #small mid i, lower
data1.append([1,0,0,1,0,0,0,0,0]) #small left i, upper
data1.append([0,0,0,1,0,0,1,0,0]) #small left i, lower
data1.append([0,1,0,0,1,1,0,0,0]) #small mid l, upper
data1.append([0,0,0,0,1,0,0,1,1]) #small mid l, lower
data1.append([1,0,0,1,1,0,0,0,0]) #small left l, upper
data1.append([0,0,0,1,0,0,1,1,0]) #small left l, lower
data1.append([1,1,0,1,1,0,1,1,0]) #large i, left
data1.append([0,1,1,0,1,1,0,1,1]) #large i, right
data1.append([1,1,0,1,1,0,1,1,1]) #large l, small bottom
data1.append([1,1,0,1,1,1,1,1,1]) #large l, filled mid
label1 = [0,1,1,0,0,0,0,0,0,0,1,1,1,1,0,0,1,1]
average(10,trainingInputs1,trainingLabels1,data1,label1)

print("test 2: 3x3 grid")
trainingInputs2 = []
trainingInputs2.append([0,1,0,0,1,0,0,1,0]) #middle i
trainingInputs2.append([0,1,0,0,1,0,0,1,1]) #middle l
trainingInputs2.append([1,0,0,1,0,0,1,1,0]) #left l
trainingInputs2.append([1,0,0,1,0,0,1,0,0]) #left i
trainingInputs2.append([0,0,1,0,0,1,0,0,0]) #small right i, upper
trainingInputs2.append([1,0,0,1,1,0,0,0,0]) #small left l, upper
trainingLabels2 = [0,1,1,0,0,1]
data2 = []
data2.append([0,0,1,0,0,1,0,0,1]) #right i
data2.append([1,0,0,1,0,0,1,1,1]) #full l
data2.append([0,0,0,0,0,1,0,0,1]) #small right i, lower
data2.append([0,1,0,0,1,0,0,0,0]) #small mid i, upper
data2.append([0,0,0,0,1,0,0,1,0]) #small mid i, lower
data2.append([1,0,0,1,0,0,0,0,0]) #small left i, upper
data2.append([0,0,0,1,0,0,1,0,0]) #small left i, lower
data2.append([0,1,0,0,1,1,0,0,0]) #small mid l, upper
data2.append([0,0,0,0,1,0,0,1,1]) #small mid l, lower
data2.append([0,0,0,1,0,0,1,1,0]) #small left l, lower
data2.append([1,1,0,1,1,0,1,1,0]) #large i, left
data2.append([0,1,1,0,1,1,0,1,1]) #large i, right
data2.append([1,1,0,1,1,0,1,1,1]) #large l, small bottom
data2.append([1,1,0,1,1,1,1,1,1]) #large l, filled mid
label2 = [0,1,0,0,0,0,0,1,1,1,0,0,1,1]
average(10,trainingInputs2,trainingLabels2,data2,label2)

print("test 3: 5x5 grid")
trainingInputs3 = []
trainingInputs3.append([0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0]) #standard middle i
trainingInputs3.append([0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,1,1]) #standard middle l
trainingLabels3 = [0,1]
data3 = []
data3.append([1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0]) #standard left i
data3.append([1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,1,1,0,0]) #standard left l
data3.append([0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0]) #standard mid-left i
data3.append([0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,1,1,0]) #standard mid-left l
data3.append([0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0]) #standard mid-right i
data3.append([0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1]) #standard right i
data3.append([1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,1,1,1,1]) #full-bottom left l
data3.append([0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,1,1,1]) #full-bottom mid-left l
data3.append([0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,1]) #2-wide middle l
data3.append([0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0]) #2-wide middle i
data3.append([0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0]) #2-wide mid-left i
data3.append([1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0]) #2-wide left i
label3 = [0,1,0,1,0,0,1,1,1,0,0,0]
average(10,trainingInputs3,trainingLabels3,data3,label3)
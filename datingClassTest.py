# -*- coding: utf-8 -*-
import myKNN
from numpy import*
from os import listdir
import time
start_time = time.time()
hwLabels = []
trainingFileList = listdir('trainingDigits')           #load the training set
m = len(trainingFileList)
trainingMat = zeros((m, 1024))
for i in range(m):
    fileNameStr = trainingFileList[i]
    fileStr = fileNameStr.split('.')[0]  # take off .txt
    classNumStr = int(fileStr.split('_')[0])
    hwLabels.append(classNumStr)
    trainingMat[i, :] = myKNN.img2vector('trainingDigits/%s' % fileNameStr)
testFileList = listdir('testDigits')  # iterate through the test set
errorCount = 0.0
mTest = len(testFileList)
for i in range(mTest):
    fileNameStr = testFileList[i]
    fileStr = fileNameStr.split('.')[0]  # take off .txt
    classNumStr = int(fileStr.split('_')[0])
    vectorUnderTest =  myKNN.img2vector('testDigits/%s' % fileNameStr)
    classifierResult =  myKNN.classify0(vectorUnderTest, trainingMat, hwLabels, 3)
    #print "the classifier came back with: %d, the real answer is: %d" % (classifierResult, classNumStr)
    if (classifierResult != classNumStr): errorCount += 1.0
#print "\nthe total number of errors is: %d" % errorCount
print "\nthe total error rate is: %f" % (errorCount/float(mTest))
end_time = time.time()
print'total time is:',end_time - start_time
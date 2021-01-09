#!/usr/bin/python
# encoding: utf-8

import random
import os
import sys
import subprocess

global maxNum
global minNum

subprocess.Popen(["say", "-v", "Fred", "Pick", "a", "number..."])  
dailyNum = int(raw_input("What is the number of the day: "))
iterations = int(raw_input("How many examples would you like: "))

def generateMultiple(dailyNum):
    maxNum = int(dailyNum / 5)
    minNum = 3
    num1 = random.randint(minNum, maxNum)
    num2 = random.randint(minNum, maxNum)
    generatedNum = num1 * num2
    if generatedNum > dailyNum:
        delta = generatedNum - dailyNum
        symbol = " - "
        print(str(num1) + " x " + str(num2) + symbol + str(delta) + " = " + str(dailyNum))
    elif generatedNum < dailyNum:
        delta = dailyNum - generatedNum
        symbol = " + "
        print(str(num1) + " x " + str(num2) + symbol + str(delta) + " = " + str(dailyNum))
    else:
        pass
    
def generateAddition(dailyNum):
    maxNum = int(dailyNum / 2)
    minNum = int(dailyNum / 3)
    num1 = random.randint(minNum, maxNum)
    num2 = random.randint(minNum, maxNum)
    generatedNum = num1 + num2
    if generatedNum > dailyNum:
        delta = generatedNum - dailyNum
        symbol = " - "
        print(str(num1) + " + " + str(num2) + symbol + str(delta) + " = " + str(dailyNum))
    elif generatedNum < dailyNum:
        delta = dailyNum - generatedNum
        symbol = " + "
        print(str(num1) + " + " + str(num2) + symbol + str(delta) + " = " + str(dailyNum))
    else:
        pass
    
def generateSubtraction(dailyNum):
    maxNum = int(dailyNum * 1.5)
    minNum = int(dailyNum / 5)
    num1 = random.randint(minNum, maxNum)
    num2 = random.randint(minNum, maxNum)
    allNums = sorted([num1, num2])
    generatedNum = allNums[1] - allNums[0]
    
    if generatedNum > dailyNum:
        delta = generatedNum - dailyNum
        symbol = " - "
        print(str(allNums[1]) + " - " + str(allNums[0]) + symbol + str(delta) + " = " + str(dailyNum))
    elif generatedNum < dailyNum:
        delta = dailyNum - generatedNum
        symbol = " + "
        print(str(allNums[1]) + " - " + str(allNums[0]) + symbol + str(delta) + " = " + str(dailyNum))
    else:
        pass  
        
        
def factorsOfNum(dailyNum):
    for i in range(1, dailyNum + 1):
        if dailyNum % i == 0:
            print(i)        
        

print("\n >>> MULTIPLES THAT WILL TOTAL " + str(dailyNum) + "...")
for i in range(iterations):
    generateMultiple(dailyNum)

print("\n >>> INITIAL ADDITIONS THAT WILL TOTAL " + str(dailyNum) + "...")
for i in range(iterations):
    generateAddition(dailyNum)
    
print("\n >>> SUBTRACTIONS WITH ADDITIONS THAT WILL TOTAL " + str(dailyNum) + "...")
for i in range(iterations):
    generateSubtraction(dailyNum)
    
print("\n >>> FACTORS")
factorsOfNum(dailyNum)

print("")
    
    
subprocess.Popen(["say", "-v", "Fred", "Homework", "is", "done"])    
    
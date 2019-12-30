from math import *

print("Welcome to Python")

# data variables strings

print("We the people of India.\n I wanted print this line ")
print("Python is cool" + str(12))
strVal = "Perform string operation"
print(strVal)
print(strVal.upper() + ". Length of string is : " + str(len(strVal)))

print("Value of index is :" + strVal[7])
print("Value of index is : " + strVal[8])
print("Indexed Value is : " + str(strVal.index("i")))
# Math Operations
num1 = 10
num2 = 5
print(num1 + num1)

print(round(3.14))
print(ceil(3.189))
print(sqrt(10))
print(pow(2, 4))
print(pow(10, 1))

userName = input("Please enter your name : ")
print("Hello " + userName + ", Welcome to the Python. ")

num1=input("Enter Value 1")
num2= input("Enter second value")

print(num1+num2) #not a summation its a concatination
#print(int(num1)+int(num2)) #summation of integers only
print(float(num1)+float(num2))  # Summation of all whole number
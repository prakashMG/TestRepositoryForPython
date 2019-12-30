def functionDemo():
    print("any code inside function should be indented")


def sayHi():
    print("This is Hi function")


def parameterizedFunction(val1, val2):
    print("This is value1 : " + str(val1))
    print("This is value1 : " + str(val2))


def cube(num):
    cubeRoot = num * num * num
    return cubeRoot


def maxnumber(num1, num2):
    if (num1 > num2):
        print("max number among all is : " + str(num1))
    else:
        print("max number among all is : " + str(num2))


def maxofThreenums(num1, num2, num3):
    if (num1 >= num2 and num1 >= num3):
        return num1
    elif (num2 >= num3 and num2 >= num1):
        return num2
    else:
        return num3


print("Start")
functionDemo()
sayHi()
print("Cuberoot of a vlaue is : " + str(cube(3)))
parameterizedFunction(10, 20)
maxnumber(10, 20)
print(maxofThreenums(10, 30, 50))

print(2**4)
print("Finish")

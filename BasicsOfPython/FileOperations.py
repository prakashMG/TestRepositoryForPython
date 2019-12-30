import random
# a- append, r- read, w- over write

emp_file = open("EmployeeList.txt", "r")
print(emp_file.readable())

print(emp_file.readline(1))  # number of charecters in that line

print(emp_file.readlines())  # reads all line and save it in a list

for employee in emp_file.readlines():
    print("Hi :  " + employee)

emp_file.close()

emp_file = open("EmployeeList.txt", "a")
print(emp_file.readable())

emp_file.write("\nKelly  Customer service ")
#print(emp_file.readlines())
emp_file.close()

def roll_dice(num):
    return random.randint(1,num)
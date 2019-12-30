try:
    num1 = float(input("Enter a number: "))
    print(num1)
    print(10 / 0)
except ZeroDivisionError as err:
    print("error message is : " + str(err))

except FileExistsError as fileError:
    print("File was not exist is the required folder, please chahnge the file location : " + fileError)



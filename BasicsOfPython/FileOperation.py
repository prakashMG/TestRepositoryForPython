
"""
my_file=open("Textfile.txt","r+")
my_file.write("Entered line with read/write option\n")
my_file.close()


my_file=open("Textfile.txt","w")
my_file.write("Entered line")
my_file.close()
"""


my_file=open("Textfile.txt","a")
my_file.write("\nEntered line with append option")
my_file.close()



my_file=open("Textfile.txt","r")
#print(my_file.readline())
#print(my_file.read())
my_file.close()

with open("Textfile.txt","a") as with_as_writeFile:
    print("With as Write option started ")
    with_as_writeFile.writelines("Entered line with as option ")

with open("Textfile.txt","r") as with_as_readfile:
    print("with as read option started========= \n")
    print(with_as_readfile.read())





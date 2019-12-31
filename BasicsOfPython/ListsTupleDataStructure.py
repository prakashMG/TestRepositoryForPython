"""
#list[]
nameList=["Abc","Def","Ghi"]
print(nameList)

householdList= ["table","chair",["cot", "bed","pillows"],10,20]
print(householdList)
print(householdList[2])
print(householdList[-2])
#You can add range
print(householdList[1:3])

listNumbers=[10,40,30,10,80,60]
frenList=["Abc","Def","Ghi"]
frenList.append("Jkl")
frenList.insert(0,"Xyz")
print(frenList)
frenList.remove("Ghi")
print(frenList)
print("Pop operations : "+frenList.pop())
print("Sorting")
listNumbers.sort()
print(listNumbers)
listNumbers.reverse()
print(listNumbers)
coplist=listNumbers
print("copylist")
print(coplist)


#tuples () immutablt : u can not add remove
sampleTuple=(10,20,30,40)
print(sampleTuple)
print(sampleTuple[1])
print(sampleTuple.__contains__(10))

#list of tuples
listCoordinates=[(10,20),(30,40),(50,60),(70,80)]
print(listCoordinates)
listCoordinates.insert(0,(0,10))
listCoordinates.pop(1)
listCoordinates.insert(1,(10,20,30,40))
print(listCoordinates)

"""
#Dictionaries : It always have key value pair

dictMonth={"Jan": "January", "Feb": "February", "Mar": "March"}
print(dictMonth["Feb"])
print(dictMonth.get("Jan"))
print(dictMonth)

i=1
while i<=10:
    print(i)
    i=i+1

print("finished while loop")



















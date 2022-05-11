'''
NAME:HARIHARAN P
DATE:11/05/2022
'''
#Note: In the question,example input were lists 
inputlist = []

n = int(input("no of elements u require in the list/range : "))
print("\n enter the values ") 
for i in range(0, n):
    value= float(input())
    inputlist.append(value)

for value in inputlist:
    if value >= 0:
       print(value, end = " ")     
'''
creating new list from existing list 
filtring list 
modifying list 

'''
import math
numbers=[20,30,54,65,95,47,22,35,20,87,99,65,85,74,69]
oddeven=[0 if i%2==0 else 1 for i in numbers]
print(oddeven)

digits=["two" if i>=10 and i>99 else "one" for i in numbers]
#print(digits)

numbers=[i*i for i in range(50)]
print(numbers)
sqrts=[round (math.sqrt(i),2) for i in range (0,1000,5)]
print(sqrts)

s,e=map(int,input("enter start and end:").split())
n,m=map(int,input("enter the numbers to divide:").split())
l=[i for i in range(s,e) if i%n==0 and i%m==0]
#print(l)

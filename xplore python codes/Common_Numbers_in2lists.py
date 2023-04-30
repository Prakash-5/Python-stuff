# Python Program to take 2 lists as input which contain numbers as input and return another list with the common numbers in those lists


def find_common_numbers(l1,l2):
    l3=[elem for elem in l1 if elem in l2]
    return l3

n=int(input())
l1=[]
for i in range(n):
    l1.append(int(input()))
    
m=int(input())
l2=[]
for j in range(m):
    l2.append(int(input()))
    
common_numbers=find_common_numbers(l1,l2)

if len(common_numbers)==0:
    print("No Common Numbers")
else:
    print("Common Numbers:",common_numbers)

# The program will take input from the user in the form of a string and will pass the string as an argument to a function. The function will take the strings as arguments and return the Position(or index) of the list if the passed string is present in the list, else it’ll return “String not found”. If the passed strings are present at multiple indices, in that case, the function should only return The first index of occurrence.

# Considering the above scenario into account, build the logic to print the position of the passed string from a given list of strings.

# Refer to the below instructions and sample input-Output for more clarity on the requirement.

# Input:

# 4

# Hello Good Morning

# abcd123Fghy

# India

# Progoti.c

# India

def isPresent(lis,st):

    for i in range(0, len(lis)):

        if lis[i] == st:

            return i

lis = []

for j in range(int(input())):

    lis.append(input())

st = input()

ind = isPresent(lis,st)

if ind == -1:

    print("String not found")

else:

    print("Position of the searched string is:" ,ind)
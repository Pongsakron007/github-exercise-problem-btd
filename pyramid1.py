'''
input: 4

output:
*
**
***
****

'''

p = int(input())

for row in range(1,p+1):
    for column in range(0,row):
        print("*",end="")
    print(" ")

'''
คำอธิบาย
In Minecraft, players can use different kinds of blocks to create various buildings.
Given a valley with N blocks and each block has a length of L.
Pegura, a rookie vtuber, is wondering how deep the valley is.
Can you donate a superchat to tell her the height H ?

รูปเเบบ Input
Two integers N and L (1 <= N, L <= 1000) separated by a blank.

รูปเเบบ Output
The height H.
Note that you do not need to print '\n' at the end of the output.

ตัวอย่างที่1
Input:
6 6

Output:
36

ตัวอย่างที่2
Input:
7 5

Output:
35

ตัวอย่างที่3
Input:
80 10

Output:
800
'''
h, l = list(map(int, (input().split())))

print(h* l)

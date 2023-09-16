'''
คำอธิบาย
สร้าง sub array ภายใต้ input array หาผลรวมของ array และ sub array แล้วนำมารวมกันอีกทีนึง

ตัวอย่างเช่น

input: [2 5 5]
ผลรวม = 2 + 5 + 5 = 12

subArr1: [2 5]
ผลรวม = 2 + 5 = 7

subArr2: [5 5]
ผลรวม = 5 + 5 = 10

นำผลรวมของ array และ sub array มารวมกันเป็นคำตอบ
= 12 + 7 + 10 = 29 (คำตอบ)

รูปเเบบ Input
[2 5 5]: number[]

รูปเเบบ Output
29: number

ตัวอย่างที่1
Input:

2 5 8 5
Output:

53

ตัวอย่างที่2
Input:
2 5 5

Output:
29
'''
num = input()

num = num.split(" ")
num = [int(i) for i in num]

all_sub = []

for i in range(len(num)-1):
  sub = num[ i : i+2]
  all_sub.append(sum(sub))

all = sum(num) + sum(all_sub)

print(all)

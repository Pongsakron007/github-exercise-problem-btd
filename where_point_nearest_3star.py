'''
คำอธิบาย
มีจุด n จุดบนระนาบสองมิติ จงหากำลังสองของระยะห่างของจุดที่ใกล้กันมาดที่สุด
โดยระยะห่างของจุด (x,y) และ (a,b) ใดๆ เท่ากับ 

รูปเเบบ Input
บรรทัดแรกระบุจำนวนจุด n เป็นจำนวนเต็มบวก โดยที่ n>=2
บรรทัดที่สองถึงบรรทัดที่ n+1 แต่ละบรรทัดระบุพิกัดของแต่ละจุดเป็นจำนวนจริง 2 ตัว โดยมีช่องว่างคั่นระหว่างจำนวนทั้งสอง

รูปเเบบ Output
กำลังสองของระยะห่างของจุดที่ใกล้กันมากที่สุด

ข้อจำกัด
n เป็นจำนวนเต็ม โดยที่ n>=2

ตัวอย่างที่1
Input:
3
2 4
5 4
5 8

Output:
9.00

ตัวอย่างที่2
Input:
4
5.75 3
0 0.2
1 -9.33
-1 1.5

Output:
2.69

ตัวอย่างที่3
Input:
6
32 12
23.11 32
88.11 0.15
29.88 8.66
-32.43 12.12
17 32

Output:
15.65

'''
import math

num = int(input())
coordinate = [input().split() for i in range(num)]
coordinate = list(map(lambda x: (float(x[0]), float(x[1])), coordinate))


def dis_sqr(i, j):
  result = math.sqrt((i[0] - j[0])**2 + (i[1] - j[1])**2)
  return result

last = 10**4

for i in coordinate:
  for j in coordinate:
    if i != j:
      value = dis_sqr(i, j)
      last = min(last, value)
    
  
last = last **2
last = round(last, 2)

print(f"{last:.2f}")

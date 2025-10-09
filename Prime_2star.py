'''
คำอธิบาย
ให้เขียนโปรแกรม หาจำนวนเฉพาะตั้งแต่ a ถึง b

รูปเเบบ Input
บรรทัดแรก 	input a 
บรรทัดที่สอง 	input b

รูปแบบ Output
ให้ปริ้นจำนวนเฉพาะที่ตรงเงื่อนไขอยู่ในบรรทัดเดียวกันทั้งหมด ถ้าไม่มีให้ปริ้น None.

output: x x x x x 

ข้อจำกัด
0 < a, b < 100,000

ตัวอย่างที่ 1
ข้อมูลขาเข้า
1
11

ผลลัพธ์
2 3 5 7 11

ตัวอย่างที่ 2
ข้อมูลขาเข้า
10
21

ผลลัพธ์
11 13 17 19

ตัวอย่างที่ 3
ข้อมูลขาเข้า
90
96

ผลลัพธ์
None.
'''
import math
start, end = [int(input()) for i in range(2)]

def prime(n):
  for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
      return False
  return True

prime_num = []

def cal_prime(start, end):
  for i in range(start, end+1):
    if i < 2:
      continue
    elif prime(i):
      prime_num.append(i)

cal_prime(start, end)

str_prime_num = list(map(lambda x: str(x), prime_num))
result = " ".join(str_prime_num)

print(result)

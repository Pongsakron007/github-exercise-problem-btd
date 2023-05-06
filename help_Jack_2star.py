'''
คำอธิบาย
แจ็กเป็นคาวบอย แจ็กอยากเป็นนักคณิตศาสตร์แล้วสงไสว่า 2566! มี 0 ต่อท้ายทั้งหมดกี่ตัว ช่วยแจ็กด้วยช่วยแจ็กด้วย แจ็กสงไสจริงๆนะจ๊ะ

รูปเเบบ Input
บรรทัดที่ 1 รับตัวเลขจำนวนเต็มบวก N

รูปเเบบ Output
Number of N! have 0 of the end equal A

ข้อจำกัด
N >=0

ตัวอย่างที่1
Input:
2566

Output:
Number of 2566 factoria have 0 of the end equal 639

ตัวอย่างที่2
Input:
5

Output:
Number of 5 factoria have 0 of the end equal 1

ตัวอย่างที่3
Input:
20

Output:
Number of 20 factoria have 0 of the end equal 4
'''
import math

num = int(input())

fac_num = math.factorial(num)

str_f = list(str(fac_num))[::-1]

def cal(text):
  i = 0
  count = 0
  while text[i] == "0":
    i += 1
    count += 1
  return count

print(f"Number of {num} factoria have 0 of the end equal {cal(str_f)}")

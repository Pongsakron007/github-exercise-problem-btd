'''
คำอธิบาย
จงหาเขียนโปรเเกรมหาค่า Factorial โดยให้ผู้ใช้ input ค่าที่ต้องการหาได้

รูปเเบบ Input
input เป็นค่าจำนวนเต็มบวก หรือ เต็มศูนย์ อย่างเช่น 6

รูปเเบบ Output
เป็นจำนวนเต็มบวก อย่างเช่น 720

ข้อจำกัด
โดยใช้ recursive function

ตัวอย่างที่1
Input:
4

Output:
24

ตัวอย่างที่2
Input:
6

Output:
720

ตัวอย่างที่3
Input:
8

Output:
40320
'''
num = int(input())

def factorial(num):
  if num ==0:
    return 1
  elif num ==1:
    return num
  else:
    return num * factorial(num-1)
  
print(factorial(num))

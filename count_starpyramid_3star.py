'''
คำอธิบาย
เราได้สร้างพีระมิดด้วย * ซึ่งเราจะรับค่าของจำนวน * ของฐานพีระมิดและจะสร้างพีระมิดจากชั้นแรกและลดจำนวน * ลงที่ละ 2 เมื่อรับค่าเป็นจำนวนคี่แต่จะลดลงที่ละ1เมื่อรับค่าเป็นจำนวนคู่ซึ่งพีระมิดมีลักษะตัวอย่างแบบนี้

   *
  ***
 *****
*******
ซึ่งตอนนี้นั้นเราอยากจะรู้ว่ามีดาวทั้งหมดกี่ดวงจากการสร้างพีระมิดนี้

รูปเเบบ Input
input จำนวนดาวของฐานพีระมิดไว้ที่ตัวแปล B

รูปเเบบ Output
output เป็นจำนวนดาวทั้งหมดของพีระมิด ไว้ที่ตัวแปร X

ข้อจำกัด
B >=0
X >= 0

ตัวอย่างที่1
Input:
5

Output:
9

ตัวอย่างที่2
Input:
8

Output:
36

ตัวอย่างที่3
Input:
12

Output:
78
'''
py = int(input())

if py % 2 ==0:
  result = sum([i for i in range(py, 0, -1)])
  print(result)
else:
  result = sum([i for i in range(py, 0, -2)])
  print(result)

'''
คำอธิบาย
ในโจทย์ข้อนี้เราจะรับจำนวน 2 จำนวนและให้คุณเทียบจำนวนสองจำนวนว่าจำนวนใดมีค่ามากกว่ากัน (แสดงจำนวนที่มากกว่าออกมา) โดยถ้าสองจำนวนนี้เท่ากันให้แสดงคำว่า "E"

รูปเเบบ Input
รับค่าจำนวนจริง 2 จำนวน (อาจเป็นทศนิยม)

รูปเเบบ Output
ข้อมูลส่งออก คือ จำนวนที่มากกว่า ถ้าเท่ากันให้แสดงคำว่า "E"

ข้อจำกัด
ข้อมูลนำเข้าอาจติดลบได้

ตัวอย่างที่1
Input:
5
7

Output:
7

ตัวอย่างที่2
Input:
9
20

Output:
20

ตัวอย่างที่3
Input:
100
100

Output:
E
'''
num1, num2 = [input() for i in range(2)]
num3, num4 = float(num1), float(num2)

if num3 > num4:
  print(num1)
elif num4 > num3:
  print(num2)
else:
  print("E")

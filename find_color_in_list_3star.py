'''
คำอธิบาย
ต้องการหาสี ที่มีอยู่ในสต๊อก ที่เรามีทั้งหมดโดยสีที่มีคือ สีแดง สีเขียน สีน้ำเงิน สีดำ สีเหลือง ['RED', 'GREEN', 'BLUE', 'BLACK', 'YELLOW'] ตามลำดับ

รูปเเบบ Input
เลือกสีต้องการหา 1 สี อย่าง สีเหลือง Yellow แฮร่!

รูปเเบบ Output
พบข้อมูลสี YELLOW ใน list ลำดับที่ 4

ตัวอย่างที่1
Input:
RED

Output:
found RED color in list No. 0

ตัวอย่างที่2
Input:
PINK

Output:
not found PINK color in list
'''
list_color = ['RED', 'GREEN', 'BLUE', 'BLACK', 'YELLOW'] 

color = input()

def find_color(color):
  for i in list_color:
    if i == color:
      return color, list_color.index(i)
  return False, None
    
result = find_color(color)

if result == (False, None):
  print(f"not found {color} color in list")
else:
  print(f"found {color} color in list No. {result[1]}")

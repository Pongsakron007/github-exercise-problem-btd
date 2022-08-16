'''
คำอธิบาย

เด็กชายเป็ดน้อยต้องการหาค่าเฉลี่ยของข้อมูลโดยแสดงผลเป็นค่าเฉลี่ยโดยมีทศนิยม 2 ตำแหน่ง

รูปเเบบ Input

รับค่าจำนวนจริงบวกเรื่อย ๆ จนกว่าจะพบค่าติดลบหรือศูนย์

รูปเเบบ Output

ค่าเฉลี่ยของ input ทั้งหมด ยกเว้นจำนวนที่ติดลบหรือศูนย์
หากรับมาจำนวนแรกเป็นลบหรือศูนย์ให้แสดงข้อความว่า No Data

ข้อจำกัด
ตัวอย่างที่1
Input:

11
12
13
-1
Output:
12.00

ตัวอย่างที่2
Input:
123.45
32.87
89.6673
1234.5678
-5.654

Output:
370.14

ตัวอย่างที่3
Input:
-4

Output:
No Data
'''
get_v = []
while True:
  v = float(input())
  if v >0:
    get_v.append(v)
  else:
    break

if len(get_v) == 0:
  print("No Data")
else:
  result = sum(get_v)/len(get_v)
  print("{:.2f}".format(result))
#print(get_v)
  

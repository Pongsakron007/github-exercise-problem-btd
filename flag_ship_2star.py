'''
คำอธิบาย
จงสร้างธงของเรือใบโดยมีความสูงเท่ากับค่าที่รับมา(เป็นโจทย์แรกที่ผมเขียนนะครับถ้าไม่ดียังไงติชมได้ครับผมจะแก้ไขให้ครับ)

รูปเเบบ Input
บรรทัดที่1 รับค่าความสูงของธง

กำหนดให้ 20>h>1
รูปเเบบ Output

วาดรูปธงโดยใช้ความสูงจากinput บรรทัดที่1
ทำธงในรูปแบบของสามเลี่ยม

ข้อจำกัด
ต้องรับค่าintegerเท่านั้นถ้านอกเหนือจากนั้นเช่น
ใส่string มาให้แสดงผลว่า ERROR please input integer only
ถ้าใส่h=1มาให้ แสดงผลว่า ERROR please input more than 1

ตัวอย่างที่1
Input:
6

Output:

|\
| \
|  \
|   \
|    \
|=====\

ตัวอย่างที่2
Input:
2

Output:
|\
|=\

ตัวอย่างที่3
Input:
r

Output:
ERROR please input integer only
'''

try:
  num = int(input())
  if num <= 1:
    print("ERROR please input more than 1")
  else:
    for i in range(num+1):
      if i < num-1:
        print("|" + " "*i + "\\")
      elif i == num:
        print("|" + "="*(num-1) + "\\")
except:
  print("ERROR please input integer only")

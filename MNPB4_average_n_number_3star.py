'''
คำอธิบาย
ในข้อนี้เราจะให้คุณหาค่าเฉลี่ยของจำนวน n จำนวน

รูปเเบบ Input
ข้อมูลนำเข้ามี n+1 บรรทัด
บรรทัดที่ 1 รับค่า n
บรรทัดที่ 2 ถึง n+1 รับค่าจำนวนจริง n จำนวน

รูปเเบบ Output
ข้อมูลส่งออก คือ ค่าเฉลี่ยของจำนวนทั้ง n จำนวน

ข้อจำกัด
n เป็นจำนวนธรรมชาติ

ตัวอย่างที่1
Input:
3
20
30
50

Output:
33.33

ตัวอย่างที่2
Input:
5
100
100
200
500
600

Output:
300

ตัวอย่างที่3
Input:
1
90

Output:
90
'''
import decimal
decimal.getcontext().prec = 30

num = int(input())
values = [input() for i in range(num)]

last_values = []
for i in values:
  if "." in i:
    i = float(i)
    last_values.append(i)
  else:
    if int(i)> 10**10:
      i = decimal.Decimal(i)
      last_values.append(i)
    else:
      i = int(i)
      last_values.append(i)
    
total = round(sum(last_values) / num,1) 

if total%1 ==0:
  print(int(total))
else:
  print(total)

'''
คำอธิบาย
กำหนดว่า
Good morning ใช้ได้ตอนเวลา 5:00 - 11:59
Good afternoon ใช้ได้ตอนเวลา 12:00 - 17:59
Good evening ใช้ได้ตอนเวลาหลัง 18:00 ขึ้นไป

รูปเเบบ Input
บรรทัดแรก:
รับค่าเวลามา ชั่วโมง นาที โดยคั่นด้วย เครื่องหมาย Colon ( : )

บรรทัดที่สอง:
รับชื่อ User

รูปเเบบ Output
แสดงผล คำทักทาย แล้วตามด้วยชื่อ User

ตัวอย่างที่1
Input:
13:59
Sommai

Output:
Good afternoon, Sommai

ตัวอย่างที่2
Input:
19:53
Sky

Output:
Good evening, Sky

ตัวอย่างที่3
Input:
7:00
Eleven

Output:
Good morning, Eleven
'''
hr, m = input().split(":")
name = input()
hr, m = int(hr), int(m)

if int(hr) >= 5 and int(hr) < 12:
  print(f"Good morning, {name}")
elif int(hr) >= 12 and int(hr) < 18: 
  print(f"Good afternoon, {name}")
else:
  print(f"Good evening, {name}")

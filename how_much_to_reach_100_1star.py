'''
คำอธิบาย
สร้างโปรแกรมตรวจสอบอายุของผู้ใช้ ว่าอายุที่กรอกมานั้นจะต้องใช้เวลาอีกกี่ปี อายุของเขาผู้นั้นจะถึง 100 ปี

รูปเเบบ Input
บรรทัดที่ 1 รับชื่อของผู้ใช้ บรรทัดที่ 2 รับอายุปัจจุบัน

รูปเเบบ Output
แสดงชื่อที่ผู้ใช้กรอก พร้อมข้อความ ชื่อผู้ใช้, you will turn 100 in n years. -- โดย n ผลลัพธ์

ข้อจำกัด
อายุต้องอยู่ระหว่าง 0 - 100

ตัวอย่างที่1
Input:
Day
34

Output:
Day, you will turn 100 in 66 years.

ตัวอย่างที่2
Input:
Prayoot
65

Output:
Prayoot, you will turn 100 in 35 years.

ตัวอย่างที่3
Input:
Tiger
2

Output:
Tiger, you will turn 100 in 98 years.
'''
name, age = [input() for i in range(2)]
age = int(age)

print(f"{name}, you will turn 100 in {100 - age} years.")

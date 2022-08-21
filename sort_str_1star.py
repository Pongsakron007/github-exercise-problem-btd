'''
คำอธิบาย
เรียงข้อความจากความยาวน้อยไปความยาวมาก

รูปเเบบ Input
บรรทัดแรก รับค่าจำนวนข้อความ
บรรทัดต่อไป ข้อความที่ต้องการจัดเรียง

รูปเเบบ Output
ข้อความที่ถูกเรียงความยาวจากน้อยไปมาก

ข้อจำกัด
จำนวนข้อความไม่เกิน 50 ข้อความ

ไม่มีข้อความที่มีความยาวเท่ากัน

ตัวอย่างที่1
Input:
3
python
java
javascript

Output:
java
python
javascript

'''

num = int(input())

get = [input() for i in range(num)]

sort_list = sorted(get,key=len)
for item in sort_list:
  print(item)

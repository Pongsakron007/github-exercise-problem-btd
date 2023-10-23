'''
คำอธิบาย
โปรแกรมถอดรหัสลับ โดยรับค่ารหัสลับแล้วทำการถอดรหัส
รูปเเบบ Input
รับค่ารหัสลับ H23EL09LO8 (String)

รูปเเบบ Output
รหัสที่ถอดได้ คือ HELLO

ข้อจำกัด
ข้อมูล Input เป็น String

ตัวอย่างที่1
Input:
H23EL09LO8

Output:
HELLO

ตัวอย่างที่2
Input:
5H43E5L2P

Output:
HELP 

ตัวอย่างที่3
Input:
19RO11O8M3

Output:
ROOM
'''
code  = input()

def decode(code):
  result = ""
  for text in code:
    if not text.isdigit():
      result += text
  return result

print(decode(code))

'''
คำอธิบาย
เมื่อเกิดสงครามต้องมีเหล่าทหารนักกล้าออกรบ สิ่งสำคัญคือการสื่อสารเพื่อให้เป็นไปตามยุทธวิธีสงความที่ได้วางแผนไว้
นายพลเลือกท่านให้เป็นหน่วยทหารคอยรับคำสั่งจากนายพล เพราะฉะนั้นท่านต้องแปลงข้อความที่ได้รับมาให้เป็นข้อความหรือคำสั่งเพื่อใช้ในการปฎิบัติการ

โดยมีโจทย์ดังนี้

ข้อความที่ได้รับ
ข้อความที่ได้รับ q T R K W G T
ลดตำแหน่งข้อความลงมาตามตำแหน่ง
ตำแหน่ง 1 2 3 4 5 6 7
ข้อความที่ได้ p R O G R A M
หลังจากนั้นสลับตำแหน่งจากใหญ่ไปเล็ก จากเล็กไปใหญ่
ข้อความที่ได้ P r o g r a m
ได้รับโจทย์มาแล้ว พลทหารเตรียมพร้อม ออกรบได้!!!

Hint: ASCII code number

รูปเเบบ Input
qTRKWGT เป็นข้อความที่อ่านไม่ออก

รูปเเบบ Output
Program อ่านออกแล้ววววว

ตัวอย่างที่1
Input:
fPHQ^

Output:
Enemy

ตัวอย่างที่2
Input:
bTH}T[{PN\\P

Output:
AreYouThere

ตัวอย่างที่3
Input:
xCURNTN

Output:
Warning
'''

string = input()

def  decode(string):
  result = ""
  for idx, i in enumerate(string):
    new_str = chr(ord(i) - idx-1)
    result += new_str
  result = result.swapcase()  
  return result

print(decode(string))

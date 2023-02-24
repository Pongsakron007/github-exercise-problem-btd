'''
คำอธิบาย
ให้หาว่าใครตั้ง Password ที่ยากที่จะถูก hack จากผู้ไม่ประสงค์ดีมากที่สุด ระหว่าง Man, Non และ Miv ตามลำดับ โดยมีเกณฑ์ในการตั้ง Password ที่ดีดังนี้
ตัวอักษร a-z อย่างน้อย 1 ตัว
ตัวเลข 0-9 อย่างน้อย 1 ตัว
ตัวอักษร A-Z อย่างน้อย 1 ตัว
ตัวอักษรพิเศษ $ หรือ # หรือ @ อย่างน้อย 1 ตัว
ความยาวไม่น้อยกว่า 6 ตัว และ ไม่มากกว่า 12 ตัว

รูปเเบบ Input
Password ของทั้งสามคน Man, Non, และ Miv ตามลำดับ

รูปเเบบ Output
Password ที่ตรงตามเกณฑ์ และ เจ้าของ Password นั้น

ข้อจำกัด
มีแค่คนเดียวที่ตั้ง Password ตรงตามเกณฑ์ที่กำหนด

ตัวอย่างที่1
Input:
ABd1234@1,a F1#2w3E*,2We3345

Output:
ABd1234@1 (Man)
'''
from collections import Counter
import string

Man, Non, Miv = input().split(",")

def low(people):
  for i in people:
    if i in string.ascii_lowercase:
      return True
  return False
  
def  digit(people):
  for i in people:
    if i in string.digits:
      return True
  return False

def up(people):
  for i in people:
    if i in string.ascii_uppercase:
      return True
  return False
  
def punc(people):
  for i in people:
    if i in ["$", "#", "@"]:
      return True
  return False
  
def long(people):
  if len(people) > 6 and len(people) < 12:
    return True
  return False

point = {"Man": [low(Man) + digit(Man) + up(Man) + punc(Man) + long(Man), Man],
              "Non": [low(Non) + digit(Non) + up(Non) + punc(Non) + long(Non), Non],
               "Miv": [low(Miv) + digit(Miv) + up(Miv) + punc(Miv) + long(Miv), Miv]}

right_man = max(point, key = point.get)
#sort_man = sorted(point.items(), key = lambda x:x[1])
print(f"{point[right_man][1]} ({right_man})") 

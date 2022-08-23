'''
คำอธิบาย
ให้แยกตัวอักษรที่เป็นสระของภาษาอังกฤษออกมาจากคำที่กำหนด

รูปเเบบ Input
บรรทัดแรก ข้อความที่ต้องการแยกสระ

รูปเเบบ Output
บรรทัดแรก ตัวตัวอักษรที่เป็นสระของภาษาอังกฤษ
บรรทัดสอง ตัวอักษรที่เหลือไม่รวมเครื่องหมายและช่องว่าง

ข้อจำกัด
ความยาวของ input ไม่เกิน 100 ตัวอักษร

ตัวอย่างที่1
Input:
My feelings are overwhelmed by you.

Output:
eeiaeoeeeou
Myflngsrvrwhlmdbyy
'''
import re
text = input()
if text[-1] == ".":
  text = text[:-1]
regex = re.findall("[aeiouAEIOU]", text)
regex_sp  = re.findall("[#@!,]", text)
chars = []
for i in text:
  if i !='a':
    if i !='e':
      if i !='i':
        if i !='o':
          if i !='u': 
            if i !='A': 
              if i !='E': 
                if i !='I': 
                  if i !='O': 
                    if i !='U':
                      if i != "#":
                        chars.append(i)
for i in chars:
  if i ==" ":
    chars.remove(i)
for i in chars:
  if i in regex_sp:
    chars.remove(i)
print("".join(regex))
print("".join(chars))

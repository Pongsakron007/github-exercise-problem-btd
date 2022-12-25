'''
คำอธิบาย
ทำการแบ่งประโยคจากคำที่กำหนดให้ โดยให้แบ่งขึ้นบรรทัดใหม่ทุกครั้งที่แบ่ง

รูปเเบบ Input
บรรทัดแรก ประโยคหลักที่ต้องการแบ่ง
บรรทัดสอง คำที่ต้องการใช้แบ่งประโยค

รูปเเบบ Output
หลายบรรทัด แสดงประโยคทั้งหมดที่ถูกแบ่ง

ข้อจำกัด
คำที่ใช้แบ่งจะไม่อยู่ที่ ตัวแรก หรือตัวสุดท้ายของประโยค

ตัวอย่างที่1
Input:
This is very easy testcase.
a

Output:
This is very ea
asy testca
ase.

ตัวอย่างที่2
Input:

Devices have been used to aid computation for thousands of years.
i

Output:
Devi
ices have been used to ai
id computati
ion for thousands of years.

ตัวอย่างที่3
Input:
Early computing machines had fixed programs.
a

Output:
Ea
arly computing ma
achines ha
ad fixed progra
ams.
'''
message, word = [input() for i in range(2)]


list_m = message.split(word)

result_list =[]
for idx, i in enumerate(list_m):
  if idx == 0:
    i += word
    result_list.append(i)
  elif idx > 0 and idx < len(list_m) -1:
    i = word+ i + word
    result_list.append(i)
  elif idx == len(list_m) -1:
    i = word + i
    result_list.append(i)
    
for i in result_list:
  print(i)

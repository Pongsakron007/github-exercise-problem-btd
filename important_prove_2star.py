'''
คำอธิบาย
ตำรวจต้องการข้อมูลผู้ร้ายจากคุณเพราะคุณเป็นพยานในเหตุการณ์
คำตอบของคุณจะเป็น

T = true
F = false
DS = doesn't see

รูปเเบบ Input
ลักษณะ : ข้อมูล
ลักษณะที่ตำรวจถาม : ข้อมูล

รูปเเบบ Output
T/F/DS

ข้อจำกัด
ลักษณะ และ ลักษณะที่ตำรวจถาม มีอย่างละ 1 บรรทัด
ลักษณะ มี ' ' อยู่ระหว่าง ':'

ตัวอย่างที่1
Input:
hat color : red
hat color : red

Output:
T

ตัวอย่างที่2
Input:
glasses : have
glasses : doesn\'t have

Output:
F

ตัวอย่างที่3
Input:
hair : wavy
shoe : boot

Output:
DS
'''
inform = [input() for i in range(2)]

list_inform = []
for item in inform:
  name, property_item = item.split(" : ")
  list_inform.append((name, property_item))
  
if list_inform[0] == list_inform[1]:
  print("T")
elif list_inform[1][1] == "doesn\'t have":
  print("F")
elif list_inform[0][0] == list_inform[1][0]:
  if list_inform[0][0] != list_inform[1][1]:
    print("F")
else:
  print("DS")

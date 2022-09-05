'''
คำอธิบาย
รับตัวเลขจำนวนเต็มจนกว่าจะเจอเลข 0 จากนั้นหาว่ามีกี่จำนวณ และค่ามากที่สุดและน้อยที่สุดคืออะไร

รูปเเบบ Input
รับค่าแบบจำนวณเต็ม และหยุดเมื่อเจอเลข 0

รูปเเบบ Output
บรรทัดที่ 1 แสดงจำนวณทั้งหมด (ไม่นับเลข 0 ตัวสุดท้าย)
บรรทัดที่ 2 แสดงค่าที่มากที่สุด
บรรทัดที่ 3 แสดงค่าที่น้อยที่สุด

ตัวอย่างที่1
Input:
1
2
3
4
5
0
Output:
Total : 5
Maximum : 5
Minimum : 1
'''


b = []
while True:
  a = int(input())
  if a ==0:
    break
  else:
    b.append(a)
    
print(f"Total : {len(b)}")
if len(b) ==0:
  print("Maximum : 0")
else:
  print(f"Maximum : {max(b)}")

if len(b) ==0:
  print("Minimum : 0")
else:
  print(f"Minimum : {min(b)}")

'''
คำอธิบาย
เนื้อเรื่อง
ปิ๊กมีผ้าผืนหนึ่ง เป็นลายตารางที่มี Pattern แบบชัดเจน ปิ๊กอยากรู้ว่าถ้าดูลายผ้าขนาด n*n แล้วเลื่อนซ้าย เลื่อนขวา ลายที่ปิ๊กเห็นจะเป็นแบบไหน

โจทย์
จงแสดงลายที่ปิ๊กเห็น

รูปเเบบ Input
บรรทัดที่ 1 รับค่า n (พื้นที่ลายที่ปิ๊กต้องการดู) และค่า m (จำนวนการเลื่อน)
บรรทัดที่ 2 ถึง m รับค่าการเลื่อน เช่น
-2 (คือเลื่อนซ้ายไปขนาด 2 หน่วย)
4 (คือเลื่อนขวาไปขนาด 4 หน่วย)

รูปเเบบ Output
ลายที่ปิ๊กเห็น โดยตัวแรกเริ่มจาก * และสลับไปเป็น - เรื่อยๆ (ระหว่างตัวอักษรให้เว้นวรรค 1 ครั้ง)

ข้อจำกัด
0 < n < 1000
0 < l < 10

ตัวอย่างที่1
Input:
4 2
-1 
-2

Output:
- * - * 
* - * - 
- * - * 
* - * -

ตัวอย่างที่2
Input:
4 2
2 
2

Output:
* - * - 
- * - * 
* - * - 
- * - * 

ตัวอย่างที่3
Input:
2 5
2 
-1 
-4 
5 
9

Output:
- * 
* - 
'''
row, s =[int(i) for i in input().split(" ")]

all_new_s = []



try:
  while True:
    new = input()
    try:
      new = int(new)
      all_new_s.append(new)
    except:
      new = new.split(" ")
      new = list(map(int, new))
      all_new_s.extend(new)
except:
  pass
  

total_s = sum(all_new_s) 


if total_s % 2==0:
  for i in range(row):
    for j in range(row):
      if  (i + j) % 2 ==0:
        print("* ", end="")
      else:
        print("- ", end="")
    print("")
else:
  for i in range(row):
    for j in range(row):
      if  (i + j) % 2 ==0:
        print("- ", end="")
      else:
        print("* ", end="")
    print("")

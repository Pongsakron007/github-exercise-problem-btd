'''
กฏของการเขียนเลขโรมัน คือ ห้ามเขียนตัวเดียวกันซ้ำมากกว่า 3 ครั้ง
ตัวอย่าง:
IIII = ❌
IV = ✅

โจทย์ จงเขียนโปรแกรมว่าเลขโรมันที่ ผู้ใช้งาน กรอกเข้าไปถูกต้องหรือไม่
หากถูกต้องให้แสดงผลคำว่า
'Correct'

หากไม่ถูกต้องให้แสดงผลคำว่า
'Not Correct'

รูปเเบบ Input
บรรทัดแรก รับค่าเลขโรมัน

รูปเเบบ Output
แสดงผลคำว่า ผู้ใช้กรอกเลขโรมันได้ถูกต้องหรือไม่

ตัวอย่างที่1
Input:
IIII

Output:
Not Correct

ตัวอย่างที่2
Input:
IV

Output:
Correct

ตัวอย่างที่3
Input:
III

Output:
Correct
'''
num_r = input()
list_r = []
most = max(num_r, key=num_r.count)

for i in num_r:
  if i == most:
    list_r.append(i)

if len(list_r) > 3:
  print("Not Correct")
else:
  print("Correct")

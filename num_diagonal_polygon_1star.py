'''
คำอธิบาย
การหาเส้นทแยงมุมในรูปหลายเหลี่ยมเป็นทักษะที่จำเป็นในการพัฒนาคณิตศาสตร์ ในตอนแรกอาจดูเหมือนยาก แต่ก็ค่อนข้างง่ายเมื่อคุณเรียนรู้สูตรพื้นฐานเส้นทแยงมุมคือส่วนของเส้นตรงที่ลากระหว่างจุดยอดของรูปหลายเหลี่ยมที่ไม่มีด้านข้างของรูปหลายเหลี่ยมนั้นรูปหลายเหลี่ยมคือรูปร่างใด ๆ ที่มีมากกว่าสามด้าน คุณสามารถคำนวณจำนวนเส้นทแยงมุมในรูปหลายเหลี่ยมไม่ว่าจะมี 4 ด้านหรือ 4,000 ด้าน

รูปเเบบ Input
บรรทัดที่ 1 รับค่า N ที่เป็นจำนวนเต็ม //n = จำนวนเหลี่ยม

รูปเเบบ Output
number of squares n

Diagonal : x
ข้อจำกัด
n > 4

ตัวอย่างที่1
Input:

Output:
number of squares 8
Diagonal : 20.0

ตัวอย่างที่2
Input:
95

Output:
number of squares 95
Diagonal : 4370.0

ตัวอย่างที่3
Input:
1

Output:
The number of squares must be greater than 4.
'''
num = int(input())
num_di = (lambda x: (x*(x-3))/2)(num)


if num < 3:
  print("The number of squares must be greater than 4.")
else:
  print(f"number of squares {num}")
  print(f"Diagonal : {num_di}")

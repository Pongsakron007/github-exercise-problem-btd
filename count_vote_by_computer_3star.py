'''
คำอธิบาย
ณ โรงเรียนแห่งหนึ่งกำลังจะมีการสมัครเลือกประธานนักเรียนคนใหม่ โดยใช้ ระบบเสียงข้างมาก คณะครูทั้งหลายไม่อยากที่จะค่อยๆ นับคะแนนเสียงด้วยตนเองเนื่องจากทำให้เสียเวลามากเกินจำเป็นจึงอยากได้วิธิการนับแบบใหม่ก็คือ การนับโดยใช้ภาษาคอมพิวเตอร์เข้ามาช่วย

รูปเเบบ Input
บรรทัดแรก รับค่าของจำนวนผู้สมัคร และ จำนวนผู้ลงคะแนนโหวตขั้นด้วยเว้นวรรค
บรรทัดที่สอง ใส่หมายเลขของผู้สมัครโดยจะไม่เกินจำนวนผู้สมัคร และจำนวนคะแนนเสียงก็จะไม่เกินจำนวนของคนที่มาลงคะแนน แต่ละตัวขั้นด้วยเว้นวรรค

รูปเเบบ Output
บรรทัดแรก บอกหมายเลขที่ได้รับผลโหวตมากที่สุด
บรรทัดที่สอง บอกจำนวนผลโหวตที่ได้รับ

ตัวอย่างที่1
Input:
5 10
1 1 1 1 1 4 5 2 3 1

Output:
The number of candidates who received the most votes. : 1
The number of votes received is : 6

ตัวอย่างที่2
Input:
2 20
1 1 2 2 2 1 1 1 1 1 2 1 2 2 2 2 1 2 2 2

Output:
The number of candidates who received the most votes. : 2
The number of votes received is : 11

ตัวอย่างที่3
Input:
4 5
1 4 2 3 4

Output:
The number of candidates who received the most votes. : 4
The number of votes received is : 2
'''
from collections import Counter


cand, votter = input().split(" ")
point = input().split(" ")

cand, votter = int(cand), int(votter)
count_point = Counter(point)
count_point = dict(count_point)
max_id = max(count_point, key = count_point.get)

print(f"The number of candidates who received the most votes. : {max_id}")
print(f"The number of votes received is : {count_point[max_id]}")
#print(count_point[max_id])

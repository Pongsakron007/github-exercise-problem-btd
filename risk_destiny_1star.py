'''
คำอธิบาย
บทนำ
เมื่อคืนน้องจอยฝันดี ว่าตัวเองถูกล็อตตารี่รางวัลที่1ในฝัน
และน้องจอยก็จำเลขทุกตัวได้อย่างแม่นว่ามันคือเลข 8, 14, 112, 76, 2 เมื่อตืนจากฝัน
น้องจอยเลยลองเขียนโปรแกรมสำหรับวัดดวงของตัวเอง

โจทย์
จงเขียนโปรแกรมรับค่าจากผู้ใช้ 5 ตัว หากมีตัวเลข"อย่างน้อย" 3 ตัว ตรงกับตัวเลขหวยในฝันของน้องจอย ให้แสดงผลลัพธ์ว่า You are lucky แต่ถ้าไม่ ให้แสดงว่า You are unlucky

รูปเเบบ Input
รับตัวเลขจำนวนเต็ม 5 ตัว ที่ไม่ซ้ำกัน

รูปเเบบ Output
แสดงข้อความ string

ตัวอย่างที่1
Input:
1
2
3
4
5

Output:
You are unlucky
'''
list_a = [8, 14, 112, 76, 2]

get = [int(input()) for i in range(5)]
result = []
for i in list_a:
  if i in get:
    result.append(i)
    
if len(result) >= 3:
  print("You are lucky")
else:
  print("You are unlucky")

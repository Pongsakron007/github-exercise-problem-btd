'''
คำอธิบาย
สร้างฟังก์ชั่นที่หาความแตกต่างของ array 2 ชุดที่ประกอบไปด้วยตัวเลข และเรียงจากน้อยไปมาก

รูปเเบบ Input
บรรทัดที่ 1 รับ array ชุดแรก
บรรทัดที่ 2 รับ array ชุดที่สอง

เช่น
[100, 0, 1, 10]
[0, 1, 5, 10]

รูปเเบบ Output
[ 5, 100 ]

ข้อจำกัด
ทั้งสอง array จะต้องมี element อย่างน้อย 1 ตัว และแต่ละ element ใน array จะต้องมีค่ามากกว่า 0
Hint: JSON method
ตัวอย่างที่1
Input:
[1]
[10]

Output:
[ 1, 10 ]

ตัวอย่างที่2
Input:
[5, 0, 7]
[0, 1, 5]

Output:
[ 1, 7 ]

ตัวอย่างที่3
Input:
[5, 50, 25, 2]
[2, 25, 7]

Output:
[ 5, 7, 50 ]
'''
a = input().rstrip("]").lstrip("[").split(",")
b = input().rstrip("]").lstrip("[").split(",")

a = [int(i) for i in a]
b = [int(i) for i in b]

a, b = set(a), set(b)
c = a.difference(b)
d = b.difference(a)

e = (list(c) + list(d))
e.sort()
e = [str(i) for i in e]
result = ", ".join(e)
print(f"[ {result} ]")

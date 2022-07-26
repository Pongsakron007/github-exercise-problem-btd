'''
คำอธิบาย
เราจะสมมติว่าคีย์บอร์ดเรากำลังเล่นเกมอยู่ โดยที่
w = ขึ้น
a = ซ้าย
s = ล่าง
d = ขวา
แล้วเราแสดงผลออกมาว่า เราไปทางไหน
โจทย์จะให้ 4 ชุดปุ่ม ต่อ 1 test

รูปเเบบ Input
w หรือ a หรือ s หรือ d
โดยแต่ละ test จะสุ่มมา 4

ตัวอย่าง (ตรงกับ ตัวอย่าง output ด้านล่างนะ)
a
w
a
a

รูปเเบบ Output
ออกมาเป็นลูกศร โดย
w จะออกมาเป็น ^
a จะออกมาเป็น <
s จะออกมาเป็น v ( ตัว v (วี) )
d จะออกมาเป็น >

เมื่อจบ 1 ปุ่มแล้วขึ้นบรรทัดใหม

<
^
>
>

ข้อจำกัด
โจทย์จะให้ 4 ชุดปุ่ม ต่อ 1 test

ตัวอย่างที่1
Input:
w
w
s
d

Output:
^
^
v
>
'''

def direction():
  for i in range(4):
    direct = input()
    if direct =="w":
      print("^")
    elif direct =="a":
      print("<")
    elif direct =="s":
      print("v")
    elif direct =="d":
      print(">")
      
if __name__ == "__main__":
  direction()

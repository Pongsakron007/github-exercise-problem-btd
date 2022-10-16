'''
คำอธิบาย
สร้าง pattern จัตุรัส ตามขนาด nxn ที่รับจากinput แต่มีรายละเอียดภายในเพิ่มเติม

รายละเอียด จัตุรัส มีดังนี้

จะมีเส้นทะแยงมุม จาก มุมซ้ายบน มา ยัง มุมขวาล่าง จัตุรัส โดย เส้นทะแยงเป็นหลักหน่วยของค่า hint: modulus
ใต้เส้นทะแยงเป็นสัญญาลักษณ์ เครื่องหมาย ลบ '-' hint:ไม่ได้บังคับวิธีคิดทำอย่างไรก็ได้แค่ pattern สุดท้ายที่รวมเหมือนกัน
เหนือเส้นทะแยง แสดง เครื่องหมาย บวก '+'
ตัวอย่าง
input: n=12
12

-----------------------------------------------------------

output:
2 + + + + + + + + + + + 

- 2 + + + + + + + + + + 

- - 2 + + + + + + + + + 

- - - 2 + + + + + + + + 

- - - - 2 + + + + + + + 

- - - - - 2 + + + + + + 

- - - - - - 2 + + + + +

- - - - - - - 2 + + + +

- - - - - - - - 2 + + +

- - - - - - - - - 2 + +

- - - - - - - - - - 2 +

- - - - - - - - - - - 2

รูปเเบบ Input
เป็นค่า integer 1 statement input จาก user

รูปเเบบ Output
! ! ! ! ! ! ! แต่ละตัวอักษรมีช่องว่างระหว่างกัน เพื่อดูง่ายและสวยงาม

ข้อจำกัด
1<=n<=100

ตัวอย่างที่1
Input:
4

Output:
4 + + + 
- 4 + +
- - 4 +
- - - 4

ตัวอย่างที่2
Input:
9

Output:
9 + + + + + + + + 
- 9 + + + + + + +
- - 9 + + + + + +
- - - 9 + + + + +
- - - - 9 + + + +
- - - - - 9 + + +
- - - - - - 9 + +
- - - - - - - 9 +
- - - - - - - - 9
'''
get = int(input())

for row in range(get):
  for column in range(get):
    if row == column:
      if get>=10:
        print(str(get%10),end = " ")
      else:
        print(str(get), end = " ")
    elif column > row:
      print("+",end=" ")
    elif column < row:
      print("-", end=" ")
  print("")

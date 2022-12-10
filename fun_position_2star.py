'''
คำอธิบาย
ต้องการสร้างตารางรูป (#) โดยมีการระบุพิกัดไว้ โดยจุดที่ระบุพิกัดจะแทนที่ด้วย (*) ซึ่งพิกัดคู่อันดับ (0,0) จะอยู่ที่มุมล่างซ้ายของตาราง เมื่อไปทางขวา x จะเพิ่ม และเมื่อไปด้านบน y จะเพิ่ม

รูปเเบบ Input
บรรทัดแรกรับคู่อันดับ (x,y) ที่จะ mark ในกราฟ
บรรทัดที่สองรับค่า size (โดยที่ 1 <= size < 100)

รูปเเบบ Output
Output เป็นตารางที่จุด Mark จะอยู่ และหากคู่อันดับ (x,y) เกินขนาดของตารางก็จะมี Output ว่า That position is not loaded.

ตัวอย่างที่1
Input:
(0,0)
8

Output:
########
########
########
########
########
########
########
*#######

ตัวอย่างที่2
Input:
(2,3)
7

Output:
#######
#######
#######
##*####
#######
#######
#######

ตัวอย่างที่3
Input:
(17,16)
9

Output:
That position is not loaded.
'''
position = input()
num = int(input())
position = position.rstrip(")")
position = position.lstrip("(")
x, y = position.split(",")
x = int(x); y = int(y)

if x >= num:
  print("That position is not loaded.")
elif y >= num:
  print("That position is not loaded.")
else:
  for row in range(1, num+1):
    for column in range(1, num+1):
      if row ==  num - y   and column ==  x+1 :
        print("*", end="")
      else:
        print("#", end="")
    print("")

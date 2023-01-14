'''
คำอธิบาย
เราสร้าง หุ่นยนต์ ตัวหนึ่งให้เคลื่อนไปตาม input ที่เราป้อนให้ เริ่มต้นนั้นหุ่นยนต์จะหันหน้าไปทางแกน y ที่มีค่าบวก(เหนือ) เสมอ แต่มันจะหันหน้าไปทาง แกน y ที่มีค่าลบ(ใต้) หรือ แกน x ที่มีค่าบวก(ตะวันออก) กับ แกน x ที่มีค่าลบ(ตะวันตก) ตาม input ที่เราป้อนพร้อมกับเคลื่อนที่ไปหนึ่งหน่วย จนกว่า input นั้นจะเท่า กับ END ถึงจะหยุดการทำงาน
ปัญหาคือ เราควบคุมหุ่นยนต์ตัวนี้จากระยะไกล ทำให้เราหาตำแหน่งล่าสุดของหุ่นยนต์เพื่อไปตามเก็บค่อนข้างยาก เราอยากให้พวกเธอช่วยคิดโปรแกรมที่แสดง ตำแหน่งล่าสุดของหุ่นยนต์ หลังจากจบการทำงานให้เราที

รูปเเบบ Input
โดยก่อนเริ่มการทำงาน ที่บรรรทัดแรก จะต้องรับตำแหน่งหุ่นยนต์ ณ ปัจจุบัน เป็น (x,y) มาก่อน เช่น (0,0) หรือ (2,4) เป็นต้น
บรรทัดถัดไปคือ การสั่งการให้ หุ่นยนเคลื่อนที่ ดังนี้
FW (เดินหน้า) หันไปทิศเดิม แล้วเคลื่อนที่ไปหนึ่งหน่วย
BK (ถอยหลัง) หันไปทิศตรงข้าม แล้วเคลื่อนที่ไปหนึ่งหน่วย
L ( เลี้ยวซ้าย) หันไปทางซ้าย แล้วเคลื่อนที่ไปหนึ่งหน่วย
R ( เลี้ยวขวา) หันไปทางขวา แล้วเคลื่อนที่ไปหนึ่งหน่วย
จนกว่า input จะเท่ากับ END ถึงจะหยุดการทำงาน

รูปเเบบ Output
แสดง ตำแหน่งล่าสุดของหุ่นยนต์เป็น (x,y) เช่น (1,4) หรือ (2,3) เป็นต้น
ข้อจำกัด
x และ y ต้องเป็นจำนวนเต็มเท่านั้น

ตัวอย่างที่1
Input:
(0,2)
FW
BK
L
R
FW
L
BK
END

Output:
(1,0)

ตัวอย่างที่2
Input:
(0,0)
FW
R
L
BK
END

Output:
(1,1)

ตัวอย่างที่3
Input:
(2,3)
FW
BK
L
R
END

Output:
(3,2)
'''
initail_pt = input().rstrip(")").lstrip("(").split(",")
initail_pt = [int(i) for i in initail_pt]
in_pt =[]
get = ""
while get != "END":
  get = input()
  if get != "END":
    in_pt.append(get)

x = initail_pt[0]
y = initail_pt[1]
in_direct = "N"

for i in in_pt:
  if in_direct == "N":
    if i == "FW":
      y +=1
      in_direct = "N"
    elif i == "BK":
      y -=1
      in_direct = "S"
    elif i == "L":
      x -= 1
      in_direct = "W"
    elif i == "R":
      x += 1
      in_direct = "E"
  elif in_direct == "S":
    if i == "FW":
      y -=1
      in_direct = "S"
    elif i == "BK":
      y +=1
      in_direct = "N"
    elif i == "L":
      x += 1
      in_direct = "E"
    elif i == "R":
      x -= 1
      in_direct = "W"
  elif in_direct == "W":
    if i == "FW":
      x -=1
      in_direct = "W"
    elif i == "BK":
      x +=1
      in_direct = "E"
    elif i == "L":
      y -= 1
      in_direct = "S"
    elif i == "R":
      y += 1
      in_direct = "N"
  elif in_direct == "E":
    if i == "FW":
      x +=1
      in_direct = "E"
    elif i == "BK":
      x -=1
      in_direct = "W"
    elif i == "L":
      y += 1
      in_direct = "N"
    elif i == "R":
      y -= 1
      in_direct = "S"
      
print(f"({x},{y})")

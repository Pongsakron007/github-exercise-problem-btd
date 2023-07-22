'''
คำอธิบาย
เราจะมีลิฟท์ทั้งหมด 5 ชั้น ได้แก่ 1 2 3 4 และ 5 โดยจะอยู่ที่ชั้น 1 เสมอ
และเราจะรับข้อมูลชั้นที่อยากจะไป(อาจมีหลายชั้น)
แล้วแสดงข้อมูลทีละ step โดย รูปแบบดูได้ที่ out put
ถ้ากรอกตัวเลขชั้นไม่ตรงกับที่มีอยู่ ให้ แสดง ว่า
Error! Not have this floor

รูปเเบบ Input
รับเลขชั้น(จำนวนเต็ม Integer) แล้วจบด้วยตัว - คือจบ input แล้ว
เช่น
1
-
ถ้ามีหลายชั้นจะ input เป็น
1 ชั้น 1 บรรทัด เช่น
1
3
4
-
โดยเลขชั้นจะเรียงจากน้อยไปมากหรือมากไปน้อยก็ได้

รูปเเบบ Output
รูปแบบคือ

OK! Wait please
---------------
Lift is arriving!
---------------
Lift is going up!
---------------
Lift has reached the (ชั้นตามด้วย *ตัวตามหลังอันดับ*) floor!
---------------
Lift is going up!
---------------
Lift has reached the (ชั้นตามด้วย *ตัวตามหลังอันดับ*) floor! 
---------------

...ไปเรื่อยจนหมดทุกชั้นที่รับinputมา...
(-) 15 ตัว
ตัวตามหลังอันดับ เช่น 1st 2nd 3 rd 4th ...
ชั้นที่ output ออกมาทีละชั้นให้เรยี=งจากน้อยไปมาก โดยขั้นด้วย ประโยค "Lift is going up!"
ถ้ากรอกตัวเลขชั้นไม่ตรงกับที่มีอยู่
หรือ หากมีการตรวจเจอชั้นที่ไม่มีตามในโจทย์แม้แต่ 1 อัน

ให้แสดงว่า
Error! Not have this floor
แล้วจบ

ตัวอย่างที่1
Input:
1
-

Output:

OK! Wait please
---------------
Lift is arriving!
---------------
Lift is going up!
---------------
Lift has reached the 1st floor!

ตัวอย่างที่2
Input:
0
2
5
-

Output:
Error! Not have this floor

ตัวอย่างที่3
Input:
3
1
5
-

Output:

OK! Wait please
---------------
Lift is arriving!
---------------
Lift is going up!
---------------
Lift has reached the 1st floor!
---------------
Lift is going up!
---------------
Lift has reached the 3rd floor!
---------------
Lift is going up!
---------------
Lift has reached the 5th floor!
'''
floor_in = []

while True:
  f_in = input()
  if f_in == "-" :
    break
  floor_in.append(f_in)

def check_correct_floor(floor_in):
  int_floor  = [int(i) for i in floor_in]
  for i in int_floor:
    if i > 5 or i < 1:
      return False
  return True

def show(floor_in):
  int2_floor  = [int(i) for i in floor_in]
  int2_floor.sort()
  print("OK! Wait please")
  print("---------------")
  print("Lift is arriving!")
  print("---------------")
  print("Lift is going up!")
  print("---------------")
  for idx, f in enumerate(int2_floor) :
    if int2_floor[-1] != int2_floor[idx]:
      if f == 1:
        print(f"Lift has reached the {f}st floor!")
      elif f == 2:
        print(f"Lift has reached the {f}nd floor!")
      elif f == 3:
        print(f"Lift has reached the {f}rd floor!")
      else:
        print(f"Lift has reached the {f}th floor!")
      print("---------------")
      print("Lift is going up!")
      print("---------------")
    else:
      if f == 1:
        print(f"Lift has reached the {f}st floor!")
      elif f == 2:
        print(f"Lift has reached the {f}nd floor!")
      elif f == 3:
        print(f"Lift has reached the {f}rd floor!")
      else:
        print(f"Lift has reached the {f}th floor!")

show(floor_in) if check_correct_floor(floor_in) else print("Error! Not have this floor")

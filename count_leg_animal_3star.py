'''
คำอธิบาย
ณ ฟาร์มแห่งหนึ่ง มีเจ้าของฟาร์มที่ไม่ค่อยจะปกติสักเท่าใหร่ เค้าไม่อยากรู้จำนวนสัตว์เลี้ยงในฟาร์มของเขา แต่เขากลับอยากรู้จำนวนขาของสัตว์ในฟาร์มมากกว่า
ให้ทุกคนเขียนโปรแกรมหาจำนวนขาของสัตว์ในฟาร์ม
โดยที่ในฟาร์มมีสัตว์ดังนี้ สุนัข แมว ไก่ เป็ด วัว งู นก



ข้อมูลเพิ่มเติม เผื่อใครไม่รู้
สุนัขมี 4 ขา
แมวมี 4 ขา
ไก่มี 2 ขา
เป็ดมี 2 ขา
วัวมี 4 ขา
งู ไม่มีขา
นกมี 2 ขา

รูปเเบบ Input
ให้ชื่อและจำนวนสัตว์แต่ละชนิด จำนวน 3 ชนิด
เช่น
Cow 3
Dog 2
Bird 4

รูปเเบบ Output
Output เป็นจำนวนขาทั้งหมด

เช่น
28

ข้อจำกัด
แต่ละข้อจะมีสัตว์ 3 ชนิดเท่านั้น
จำนวนสัตว์เป็นจำนวนนับ

ตัวอย่างที่1
Input:
Dog 2
Chicken 7
Cow 3

Output:
34

ตัวอย่างที่2
Input:
Cat 2
Duck 7
Snake 15

Output:
22

ตัวอย่างที่3
Input:
Snake 7
Bird 1
Dog 1

Output:
6
'''
animal = [input() for i in range(3)]

list_an = []
for i in animal:
  an_l = i.split()
  list_an.append(an_l)
  
leg_re = 0
for i in list_an:
  if i[0] == "Dog":
    leg_re += int(i[1])*4
  elif i[0] == "Cat":
    leg_re += int(i[1])*4
  elif i[0] == "Chicken":
    leg_re += int(i[1])*2
  elif i[0] == "Duck":
    leg_re += int(i[1])*2
  elif i[0] == "Cow":
    leg_re += int(i[1])*4
  elif i[0] == "Snake":
    leg_re += int(i[1])*0
  elif i[0] == "Bird":
    leg_re += int(i[1])*2
    
print(leg_re)

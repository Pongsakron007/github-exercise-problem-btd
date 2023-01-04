'''
คำอธิบาย
ข้อนี้จะเป็นการบอกรายละเอียดสินค้าและนำมาคำนวณหารคา รัชหัสก็จะมีมากมาย เช่น สี size และ อีกมากมาย โดยข้อนี้จะเป็น เสื้อผ้านะครับ
เราจะนำราคาทุกเงื่อนไขมาบวกกันจนได้ราคาสุทธิ
โดยจะมีเงื่อนไขทั้งหมดต่อไปนี้

บรรทัดที่ 1 - ประเภท

หมายเลข 1 คือ underwear(ชุดชั้นใน เช่น กางเกงใน และอื่นๆ) - ราคา 20  
หมายเลข 2 คือ pants(กางเกง) - ราคา 30
หมายเลข 3 คือ skirt - ราคา 30
หมายเลข 4 คือ shirt - 40
หมายเลข 5 คือ blouse - 40

ด้านหลังคือราคานะครับ
ทีไม่ได้วงเล็บหาคำแปลกันเอาเองนะจ๊ะ

บรรทัดที่ 2 - size
หมายเลข 1 คือ S - 5
หมายเลข 2 คือ M - 10
หมายเลข 3 คือ L - 15
หมายเลข 4 คือ Xl -20 
หมายเลข 5 คือ XXL - 25

ด้านหลังคือราคานะครับ

บรรทัดที่ 3 - สี
หมายเลข R คือ red - 15
หมายเลข B คือ blue - 15
หมายเลข W คือ white - 10
หมายเลข G คือ green - 15 
หมายเลข BK คือ black - 15

ด้านหลังคือราคานะครับ

บรรทัดที่ 4 - เนื้อผ้า
หมายเลข 1 คือ cotton - 20
หมายเลข 2 คือ nylon - 15
หมายเลข 3 คือ spandex - 25
หมายเลข 4 คือ wool - 30 
หมายเลข 5 คือ linen - 25

ด้านหลังคือราคานะครับ

บรรทัดที่ 5 - จำนวน
เป็นจำนวนเต็ม เช่น 1 2 3
ก็ให้นำราคาแต่ละเงื่อนไขมาบวกกัน แล้วมาคูณจำนวนนะครับ

รูปเเบบ Input
ตามด้านบนนะครับ มีการเว้นบรรทัด เช่น
1
1
R
1
1
หมายความว่า
underwear 
size S
color red
cotton
amount 1

รูปเเบบ Output
แสดงรายละเอียดนะครับ
แล้วบรรทัดสุดท้ายแสดงผมรวมราคา

รูปแบบคือ
(ชนิดเสื้อ) - (ราคา)
size (sixe) - (ราคา)
color (สี) - (ราคา) 
(ชนิดผ้า) - (ราคา)
amount - (จำนวนตัว)
cost - (ราคาตัวละ)*(จำนวน) = (ราคาสุทธิ)
*size ตัวใหญ่นะครับ เช่น S L XXL

*รหัสสีตัวใหญ่นะครับ เช่น R
*ราคาตัวละ คือเอามาบวกกันทั้งหมด

เช่น

underwear - 20
size S - 5
color red - 15 
cotton - 20
amount - 1
cost - 60*1 = 60

ตัวอย่างที่1
Input:
1
1
R
1
1

Output:
underwear - 20
size S - 5
color red - 15 
cotton - 20
amount - 1
cost - 60*1 = 60

ตัวอย่างที่2
Input:
2
1
BK
3
2

Output:
pants - 30
size S - 5
color black - 15 
spandex - 25
amount - 2
cost - 75*2 = 150
'''
type_dict = {1:["underwear", 20], 2:["pants", 30], 3:["skirt", 30], 4:["shirt", 40], 5:["blouse", 40]}
size_dict = {1:["S", 5], 2:["M", 10], 3:["L", 15], 4:["Xl", 20], 5:["XXL", 25]}
color_dict = {"R":["red", 15], "B":["blue", 15], "W":["white", 10], "G":["green", 15], "BK":["black", 15]}
texture_dict = {1:["cotton", 20], 2:["nylon", 15], 3:["spandex", 25], 4:["wool", 30], 5:["linen", 25]}

type_s, size, color, texture, num = [input() for i in range(5)]
type_s, size, color, texture, num = int(type_s), int(size), color, int(texture), int(num)

total = type_dict[type_s][1] + size_dict[size][1] + color_dict[color][1] + texture_dict[texture][1]

print(f"{type_dict[type_s][0]} - {type_dict[type_s][1]}")
print(f"size {size_dict[size][0]} - {size_dict[size][1]}")
print(f"color {color_dict[color][0]} - {color_dict[color][1]}")
print(f"{texture_dict[texture][0]} - {texture_dict[texture][1]}")
print(f"amount - {num}")
print(f"cost - {total}*{num} = {total*num}")

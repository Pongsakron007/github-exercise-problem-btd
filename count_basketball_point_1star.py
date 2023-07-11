'''
คำอธิบาย
ในการแข่งขันบาสเกตบอล จะมีผู้เล่นอยู่ 5 ตำแหน่ง ได้แก่

C - Center
PG - Point Guard
SG - Shooting Guard
SF - Small Forward
PF - Power Forward

ในการทำแต้มจะมี 2 แบบ คือ ทำแต้มวงใน และวงนอก โดยวงในได้ 2 แต้ม วงนอกได้ 3 แต้ม ซึ่งในที่นี้ Shooting Guard จะเป็นตำแหน่งเดียวที่ทำแต้มวงนอก ส่วนตำแหน่งที่เหลือทำแต้มวงใน นอกจานั้นถ้าหากว่าฝั่งตรงข้ามทำฟาวล์ เราจะได้ 1 แต้ม

รูปเเบบ Input
Line 1 - จำนวนลูกที่ทำแต้มได้ N
Line 2 - ชื่อทีม
Line 3 to N+2 - ตำแหน่งที่ทำแต้ม (F คือ ฟาวล์)

รูปเเบบ Output
Line 1 - ชื่อทีม เช่น "Team : Name"
Line 2 - จำนวนแต้ม เช่น "Get ...... points"

ข้อจำกัด
1 <= N <= 50
ในทุกทีมจะมีครบ 5 ตำแหน่ง

ตัวอย่างที่1
Input:
5
ABC
SG
SG
PG
PF
SF

Output:
Team : ABC
Get 28 points

ตัวอย่างที่2
Input:
10
BASket
PG
PF
SF
F
C
SG
PG
C
C
SG

Output:
Team : BASket
Get 21 points

ตัวอย่างที่3
Input:
2
Civilization
PG
PG
Output:

Team : Civilization
Get 2 points
'''
num = int(input())
name_team = input()

pointer = [input() for i in range(num)]


def Do_point(pointer):
  point = 0
  for i in pointer:
    if i == "SG": point += 3
    elif i == "F": point +=1
    else: point += 2
  return point

def result():
  print(f"Team : {name_team}")
  print(f"Get {Do_point(pointer)} points")


result()

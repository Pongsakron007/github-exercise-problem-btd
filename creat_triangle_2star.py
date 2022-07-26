'''
คำอธิบาย
สร้างสามเหลี่ยม โดยที่เส้นรอบรูปของสามเหลี่ยม
ประกอบด้วย 3 เครื่องหมาย
1. (" / ")
2. (" \ ")
3. (" _ ")

รูปเเบบ Input
รับจำนวนเต็ม n แทนความสูงของสามเหลี่ยม โดยที่ n > 1

รูปเเบบ Output
แสดงผลรูปสามเหลี่ยมที่สร้างได้

2 ชั้น
5 ชั้น
9 ชั้น

ข้อจำกัด
output ให้ดูตามรูปภาพด้านบน

ตัวอย่างที่1
Input:
2

Output:
 /\\
/__\\

ตัวอย่างที่2
Input:
5

Output:
    /\\
   /  \\
  /    \\
 /      \\
/________\\

ตัวอย่างที่3
Input:
9

Output:
        /\\
       /  \\
      /    \\
     /      \\
    /        \\
   /          \\
  /            \\
 /              \\
/________________\\

'''

num = int(input())

def triangle(num):
  for i in range(1, (num*2)+1):
    if i < num:
      print(" "*(num-i) + "/" + " "*(i-1) + " "*(i-1) + "\\")
    elif i == num:
      print(" "*(num-i) + "/" + "_"*(i-1)*2  + "\\")

triangle(num)

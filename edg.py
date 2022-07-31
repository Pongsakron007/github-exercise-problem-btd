#ขอบตาราง
'''
คำอธิบาย

ให้สร้างกล่องสี่เหลี่ยมที่มีความสูงเป็น n
โดยที่ความสูงของกล่องต้องมากกว่า 2 ถ้าน้อยกว่าให้แสดงว่า "Box's height must be more than 2"

รูปเเบบ Input
รับค่า n เป็นจำนวนเต็ม

รูปเเบบ Output
รูปกล่องที่จะสร้าง

ข้อจำกัด
n > 2

Input:
6

Output:

******
*    *
*    *
*    *
*    *
******
'''

number = int(input())
if number <=2:
  print("Box's height must be more than 2")
else:
    for row in range(number):
        for column in range(number):
            if row  == 0 or row == number-1 or column == 0 or column == number-1:
                print("*",end="")
            else:
                print(" ",end="")
        print("")

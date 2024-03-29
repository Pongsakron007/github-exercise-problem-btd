'''
คำอธิบาย
เอาละตอนนี้เรามาติดใน the back room ที่เลเวล แปลก ๆๆ ที่ไม่มีทั้งน้ำและอาหาร แต่ในมือคุณนั้น มีอุปกรณ์คล้ายกับ โน๊ตบุ๊คลักษณะแปลกๆๆ ติดมา พร้อมกับมี ไฟล์ที่ มีชื่อว่า exit.txt คุณเปิดอ่านก็พบว่า ในนั้นบอกว่า ถ้าคุณอยากออกไปจากที่นี้คุณต้องเขียนโปรแกรม ภาษาอะไรก็ได้ที่คุณรู้จัก โดยจะมีการรับค่าเป็นจำนวนเต็ม และ โปรแกรมจะแสตงเป็น ลูกศร ตัวอย่างดังนี้

      *
     ***
    *****
  * ===== *
 ** ===== **
*** ===== ***
    =====
    =====
    =====
level 3

โดยเลขที่คุณ input เข้ามาตอน run โปรแกรมนั้นจะเป็น level ที่คุณอยากที่จะไป เอาละข้อให้โชคดีกับการ noclip ครั้งนี้ละลูกแกะหลงทางตัวจอย และ คุณไม่ต้องห่วงเรื่อง ไลเบอรี่ข้องโปรแกรม ต่างๆนะเพราะ notebook ตัวนี้นะ มันมีไลเบอรี่ และติดตั้งไวทุกอย่างที่คุณต้องการแล้ว เอาละ รีบ สร้างไฟล์โปรแกรม ซะ เพราะไม่รู้ถ้า คุณอยู่นานเกินไป พวก entity พวกนั้นจะเจอคุณแน่นอน
รูปเเบบ Input
รับค่าเป็นจำนวนเต็มบวก

รูปเเบบ Output
เป็นลูกศรลักษณะแบบนี้

      *
     ***
    *****
  * ===== *
 ** ===== **
*** ===== ***
    =====
    =====
    =====
level 3

ข้อจำกัด
ระวังอย่าให้ error บ่อยละเพราะ อุปกรณ์ใน notebook ของคุณที่ทำหน้าที่ไล่ entity พวกนั้น จะเสื่อมเร็วมากขึ้น ซึ่งไม่สนุกแน่นอน และ อ่อ ห้องที่คุณเลือกไปนั้นไปได้แค่จำนวนเต็ม บวกเท่านั้น หรือ n เป็นจำนวนเติม n>=0

ตัวอย่างที่1
Input:
3

Output:
      *
     ***
    *****
  * ===== *
 ** ===== **
*** ===== ***
    =====
    =====
    =====
level 3

ตัวอย่างที่2
Input:
4

Output:

        *
       ***
      *****
     *******
   * ======= *
  ** ======= **
 *** ======= ***
**** ======= ****
     =======
     =======
     =======
     =======
level 4

ตัวอย่างที่3
Input:
0

Output:
level 0
'''
num = int(input())

def arrow(num):
  for i in range(num):
    print(" "* (num ) + " "* (num-i) + "*" *(i+1) + "*" *(i))

  for i in range(num):
    print(" "* (num -1-i) + "*"*(i+1) + " " + "=" *(num+num-1) + " " +"*"* (i+1))

  for i in range(num):
    print(" "*(num+1) + "="*(num*2 -1))

  print(f"level {num}")


arrow(num)

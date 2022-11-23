'''
คำอธิบาย
สร้างต้นไม่ครึ่งต้นด้วยสัญลักษณ์ *

รูปเเบบ Input
สร้างต้นไม้ครึ่งต้น(ความสูงของลำต้นตาม input)

รูปเเบบ Output
*
**
***
****
*****
******
*******
********
*********
**********
***
***
***
***
***

ตัวอย่างที่1
Input:
1

Output:
*
**
***
****
*****
******
*******
********
*********
**********
***
ตัวอย่างที่2
Input:
2

Output:
*
**
***
****
*****
******
*******
********
*********
**********
***
***

ตัวอย่างที่3
Input:
3

Output:
*
**
***
****
*****
******
*******
********
*********
**********
***
***
***
'''
def tree():
  T = int(input())
  for i in range(1, 11):
    print("*"*i)
  for i in range(T):
    print("*"*3)
    
tree()

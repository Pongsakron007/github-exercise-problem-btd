'''
คำอธิบาย
ให้ทำการสร้างต้นคริสมาสต์จากความสูงที่รับเข้ามาโดยมีตัวอย่างดังภาพ

รูปเเบบ Input
บรรทัดแรก จำนวนเต็ม n เป็นความสูงของต้นคริสมาสต์

รูปเเบบ Output
แสดงต้นคริสมาสต์ตามความสูงที่รับเข้ามา

ข้อจำกัด
0<n<100

Input: 2

Output:
  *
 ***
  *
 ***
*****
  |
==V==

'''
p = int(input())
def py():
  for row in range(2,p+2):
    for column in range(1,row+1):
      print(" "*(p-column+1)+"*"+("*"*(2*column-2)))
  print(" "*p + "|")
  print("="*p + "V" + "="*p)
py()

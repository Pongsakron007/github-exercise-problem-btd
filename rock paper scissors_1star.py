'''
คำอธิบาย
บอสต้องการเป่ายิ้งฉุบกับคลีนเพื่อนรัก ซึ่งเขามีความสามารถในการอ่านใจ เขาสามารถรู้ได้ว่าคลีนต้องการจะออกอะไร แต่เขาไม่รู้ว่าเขาต้องออกอะไร บอสต้องการให้ทุกคนช่วย มาช่วยเขียนโปรแกรมกันเถอะว่าบอสต้องออกอะไร

รูปเเบบ Input
สิ่งที่คลีนจะออก

รูปเเบบ Output
สิ่งที่บอสต้อง

ตัวอย่างที่1
Input:
ROCK

Output:
PAPER
'''
get = input()

if get =="ROCK":
  print("PAPER")
elif get =="SCISSORS":
  print("ROCK")
elif get=="PAPER":
  print("SCISSORS")
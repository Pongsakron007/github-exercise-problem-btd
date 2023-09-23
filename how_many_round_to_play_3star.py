'''
คำอธิบาย
สยุ๋มตุ๋ย ชอบเล่นเกมมาก และมักจะมีปัญหาเรื่อง จัดการเวลา เล่นเกมทุกวันทำให้บางครั้งต้องเลิกเล่นทั้งที่ยังไม่จบรอบ สยุ๋มตุ๋ยเลยเข้าไปในด่ากแว๊บเพื่อจ้างวาน นักวางแผนตัวฉกาจ(คุณ) มาแก้ปัญหาให้กับเขา

#Requirement
สยุ๋มตุ๋ย ชอบเล่นเกม Public Static G ที่จะมีรอบการเล่นอย่างแน่นอน รอบละ 15 นาที
โดยตัวเขาเองจะมีเวลาเริ่มเล่นและเวลาเลิกเล่นไม่เหมือนกันทุกครั้งและทุกวัน
ให้คำนวณหา จำนวนรอบ ที่ สยุ๋มตุ๋ย สามารถเล่นได้แบบ จบเกมพอดี ภายในระยะเวลาที่เขากำหนดเอง

รูปเเบบ Input
รับค่า เวลาเริ่มเล่นเกม และ เวลาเลิกเล่นเกม
รูปแบบ ชม:นาที (HH:MM)

#ตัวอย่าง
Input 1 : 00:00
Input 2 : 23.59

รูปเเบบ Output
แสดงผล จำนวนรอบ ที่สามารถเล่นได้จน จบเกมพอดี ภายในระยะเวลาที่รับค่าเข้ามา

#ตัวอย่าง
Output : Can play 95 round
#ตัวอย่างเมื่อเล่นไม่ได้สักรอบ
Output : Can not play any round :P
#ตัวอย่างเมื่อรูปแบบเวลาผิด

Output : Time format went wrong
ข้อจำกัด
รูปแบบเวลา 24 ชั่วโมง

ตัวอย่างที่1
Input:
00:00
23:59

Output:
Can play 95 round

ตัวอย่างที่2
Input:
00:00
00:14

Output:
Can not play any round :P

ตัวอย่างที่3
Input:
00:00
24:00

Output:
Time format went wrong
'''

from datetime import datetime

start, end = [input() for i in range(2)]

try:

  start_time = datetime.strptime(start, "%H:%M")
  end_time = datetime.strptime(end, "%H:%M") 
  if end_time == start_time:
    round_to_play = 0
  elif end_time > start_time:
    time_difference = (end_time - start_time).total_seconds() / 60
    round_to_play = abs(time_difference//15)
  else:
    mid1 = datetime.strptime("23:59", "%H:%M")
    mid2 = datetime.strptime("00:00", "%H:%M")
    time_difference_1 = ((mid1 - start_time).total_seconds() / 60 )+1
    time_difference_2 = (end_time - mid2).total_seconds() / 60
    total_difference = time_difference_1 + time_difference_2
    round_to_play = abs(total_difference//15)
    #print(time_difference_1, time_difference_2)


  if round_to_play == 0:
    print("Can not play any round :P")
  elif round_to_play >0:
    print(f"Can play {int(round_to_play)} round")

  
except:
  print("Time format went wrong")

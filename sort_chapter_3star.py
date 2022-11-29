'''
คำอธิบาย
อาจารย์ให้นักเรียนอ่านหนังสือนอกเวลาเล่มหนึ่ง โดยจะนำเนื้อหาในหนังสือมาออกข้อสอบกลางภาค ซึ่งเนื้อหาในหนังสือก็มีจำนวนบทค่อนข้างมากและวันสอบกลางภาคก็เข้าใกล้มาทุกทีแล้ว เพื่อนๆในชั้นเรียนจึงได้ตัดสินใจกันว่าจะแบ่งเนื้อหาในหนังสืออ่านกันคนละ 1 บท และเมื่ออ่านเสร็จก็ทำการสรุปเนื้อหาในบทที่ตนเองอ่านลงในแชทกลุ่ม
แต่เนื่องจากแต่ละคนไม่ได้สรุปเนื้อหาเสร็จพร้อมกันทำให้ข้อความเนื้อหาที่เพื่อนๆสรุปลงในแชทกลุ่มนั้นไม่ได้เรียงตามบทที่ควรจะเป็น ทำให้ยากต่อการอ่านและทำความเข้าใจคุณจึงต้องทำการเขียนโปรแกรมเพื่อเรียงบทของหนังสือขึ้นมา

รูปเเบบ Input
บรรทัดแรกรับค่าจำนวนเต็ม n เพื่อบอกจำนวนบททั้งหมดของหนังสือ
บรรทัดต่อมารับเลขบทของหนังสือและรับเนื้อหาที่ทำการที่สรุปแล้วในบรรทัดมา

อีกเป็นจำนวน n ครั้ง
รูปเเบบ Output
แสดงเนื้อหาของหนังสือที่ผ่านการเรียงลำดับตามบทมาแล้ว


ตัวอย่างที่1
Input:
3
3
The human body is made up of over 70 percent water.
1
Humans will die if they hear noises above 200 decibels.
2
You will not be able to hold your breath until death.

Output:
Chapter 1
Humans will die if they hear noises above 200 decibels.
Chapter 2
You will not be able to hold your breath until death.
Chapter 3
The human body is made up of over 70 percent water.

ตัวอย่างที่2
Input:
2
1
Plastic made from polymers.
2
Hummingbird do NOT flap their wings, they rotate them in a figure 8.

Output:
Chapter 1
Plastic made from polymers.
Chapter 2
Hummingbird do NOT flap their wings, they rotate them in a figure 8.

ตัวอย่างที่3
Input:
5
4
I love you.
1
I hate you.
2
I like you.
3
I know you.
5
I do not know.

Output:
Chapter 1
I hate you.
Chapter 2
I like you.
Chapter 3
I know you.
Chapter 4
I love you.
Chapter 5
I do not know.
'''
num = int(input())

list_s  = [input() for i in range(num*2)]

list_c = list_s[::2]
list_t = list_s[1::2]

dic_re = {}

for i, j  in zip(list_t, list_c):
  dic_re[j] = i
  
  
dic_last = dict(sorted(dic_re.items()))

for key, value in dic_last.items():
  print(f"Chapter {key}")
  print(value)

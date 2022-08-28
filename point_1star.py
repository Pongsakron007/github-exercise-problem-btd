'''
คำอธิบาย
นักเรียนชั้น ป.1 คนนหนึ่ง มีการสอบวิชาภาษาอังกฤษคะแนนเต็มมี100คะแนน
มีเกณฑ์คะแนน ดังนี้

0-25 = fail
26-50 = good
51-75 = very good
76-100 = excellent

รูปเเบบ Input
คะแนนที่สอบได้(ตัวเลขจำนวนเต็ม)

รูปเเบบ Output
แสดงข้อความตามเกณฑ์คะแนนที่กำหนด fail , good , very good, excellent

ตัวอย่างที่1
Input:
20

Output:
fail
'''

point = int(input())

if point >=76 and point <=100:
  print("excellent")
elif point >=51 and point <=75:
  print("very good")
elif point >=26 and point <=50:
  print("good")
elif point >=0 and point <=25:
  print("fail")

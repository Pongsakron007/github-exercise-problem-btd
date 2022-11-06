'''
คำอธิบาย
ณ ตอนนี้เวลาก็ได้ผ่านมาพักหนึ่งแล้วเด็กหญิงชนิกาก็ได้เติบโตขึ้นมาจากแต่ก่อนและมีความขยับมากกว่าเดิมแต่เธอนั้นกลัวที่จะลืมในสิ่งที่ตนเองต้องทำ จึงของให้พี่ชายของเธอนั้นช่วยเตือนเธอถึงส่งที่เธอต้องทำ แต่ตามเคยพี่ชายของเธอนั้นเป็นคนที่ขี้เกียจจึงมาขอร้องให้คุณโปรแกรมสุดเก่งคนดีคนเดิมมาช่วยในการทำโปรแกรมแจ้งเตือนในสิ่งที่ต้องทำและยังคงเหลืออะไรที่ต้องทำบ้าง

ตารางสิ่งที่ต้องทำประจำวันของเด็กหญิงชนิกา
เรียนคณิตศาสตร์online
เรียนอังกฤษonline
เรียนไทยonline
เรียนวิทย์online
อ่านเตรียมสอบ o-net
ทำงานบ้าน
เรียนวาดรูป
เรียนร้องเพลง

รูปเเบบ Input
ใส่สิ่งที่เธอทำไปแล้ว

รูปเเบบ Output
บอกว่าเหลืออีกกี่อย่างที่เธอต้องทำและทำอะไรบ้าง?

ตัวอย่างที่1
Input:
เรียนคณิตศาสตร์online,เรียนอังกฤษonline,เรียนไทยonline,เรียนวิทย์online,อ่านเตรียมสอบ o-net,ทำงานบ้าน,เรียนวาดรูป,เรียนร้องเพลง

Output:
ยังเหลือสิ่งที่ต้องทำอีก 0 อย่าง

ตัวอย่างที่2
Input:
เรียนคณิตศาสตร์online,เรียนไทยonline,เรียนวิทย์online,อ่านเตรียมสอบ o-net,ทำงานบ้าน,เรียนวาดรูป,เรียนร้องเพลง

Output:
ยังเหลือสิ่งที่ต้องทำอีก 1 อย่าง
- เรียนอังกฤษonline

ตัวอย่างที่3
Input:
เรียนคณิตศาสตร์online,เรียนอังกฤษonline,เรียนไทยonline,เรียนวิทย์online,เรียนร้องเพลง

Output:
ยังเหลือสิ่งที่ต้องทำอีก 3 อย่าง
- อ่านเตรียมสอบ o-net
- ทำงานบ้าน
- เรียนวาดรูป
'''
total = ["เรียนคณิตศาสตร์online", "เรียนอังกฤษonline", "เรียนไทยonline", 
         "เรียนวิทย์online", "อ่านเตรียมสอบ o-net", "ทำงานบ้าน", "เรียนวาดรูป", "เรียนร้องเพลง"]

get = input()
get = get.split(",")

rest = [i for i in total if i not in get]


def result():
  print(f"ยังเหลือสิ่งที่ต้องทำอีก {len(rest)} อย่าง")
  for i in rest:
    print(f"- {i}")
    
result()

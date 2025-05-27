'''
คำอธิบาย
บทนำ
น้องจอย ได้รับการจ้างวานจากหญิงสาวปริศนาคนนึง โดยหญิงสาวคนนั้นได้ให้กระดาษแผ่นนึงแก่น้องจอย พร้อมกับบอกว่า "ช่วยถอดรหัสปริศนานี้" ให้หน่อย โดยที่ถ้าแก้ได้ น้องจอยจะได้รับรางวัลตอบแทนอย่างงาม!!
แต่น้องจอยนั่งคิดมาหลายวันแล้วก็คิดไม่ออก เลยมาหาทางให้เพื่อนๆช่วยน้องจอยที


โจทย์
จงเขียนโปรแกรมถอดปริศนานี้

รูปเเบบ Input
บรรทัดที่ 1 รับ string
บรรทัดที่ 2 รับ array ของตัวเลขจำนวนเต็มบวก

รูปแบบ Output
แสดงผลลัพธ์ในรูปแบบของ string

ตัวอย่างที่ 1
ข้อมูลขาเข้า
myoxjmvle
[8, 3, 7, 9]

ผลลัพธ์
love

ตัวอย่างที่ 2
ข้อมูลขาเข้า
goyzajbcn
[5, 7, 8]

ผลลัพธ์
abc

ตัวอย่างที่ 3
ข้อมูลขาเข้า
qyomgljpn
[9, 3, 9, 5, 7, 3, 2]

ผลลัพธ์
nongjoy
'''

input_text = [input() for i in range(2)]

text_1, text_2 = input_text[0], input_text[1]

text_2 = text_2.rstrip("]").lstrip("[").split(",")

def clean_data(text):
  new_text = []
  for ele in text:
    new_ele = int(ele.strip(" "))
    new_text.append(new_ele)
  return new_text

text_2 = clean_data(text_2)

def decode_text(text_1, list_order):
  result = ""
  for ele in list_order:
    ele_result = text_1[ele-1]
    result += ele_result
  return result
  
print(decode_text(text_1, text_2))
    

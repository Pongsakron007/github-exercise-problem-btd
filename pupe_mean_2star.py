'''
คำอธิบาย
แสดงให้เห็นถึงที่มา ความสำคัญ ลักษณะของโปรแกรม หรือ บรรยายโจทย์ว่า ต้องการให้ สมาชิกทำสิ่งใด จนถึงการแต่งนิยายที่สอดคล้องกับโจทย์ เพื่อสร้างความสนุกก็ยังได้
ทางประเทศ BNK48 ได้รับ ข้อความมาหลายชุด ซึ่งทางรัฐบาลมองเห็นว่าเป็นการเรียกชื่อ member เท่านั้น แต่เมื่อกระทรวง ICT เป็นข้อความนี้ถึงกับตกใจ เพราะข้อความดังกล่าวมิได้เพียงแค่เป็นการ Hype ชื่อmember แต่เป็นข้อความที่ถูกเข้ารหัสมมาแล้ว ซึ่งทางกระทวงตั้งชื่อการเข้ารหัสนี้ว่า "pupe code" จึงอยากให้ทางโปรแกรมเมอร์ขั้นสูงสุดแห่งดาวอังคารช่วยถอดรหัสข้อความนี้ เพื่อนำข้อความนี้ไปแจ้งเตือนกับทางรัฐบาล

ซึ่งรูปแบบการเข้ารหัสเป็นดังนี้
text -> binary(ASCII) -> pupe code



ตัวอย่างการเข้ารหัส
A = pupepupupupupupe //(A = 01000001 = pupepupupupupupe)
Ab = pupepupupupupupepupepepupupupepu //(Ab =0100000101100010 = pupepupupupupupepupepepupupupepu)
สำหรับชื่อของปูเป้ หากจะเขียนเป็นภาษาฝรั่งเศสให้แปลว่า "ตุ๊กตา" แล้ว จะเขียนว่า 「Poupée」 แต่เจ้าตัวเขียนว่า 「Pupé」 อันนี้ก็ไม่ว่ากัน เพราะเป็นชื่อเฉพาะ และน่าจะสะดวกใช้กว่าสำหรับบ้านเราที่คุ้นเคยภาษาอังกฤษมากกว่า ข้อสำคัญที่เจ้าตัวแนะนำก็คือ ตัว e ในชื่อ "ปูเป้" จริงๆ แล้ว "ต้องมี acute accent ด้วย" เพื่อให้เป็นพยางค์ที่ออกเสียงเป็นสระเอ (–เป้) นั่นเอง Cr. Bulletin48 (แต่นั่นก็ไม่ได้เกี่ยวอะไรกับโจทย์)

ในภาพอาจจะมี 1 คน, กำลังยิ้ม

รูปเเบบ Input
ข้อความที่ผ่านการเข้ารหัส

รูปเเบบ Output
ข้อความที่ถอดรหัส

ตัวอย่างที่1
Input:
pupepupupupupupe

Output:
A

ตัวอย่างที่2
Input:
pupepupupupupupepupupepupupupupupupepepupupupepupupupepupupupupupupepupupupupepe

Output:
A b C

ตัวอย่างที่3
Input:

pupepepupupupepupupepepupepepepepupepepepupupepupupepepupepepepupupepepepupepupupupepepupepepepepupepupupupepupupupepepupupepupepupepepepupepepu

Output:
borntoDev
'''
text = input()
text_split = [i+j for i,j in zip(text[::2], text[1::2])]


text_int =""
for i in text_split:
  if i == "pu":
    text_int += "0"
  elif i == "pe":
    text_int += "1"
    
num = int(len(text_int)/8)

split_text_int = []
for i in range(num):
  ele = text_int[8*i:(8*i)+8]
  split_text_int.append(ele)
  
result = []
for i in split_text_int:
  re_int = int(i, 2)
  re_str = chr(re_int)
  result.append(re_str)

print("".join(result))

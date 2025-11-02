'''
คำอธิบาย
ลบสระ a e i o และ u ออกจากชื่อที่รับเข้ามา

รูปเเบบ Input
รับชื่อ Ex. Tungpanithan

รูปแบบ Output
แสดงชื่อแบบที่ไม่มีสระ a e i o u

ตัวอย่างที่ 1
ข้อมูลขาเข้า
Tungpanithan

ผลลัพธ์
Tngpnthn

ตัวอย่างที่ 2
ข้อมูลขาเข้า
Peerawit

ผลลัพธ์
Prwt

ตัวอย่างที่ 3
ข้อมูลขาเข้า
Somsak

ผลลัพธ์
Smsk
'''

text = input()

def remove_vowels(text):
  vowels = ("a", "e", "i", "o", "u")
  new_text = ""
  for letter in text:
    if letter.lower() not in vowels:
      new_text += letter
  return new_text

print(remove_vowels(text))

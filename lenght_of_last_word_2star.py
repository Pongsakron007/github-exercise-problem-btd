'''
คำอธิบาย
โปรเเกรมนี้จะอ่านบรรทัดข้อความจากผู้ใช้เเละคำนวณความยาวของคำสุดท้ายใน string input

รูปเเบบ Input
เป็น string

รูปแบบ Output
output ต้องเป็นตัวเลข

ข้อจำกัด
เป็นตัวเลขจำนวนเต็มบวกเท่านั้น

ตัวอย่างที่ 1
ข้อมูลขาเข้า

Hello world

ผลลัพธ์
5

ตัวอย่างที่ 2
ข้อมูลขาเข้า
My name is Copter

ผลลัพธ์
6

ตัวอย่างที่ 3
ข้อมูลขาเข้า
 Why are you gay  

ผลลัพธ์
3
'''
text = input()
text = text.strip(" ")
last_word = text.split(" ")[-1]
#print(last_word)
num_letter = len(last_word)

print(num_letter)

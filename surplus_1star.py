'''
คำอธิบาย
ต้องการให้แสดงตัวอักษร ที่เกินมาจาก จำนวน n
โดย n คือจำนวนตัวอักษรของข้อความที่สั้นที่สุด ซึ่งรวมถึงช่องว่างภายในข้อความด้วย
ให้รับค่ามาเป็นข้อความสองชุด เช่น
1 = Lovewednesday
2 = army
ข้อความที่ออกมาคือ wednesday
และ ตามด้วยจำนวนตัวอักษรที่เกินมา
แต่หากข้อความทั้งสองชุดที่จำนวนตัวอักษรเท่ากันให้แสดง
no surplus
โดยจำนวนตัวอักษรของข้อความทั้งสองชุดห้ามเกิน
20 ตัวอักษร !! ....

รูปเเบบ Input
บรรทัดที่ 1 รับข้อความที่ 1 เข้ามา
บรรทัดที่ 2 รับข้อความที่ 2 เข้ามา

รูปเเบบ Output
แสดงเป็นข้อความหรือตัวอักษรที่เกินมา และตามด้วย จำนวนของตัวอักษรที่เกินมา
(แนะนำให้ดูในตัวอย่าง)

ตัวอย่างที่1
Input:
business
come
	
Output:
ness = 4

ตัวอย่างที่2
Input:
h@d oko%& *@gfd
abcd po

Output:
%& *@gfd = 8

ตัวอย่างที่3
Input:
3899932abcgtr*&
WednesdaySocute

Output:
no surplus
'''
a, b = [input() for i in range(2)]
if len(a) == len(b):
  print("no surplus")
elif len(a) > len(b):
  num_str = len(a) - len(b)
  new_str = a[len(b):]
elif len(b) > len(a):
  num_str = len(b) - len(a)
  new_str = b[len(a):]

print(f"{new_str} = {len(new_str)}")

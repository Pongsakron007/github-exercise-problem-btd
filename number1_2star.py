'''
คำอธิบาย
รับค่าเป็นตัวอักษร จากนั้นทำการแปลงเป็น ตัวเลข
เช่น a = 97 ,b= 98
แล้วนำตัวเลขที่แปลงจากแต่ละตัวมาทำการยกกำลังด้วย จำนวนอักษรทั้งหมด เช่น abc
แปลง a=97,b=98,c=99 แล้วมายกกำลังด้วยจำนวนตัวอักษรทั้งหมด คือ 3 (abc = 3 จำนวน)

97**3 =912673
98**3=941192
99**3=970299

นำตัวเลขทั้งหมดมาบวกรวมกัน ได้ 2824164
จากนั้นนำเลขทุกตัวมาบวกกันเรื่อยๆ จนเหลือ แค่ตัวเดียว

ยกตัวอย่าง 
2+8+2+4+1+6+4= 27 => 2+7 =9

รูปเเบบ Input
รับค่าเป็นตัวหนังสือบรรทัดเดียว

รูปเเบบ Output
เป็นตัวเลข 1 ตัว

ตัวอย่างที่1
Input:
abc

Output:
9
2

ตัวอย่างที่2
Input:
HelloWorld

Output:
8
3

ตัวอย่างที่3
Input:
chiangmai

Output:
2
'''

get = input()

list_get =[i for i in get]
num = len(str(get))

total = 0 

for i in list_get:
  total += ord(i)**num
  
total_str = str(total)
num_total = len(total_str)

while num_total >1:
  total_str = str(total_str)
  list_int_total = [int(i) for i in total_str]
  total_str = sum(list_int_total)
  num_total = len(str(total_str))
  
print(total_str)

'''
คำอธิบาย
รับข้อมูลและให้แสดงผล BackSlash หน้าหลังข้อความ

รูปเเบบ Input
Shadow Emperor

รูปแบบ Output
\Shadow Emperor\
\Shadow Emperor\
\Shadow Emperor\

ข้อจำกัด
รับข้อมูลครั้งเดียว แสดงผล 3 บรรทัด

ตัวอย่างที่ 1
ข้อมูลขาเข้า

Shadow Emperor

ผลลัพธ์
\Shadow Emperor\
\Shadow Emperor\
\Shadow Emperor\

ตัวอย่างที่ 2
ข้อมูลขาเข้า
Sung jin woo

ผลลัพธ์
\Sung jin woo\
\Sung jin woo\
\Sung jin woo\

'''

myInput = input()

def show(text):
  for i in range(3):
    print(f"\\{text}\\")

show(myInput)

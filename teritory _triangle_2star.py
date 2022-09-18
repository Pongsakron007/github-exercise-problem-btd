'''
คำอธิบาย
จงคำนวนพื้นที่ 3 เหลี่ยม
สุตร: 1/2 * ฐาน * สุง

รูปเเบบ Input
บรรทัดที่ 1 ความยาวฐาน

บรรทัดที่ 2 ความสูง
รูปเเบบ Output
บรรทัดที่ 1 พื้นที่ 3 เหลี่ยม

ข้อจำกัด
อย่าโกง -_-

ตัวอย่างที่1
Input:
7
3

Output:
10.5 cm2
2

ตัวอย่างที่2
Input:
13
56

Output:
364 cm2
3
'''

base = int(input())
height = int(input())

result = 1/2 * height *base 

if result%1==0:
  print(f"{int(result)} cm2")
else:        
  print(f"{result} cm2")

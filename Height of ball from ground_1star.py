'''
คำอธิบาย
เท่ห์ขว้างบอลขึ้นฟ้าไปยังหน้าบ้านของเขา ลูกบอลอยู่ในอากาศ t วินาที ก่อนจะตกพื้น
จงหาความสูง ของจุดสูงสุดของลูกบอลมายังระดับที่เท่ห์ยืน ในแนวดิ่ง

รูปเเบบ Input
ระยะเวลา t เป็น integer

รูปเเบบ Output
ระดับความสูงระหว่างลูกบอลกับระดับของเท่ห์
ตอบเป็นทศนิยม 2 ตําแหน่ง

ข้อจำกัด
ค่า g = 9.8 m/s2

ตัวอย่างที่1
Input:
4

Output:
19.60

ตัวอย่างที่2
Input:
7

Output:
60.03

ตัวอย่างที่3
Input:
2

Output:
4.90
'''

time = int(input())

u = 9.8*(time/2)

S = (u/2)*(time/2)

print(f"{S:.2f}")
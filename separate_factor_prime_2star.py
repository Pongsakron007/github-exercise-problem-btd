'''
คำอธิบาย
ใส่ input ลงไป 1 ค่า(integer) จากนั้นแยกตัวประกอบของ input ให้แสดง output ออกมาเป็นในรูปของผลคูณของตัวประกอบ input, โดยมีเงื่อนไขว่าตัวประกอบทุกตัวต้องเป็นจำนวนเฉพาะ

รูปเเบบ Input
18

รูปเเบบ Output
2
3
3

ตัวอย่างที่1
Input:
133

Output:
7
19
2

ตัวอย่างที่2
Input:
483

Output:
3
7
23

ตัวอย่างที่3
Input:
2057

Output:
11
11
17
'''
num = int(input())
result = []

while num >1:
  for i in range(2,1000):
    if num%i ==0:
      num = num//i
      result.append(i)
      break
      
for i in result:
  print(i)

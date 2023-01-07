'''
คำอธิบาย
ตัวเลขเรียง 1-n n ครั้ง

รูปเเบบ Input
จำนวนเต็ม n

รูปเเบบ Output
ตัวเลขเรียง 1-n n ครั้ง

ข้อจำกัด
0 < n < 1000

ตัวอย่างที่1
Input:
1

Output:
1

ตัวอย่างที่2
Input:
3

Output:
122333

ตัวอย่างที่3
Input:
9

Output:
122333444455555666666777777788888888999999999
'''
num = int(input())
for i in range(1,num+1):
  for j in range(i):
    print(i, end="")

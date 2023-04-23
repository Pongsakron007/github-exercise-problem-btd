'''
คำอธิบาย
ให้ทำการสร้างสูตรคูณโดยให้รับ input เป็นเลขจำนวนเต็ม แล้วนำไปคูณกับเลขจำนวนเต็ม 1 ถึง 12 และแสดงผลคูณทั้งหมดออกมา

รูปเเบบ Input
รับ input เป็นเลขจำนวนเต็ม

รูปเเบบ Output
เช่น input เท่ากับเลข 2 ==> "2 x 1 = 2" จนถึง "2 x 12 = 24" 

ตัวอย่างที่1
Input:
2

Output:
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
2 x 10 = 20
2 x 11 = 22
2 x 12 = 24

ตัวอย่างที่2
Input:
9

Output:
9 x 1 = 9
9 x 2 = 18
9 x 3 = 27
9 x 4 = 36
9 x 5 = 45
9 x 6 = 54
9 x 7 = 63
9 x 8 = 72
9 x 9 = 81
9 x 10 = 90
9 x 11 = 99
9 x 12 = 108

ตัวอย่างที่3
Input:
7

Output:
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70
7 x 11 = 77
7 x 12 = 84
'''
num = int(input())

for i in range(1, 13):
  print(f"{num} x {i} = {num*i}")
'''
คำอธิบาย
ให้สร้าง ภูเขาตามความสูงที่ user input เข้ามา

รูปเเบบ Input
บรรทัดแรก ค่า N เป็นความสูงของภูเขา

รูปเเบบ Output
แสดงภูเขาที่มีความสูง N

ข้อจำกัด
1 < N < 10000

ตัวอย่างที่1
Input:
3

Output:
  /\
 /  \
/    \

ตัวอย่างที่2
Input:
4

Output:
   /\
  /  \
 /    \
/      \

ตัวอย่างที่3
Input:
2

Output:
 /\
/  \
'''
num = int(input())

for row in range(num):
  for column in range(num+row+2):
    if column <= num - row-2:
      print(" ", end="")
    elif column == num - row:
      print("/", end="")
    elif column > num - row and column < num + row+1:
      print(" ", end="")
    elif column == num + row+1:
      print("\\", end="")
  print("")

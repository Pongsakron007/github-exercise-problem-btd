'''
คำอธิบาย
รับค่าแม่สูตรคูณ n จากนั้นจะแสดงผลลัพธ์ของสูตรคูณจนกว่าจะคูณถึง m

รูปเเบบ Input
n เป็น float คือเลขของแม่สูตรคูณ
m เป็น int ค่าตัวคูณสูงสุดของสูตรคูณแม่นั้นๆ
**หากลืมใส่ค่าตัวคูณค่เริ่มต้นเป็น 12

รูปเเบบ Output
เช่น ใส่ค่า

input:
12.5
2

output:
12.5x1 = 12.50
12x2 = 25

**output หากเป็นจำนวนจริงให้มีทศนิยม 2 ตำแหน่ง หากเป็นจำนวนเต็มให้แสดงผลออกโดยไม่มีทศนิยม

ข้อจำกัด
หากมีการใส่ค่าที่ไม่ใช่ตัวเลขใน input ให้แสดง error input

ตัวอย่างที่1
Input:
5

Output:
5x1 = 5
5x2 = 10
5x3 = 15
5x4 = 20
5x5 = 25
5x6 = 5
5x7 = 10
5x8 = 15
5x9 = 20
5x10 = 25
5x11 = 55
5x12 = 60

ตัวอย่างที่2

Input:
null
เ้้ะัะ้ะ้ะั่ะทาีพา่ั

Output:
error input

ตัวอย่างที่3
Input:
1.25
4

Output:
1.25x1 = 1.25
1.25x2 = 2.50
1.25x3 = 3.75
1.25x4 = 5
'''
round = 12


def data():
  global num, round
  try:
    num = input()
    round = int(input())
  except:
    pass

data()

def tran_v(num):
  try:
    num = float(num)
    if num % 1 !=0:
      num = float(num)
    else:
      num = int(num)
    return num
  except:
    return False


if tran_v(num):
  last_in = tran_v(num)
  for i in range(1, round+1):
    re = last_in * i
    re = int(re) if re%1 == 0 else f"{re:.2f}"
    print(f"{last_in}x{i} = {re}")
else:
  print("error input")

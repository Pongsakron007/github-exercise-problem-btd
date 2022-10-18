'''
คำอธิบาย
ทำการสร้างบันไดตามจำนวนขั้นบันไดที่รับเข้ามา

รูปเเบบ Input
บรรทัดที่ 1 จำนวนขั้นบันไดที่ต้องการสร้าง

รูปเเบบ Output
แสดงผลบันไดตามจำนวนขั้นที่รับเข้ามา

ข้อจำกัด
จำนวนขั้นบันไดที่จะสร้างจะอยู่ระหว่าง 0 - 100

ตัวอย่างที่1
Input:
0

Output:
__

ตัวอย่างที่2
Input:
3

Output:
         __
      __|
   __|
__|

'''
get = int(input())

result = "__"
def stair(get):
  a = get*"   "+  result 
  print(a)
  for row in range(1,get+1):
    for column in range(get,-1,-1):
      if column > row:
        print(" ",end ="  ")
      if row == column:
        print("__|", end="  ")
    print("")

stair(get)
#print(a + stair(get))

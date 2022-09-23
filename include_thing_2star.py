'''
คำอธิบาย
นายเมธีที่มีทักษะการบวกเลขที่เก่งกาจต้องการรวมจำนวนของสิ่งของที่ตัวเองมีกับของที่เพื่อนมี โดยต้องการบวกพร้อมๆกันหลายๆจำนวน โดนให้ลำดับของจำนวนสิ่งของตรงกัน ถ้าจำนวนของสิ่งของที่ต้องการบวกไม่เท่ากัน หรือจำนวนของที่จะนำมาบวกเกินกว่า 32548 ชื้นให้แสดงว่า Invalid

รูปเเบบ Input
บรรทัดแรกเป็น string ของจำนวนสิ่งของที่เมธีมี
บรรทัดที่ 2 เป็น string ของจำนวนสิ่งของที่เพื่อนมี

รูปเเบบ Output
ผลรวมของจำนวนสิ่งของที่มี ถ้าจำนวนของสิ่งของมีไม่เท่ากัน หรือจำนวนมากกว่าที่กำหนดให้แสดงว่า Invalid

ข้อจำกัด
ข้อมูลบรรทัดแรกและบรรทัดที่ 2 จะมีอย่างน้อย 1 ตัวอักษร
ข้อมูลทั้ง 2 บรรทัดจะมีแค่ตัวเลขเท่านั้น
จำนวนที่จะนำมาบวกต้องไม่เกิน 32548

ตัวอย่างที่1
Input:
5 8 9
7 5 2

Output:
12 13 11

ตัวอย่างที่2
Input:
8 15 89
8 15 8 9

Output:
Invalid

ตัวอย่างที่3
Input:
59847 9598 4784
25489 1298 5987

Output:
Invalid
'''
Methe = input().split(" ")
Friend = input().split(" ")
Methe = list(map(int,Methe))
Friend = list(map(int,Friend))

result = []

def add(Methe, Friend):
  for idx, (i, j) in enumerate(zip(Methe, Friend)):
    each = i+j
    result.append(each)
    
def Check_32548():
    for idx, (i, j) in enumerate(zip(Methe, Friend)):
      each = i+j
      if i + j < 32548:
        pass
      else:
        return True
    return False
    
def Check_do():
  if Check_32548():
    print("Invalid") 
  elif len(Methe) != len(Friend):
    print("Invalid")    
  elif len(Methe) == len(Friend):
    add(Methe, Friend)
    result_str = list(map(str, result))
    print(" ".join(result_str))

if __name__ == "__main__":
  Check_do()

'''
คำอธิบาย
โดนัทนั้นเป็นสิ่งที่น่ากินและนุ่มนิ่ม จะดีไหมถ้าเราได้ขึ้นบันได้ที่ทำจากโดนัท

รูปเเบบ Input
จำนวนขั้นบันได

รูปเเบบ Output
มีบันไดโดนัทออกมาตามจำนวนขั้น

ตัวอย่างที่1
Input:
2

Output:
O
OO

ตัวอย่างที่2
Input:
6

Output:
O
OO
OOO
OOOO
OOOOO
OOOOOO
'''
get = int(input())

def donut(get):
  for row in range(1, get+1):
    for column in range(row):
      print("O",end="")
    print("")
    
if __name__ == "__main__":
  donut(get)

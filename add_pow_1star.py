'''
คำอธิบาย
อ่านคำอธิบายเลย

รูปเเบบ Input
รับ input มาสองจำนวน แล้วหาผลบวก แล้วคูณตัวมันเอง

รูปเเบบ Output
เป็นผลคูณตัวมันเอง

ตัวอย่างที่1
Input:
cat
12

Output:
Error

ตัวอย่างที่2
Input:
1
1

Output:
4
'''
def add_pow():
  try:
    x, y = [int(input()) for i in range(2)]
    z= (x+y)**2
    print(f'{z:,}')
  except:
    print("Error")
    
if __name__ == "__main__":
  add_pow()

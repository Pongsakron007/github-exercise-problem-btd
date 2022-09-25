'''
คำอธิบาย
ต้องการทราบว่าจำนวนแต่ละจำนวนที่รับค่ามานั้นเป็นเลขคู่หรือเลขคี่

รูปเเบบ Input
รับค่าตัวเลขเรื่อยๆและจะหยุดรับเมื่อใส่ค่า 0 ลงไป

รูปเเบบ Output
แสดงผลตัวเลขที่ใส่ไปทั้งหมดและบอกว่าแต่ละจำนวนเป็นเลขคู่หรือเลขคี่

ตัวอย่างที่1
Input:
1
9
8
6
10
11
0

Output:
1 = odd
9 = odd
8 = even
6 = even
10 = even
11 = odd
'''

def od():
  while True:
    get = int(input())
    if get ==0:
      break
    else:
      if get%2 == 0:
        print(f"{get} = even")
      elif get%2 == 1:
        print(f"{get} = odd")
        
if __name__ == "__main__":
  od() 

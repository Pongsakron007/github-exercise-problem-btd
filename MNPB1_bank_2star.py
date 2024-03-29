'''
คำอธิบาย
ในข้อนี้เราจะให้คุณเขียนโปรแกรมนับธนบัตรธนาคาร โดยสมมติว่าคุณกำลังเขียนโปรแกรมช่วยเครื่อง ATM ในการถอนเงิน (กำหนดให้มีแค่ธนบัตร 50 100 500 1000 บาทเท่านั้น และให้ใช้จำนวนธนบัตรน้อยที่สุด) ถ้าข้อมูลนำเข้าติดลบให้แสดงคำว่า "Error"

รูปเเบบ Input
รับค่าตัวเลขจำนวนเต็ม 1 ค่า (จำนวนเงินที่จะถอนจากตู้ ATM)

รูปเเบบ Output
กรณีที่ 1 ข้อมูลส่งออก มี 4 บรรทัด
บรรทัดที่ 1 แสดงจำนวนธนบัตร 1000 บาทว่าต้องใช้กี่ใบ
บรรทัดที่ 2 แสดงจำนวนธนบัตร 500 บาทว่าต้องใช้กี่ใบ
บรรทัดที่ 3 แสดงจำนวนธนบัตร 100 บาทว่าต้องใช้กี่ใบ
บรรทัดที่ 4 แสดงจำนวนธนบัตร 50 บาทว่าต้องใช้กี่ใบ

กรณีที่ 2 ข้อมูลส่งออกมี 1 บรรทัด
บรรทัดที่ 1 แสดงคำว่า "Error"

ข้อจำกัด
ถอนเงินให้มากที่สุดเท่าที่เป็นไปได้ (หากเหลือต่ำกว่า 50 บาท ก็คิดซะว่าเงินตรงนั้นไม่มีค่า)


ตัวอย่างที่1
Input:
-443

Output:
Error

ตัวอย่างที่2
Input:
2566

Output:
1000-2
500-1
100-0
50-1

ตัวอย่างที่3
Input:
443

Output:
100-0
500-0
100-4
50-0
'''
m = int(input())

t = 0
f = 0
h = 0
fif = 0 

def cal():
  global m, t, f, h, fif
  while m >=50:
    if m >= 1000:
      t += m//1000
      m = m%1000
    elif m >=500 and m < 1000:
      f += m//500
      m = m%500
    elif m >=100 and m < 500:
      h += m//100
      m = m % 100
    elif m >= 50 and m < 100:
      fif += m//50
      m = m % 50
    
if m <0:
  print("Error")
else:
  cal()
  print(f"1000-{t}")
  print(f"500-{f}")
  print(f"100-{h}")
  print(f"50-{fif}")

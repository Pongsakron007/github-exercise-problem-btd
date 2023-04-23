'''
คำอธิบาย
คำนวณราคาสินค้าหลังหักส่วนลด โดยพิจารณาจากจำนวนสินค้า (unit) และราคาต่อหน่วย (price) พร้อมกับสถานะสมาชิก (member)

1. ถ้าเป็นสมาชิก (x)
เงื่อนไข
ถ้ายอดรวมเงิน (Total) ไม่เกิน 500 คิดส่วนลด 10% ของยอดรวมเงิน
ถ้ายอดรวมเงิน (Total) มากกว่า 500 แต่ไม่ถึง 1000 คิดส่วนลด 15% ของยอด
รวมเงิน
ถ้ายอดรวมเงิน (Total) 1000 ขึ้นไป คิดส่วนลด 20% ของยอดรวมเงิน

2. ถ้าไม่เป็นสมาชิก (y)
เงื่อนไข
ถ้ายอดรวมเงิน (Total) ไม่เกิน 500 คิดส่วนลด 5% ของยอดรวมเงิน
ถ้ายอดรวมเงิน (Total) มากกว่า 500 แต่ไม่ถึง 1000 คิดส่วนลด 10% ของยอด
รวมเงิน
ถ้ายอดรวมเงิน (Total) 1000 ขึ้นไป คิดส่วนลด 15% ของยอดรวมเงิน

รูปเเบบ Input
จำนวนสินค้า (unit) เป็นจำนวนเต็ม (integer)
ราคาต่อหน่วย (price) เป็นทศนิยม (float)
สถานะสมาชิก (member) เป็นตัวอักษร x (เป็นสมาชิก)หรือ y (ไม่เป็นสมาชิก)

รูปเเบบ Output
ราคารวมสุทธิ (total) โดยมีทศนิยม 2 ตำแหน่ง
ส่วนลด (discount) โดยมีทศนิยม 2 ตำแหน่ง
ราคาสุทธิ (amount) โดยมีทศนิยม 2 ตำแหน่ง

ข้อจำกัด
โปรแกรมรับเฉพาะจำนวนเต็มบวกเท่านั้นสำหรับ unit
ราคาต่อหน่วย (price) ต้องเป็นทศนิยมเท่านั้น
สถานะสมาชิก (member) ต้องเป็นตัวอักษร x หรือ y เท่านั้น
โปรแกรมจะแสดงผลราคาสุทธิ ส่วนลด และราคาสุทธิโดยมีทศนิยม 2 ตำแหน่ง

ตัวอย่างที่1
Input:
1
500.00
x

Output:
Total 500.00
Discount 50.00
Amount 450.00

ตัวอย่างที่2
Input:
2
600.00
x

Output:
Total 1200.00
Discount 240.00
Amount 960.00

ตัวอย่างที่3
Input:
10
50.00
y

Output:
Total 500.00
Discount 25.00
Amount 475.00
'''
q, price, member = [input() for i in range(3)]
q, price = int(q), float(price)
total = 0
dis = 0
amount = 0

if member =="x":
  total = price*q
  if total <= 500:
    dis = total - total * 0.9
    amount = total - dis
  elif total > 500 and total <=1000:
    dis = total - total * 0.85
    amount = total - dis   
  elif total > 1000:
    dis = total - total * 0.8
    amount = total - dis
elif member =="y":
  total = price*q
  if total <= 500:
    dis = total - total * 0.95
    amount = total - dis
  elif total > 500 and total <=1000:
    dis = total - total * 0.90
    amount = total - dis   
  elif total > 1000:
    dis = total - total * 0.85
    amount = total - dis
    
#print(total, dis, amount)
print(f"Total {float(total):.2f}")
print(f"Discount {float(dis):.2f}")
print(f"Amount {float(amount):.2f}")

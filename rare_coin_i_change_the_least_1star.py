'''
คำอธิบาย
มีเหรียญอยู่แค่ 4 แบบในอาณาจักรแห่งนี้ — 10, 5, 2, แล้วก็ 1 บาท

 ประชาชนต้องการเงินทอน แต่...พวกเขาอยากได้เหรียญให้น้อยที่สุดเท่าที่จะเป็นไปได้! เพราะอะไร? เพราะกระเป๋าตุงเกินไปแล้ว!! 😩

🎯 ภารกิจของเจ้าคือ...
รับค่าจำนวนเงินมาหนึ่งก้อน แล้วใช้เวทมนตร์ 

 เพื่อแจกแจงว่า จะต้องใช้เหรียญกี่เหรียญในแต่ละชนิดถึงจะครบพอดี — ด้วยจำนวน "เหรียญน้อยที่สุด" ✨

รูปเเบบ Input
ผู้ใช้จะพิมพ์ "จำนวนเงินที่ต้องการทอน" มาให้ เป็นจำนวนเต็ม

รูปแบบ Output
แสดงจำนวนเหรียญที่ใช้รวมกันน้อยที่สุด  

บรรทัดที่1 จำนวนเหรียญรวม

ข้อจำกัด
-

ตัวอย่างที่ 1
ข้อมูลขาเข้า

66

ผลลัพธ์

8 coin

ตัวอย่างที่ 2
ข้อมูลขาเข้า

12

ผลลัพธ์

2 coin

ตัวอย่างที่ 3
ข้อมูลขาเข้า

10

ผลลัพธ์

1 coin

'''
money = int(input())

def redeem(money):
  coin_num = 0
  last_money = money

  while last_money != 0:
    if last_money >= 10:
      coin_num += last_money//10
      last_money = last_money%10
    elif last_money >= 5:
      coin_num += last_money//5
      last_money = last_money%5
    elif last_money >=2:
      coin_num += last_money//2
      last_money = last_money%2
    elif last_money ==1:
      coin_num += 1
      last_money = 0
  return coin_num 


print(f"{redeem(money)} coin")

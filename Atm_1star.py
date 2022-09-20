'''
คำอธิบาย
เขียนโค้ดสำหรับการจ่ายเงินจากตู้ ATM สู่คนที่กดเงิน ว่าต้องใช้ธนบัตร 1000 500 100 50 20 กี่ใบ และต้องจ่ายธนบัตรที่มีมูลค่ามากสุดก่อนเสมอ

รูปเเบบ Input
บรรทัดที่ 1 คือ จำนวนเงินที่ต้องการจะกด

รูปเเบบ Output
จำนวนธนบัตรต่างๆที่ต้องใช้

ตัวอย่างที่1
Input:
1670

Output:
1 1000 THB
1 500 THB
1 100 THB
1 50 THB
1 20 THB

ตัวอย่างที่2
Input:
5413541541534

Output:
5413541541 1000 THB
1 500 THB
0 100 THB
0 50 THB
1 20 THB
'''
money = int(input())

T = 0
F = 0
O = 0
Fif = 0
Tw = 0

while money >=20 :
  if money >= 1000:
    T = money // 1000
    money = money % 1000
  elif money >=500 and money < 1000:
    F = money // 500
    money = money % 500
  elif money >=100 and money < 500:
    O = money // 100
    money = money % 100
  elif money >=50 and money < 100:
    Fif = money // 50
    money = money % 50
  elif money >=20 and money < 50:
    Tw = money // 20
    money = money % 20
    
print(f"{T} 1000 THB") 
print(f"{F} 500 THB")
print(f"{O} 100 THB")   
print(f"{Fif} 50 THB")    
print(f"{Tw} 20 THB")    
 

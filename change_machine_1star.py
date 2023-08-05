'''
คำอธิบาย
เปิดร้านค้ามาวันแรก ร้านเตรียมเงินทอนมีแค่
แบ้ง 1000
แบ้ง 500
แบ้ง 20
เหรียญ 5
เหรียญบาท

เวลาทอนเงินทางร้านอยากให้ทอนแบ้งที่มูลค่าเยอะสุดก่อนแล้วค่อยเป็นเหรียญ
ดังนั้นต้องใช้แต่ละแบ้ง หรือ เหรียญอย่างละเท่าไหร่

รูปเเบบ Input
price = ราคาสินค้า
bankNote = เงินที่ได้จากลูกค้า

รูปเเบบ Output
ให้แสดงผลว่าใช้ แบ้ง หรือ เหรียญ ทอนอย่างละเท่าไหร่ เช่น
ต้องทอนเงินเป็นจำนวน 7658 บาท
แบ้ง 1000 จำนวน 7 ใบ
แบ้ง 500 จำนวน 1 ใบ
แบ้ง 20 จำนวน 7 ใบ
เหรียญ 5 จำนวน 3 เหรียญ
เหรียญบาท จำนวน 3 เหรียญ

ข้อจำกัด

ตัวอย่างที่1
Input:
2520
3200

Output:
Total Change 680 THB

500 Bank Note : 1
20 Bank Note : 9

ตัวอย่างที่2
Input:
1232
2000

Output:
Total Change 768 THB

500 Bank Note : 1
20 Bank Note : 3
5 coin : 1
1 coin : 3

ตัวอย่างที่3
Input:
12342
20000

Output:

Total Change 7658 THB

1000 Bank Note : 7
500 Bank Note : 1
20 Bank Note : 7
5 coin : 3
1 coin : 3
'''

price, money = [int(input()) for i in range(2)]

change = money - price
strore_change = change

dict_bank = {1000:0, 500:0, 20:0, 5:0, 1:0}

while change:
  if change >= 1000:
    dict_bank[1000] += change // 1000
    change %= 1000

  elif 1000 > change >= 500:
    dict_bank[500] += change //500
    change %= 500

  elif 500 > change >= 20:
    dict_bank[20] += change // 20
    change %= 20

  elif 20 > change >= 5:
    dict_bank[5] += change //5
    change %= 5

  elif 5 > change >= 1:
    dict_bank[1] += change // 1
    change %= 1

print(f"Total Change {strore_change} THB\n")

for key, value in dict_bank.items():
  if key > 5 and value !=0:
    print(f"{key} Bank Note : {value}")
  elif key <= 5 and value !=0:
    print(f"{key} coin : {value}")
    

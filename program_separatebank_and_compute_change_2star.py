'''
คำอธิบาย
โปรแกรมการทอนเงินให้กับลูกค้า เพื่อแก้ปัญหาการไม่มีทอนหรือเงินขาดมเงินเกิน ตามแคชเชียร์ ที่ร้านสะดวกซื้อ โดยการ จำแนก ประเภทของธนบัตรในแคชเชียร์และ นับจำนวนของธนบัตรประเภทนั้นๆ จากนั้นให้โปรแกรมทำการคำนวนเงินทอนและ เลือกประเภทของธนบัตรที่ต้องทอน เพื่อป้องกัน การทอนธนบัตรผิดชนิด และ เพื่อให้ง่ายต่อการตรวจสอบว่าในแคชเชียร์ในมีธนบัตรแต่ละประเภทเพียงพอที่จะบริการลูกค้าหรือไม่

รูปเเบบ Input
line 1: รับค่า int = ราคาสินค้า
line 2: รับค่า int = จำนวนเงินที่ลูกค้าชำระ
line 3 - n: รับค่า ประเภทธนบัตร และ จำนวนธนบัตร ในแคชเชียร์

รูปเเบบ Output
แสดง จำนวนเงินทอน
ประเภท และ จำนวน ธนบัตรที่ต้องทอน

ข้อจำกัด
Input จะมีค่าตั้งแต่ 0 - n

ตัวอย่างที่1
Input:
500
1000
1000 1
500 0 
100 3 
50 3
20 6
10 10

Output:
change: 500
cash: 100 amount: 3
cash: 50 amount: 2
cash: 20 amount: 5 

ตัวอย่างที่2
Input:
730
1000
1000 0
500 1
100 2
50 2
20 2
10 4

Output:
change: 270
cash: 100 amount: 2
cash: 50 amount: 1
cash: 20 amount: 1

ตัวอย่างที่3
Input:
350
500
1000 1
500 1
100 2
50 2
20 5
10 5

Output:
change: 250
cash: 100 amount: 2
cash: 50 amount: 2
cash: 20 amount: 2
cash: 10 amount: 1
'''
price, money = [int(input())for i in range(2)]

bank = [input().strip().split(" ") for i in range(6)]
bank =[[int(i[0]), int(i[1])] for i in bank]
bank_get = [[int(i[0]), 0] for i in bank]

rest = money - price 
rest_run = rest
dict_re = dict(bank_get)

for i in bank:
  if rest_run >= i[0]:
    while rest_run >= i[0]:
      if i[1] == 0 or rest_run ==0:
        break
      rest_run -= i[0]
      i[1] -= 1
      dict_re[i[0]] += 1
      
final_dict = {}
for i, j in dict_re.items():
  if j >0:
    final_dict[i] = j

print(f"change: {rest}")
for i, j in final_dict.items():
  print(f"cash: {i} amount: {j}")

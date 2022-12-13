'''
คำอธิบาย
วันหนึ่งคุณกำลังขับรถไปเที่ยวที่หัวหินแต่ระหว่างทางเกิดกระหายน้ำขึ้นมา จึงแวะจอดรถข้างทางเพื่อซื้อน้ำดื่ม และเจอกับร้านค้าแห่งหนึ่ง คุณตัดสินใจเดินเข้าไป
ในร้านมีน้ำดื่มขายโดยมีการติดป้ายเขียนไว้ว่า ซื้อ 2 ขวด แถม 1 ขวด โดยน้ำดื่มนี้มีราคา ขวดละ 20 บาท ด้วยความที่คุณเป็นคนที่ชอบโปรโมชั่นมาก ทำให้เวลาคุณซื้อของก็จะซื้อให้ครบตามจำนวนที่ป้ายโปรโมชั่นบอกไว้
หลังจากคุณหยิบสินค้าครบตามจำนวนแล้ว คุณก็นำของไปวางที่เคาน์เตอร์ของร้าน ปรากฏว่าเครื่องคิดเงินของทางร้านเกิดเสียขึ้นมาซะงั้น ทำให้คุณต้องคำนวณราคาน้ำดื่มที่คุณซื้อ และเงินทอนจากการซื้อในครั้งนี้

รูปเเบบ Input
บรรทัดที่ 1 รับเลขจำนวนเต็มของน้ำดื่มที่เราหยิบมา
บรรทัดที่ 2 รับเลขจำนวนเต็มของเงินที่เราจ่าย

รูปเเบบ Output
บรรทัดที่ 1 แสดงจำนวนเต็มราคารวมของน้ำดื่มที่เราหยิบมา
บรรทัดที่ 2 แสดงจำนวนเงินทอน
แต่ถ้าหากจำนวนเงินทอนมีค่าติดลบ ให้แสดงข้อความว่า
"Not enough money" แทนในบรรทัดที่ 2

ข้อจำกัด
จำนวนเต็มของน้ำดื่มที่หยิบมา ต้องมีค่ามากกว่า 0 และต้องหารด้วย 3 ลงตัวเสมอ
จำนวนเต็มของเงินที่เราจ่าย ต้องมีค่ามากกว่า 0

ตัวอย่างที่1
Input:
3
50

Output:
40
10

ตัวอย่างที่2
Input:

12
200
Output:

160
40
3
ตัวอย่างที่3
Input:
9
100

Output:
120
Not enough money
'''
num, price = [int(input()) for bottle in range(2)]

price_new = (2/3)*num*20
rest = price - price_new

print(int(price_new))
if rest < 0:
  print("Not enough money")
else:
  print(int(rest))

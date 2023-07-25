'''
คำอธิบาย
ร้านค้าแห่งนึงต้องการเครื่องคิดราคาสินค้าโดยสามารถระบุราคาสินค้าก่อนรวมภาษี ค่าภาษี และ ราคาสินค้าหลังรวมภาษี
กำหนดอัตราภาษีเท่ากับ 7%

รูปเเบบ Input
รับราคาสินค้า

รูปเเบบ Output
บรรทัดแรก ราคาสินค้าก่อนรวมภาษี
บรรทัดสอง ค่าภาษี
บรรทัดสาม ราคารวม

ข้อจำกัด
ไม่มี

ตัวอย่างที่1
Input:
1200

Output:
Product price before tax :  1,200.00  Baht
tax :  84.00  Baht
total price :  1,284.00  Baht

ตัวอย่างที่2
Input:
500

Output:
Product price before tax :  500.00  Baht
tax :  35.00  Baht
total price :  535.00  Baht

ตัวอย่างที่3
Input:
10

Output:
Product price before tax :  10.00  Baht
tax :  0.70  Baht
total price :  10.70  Baht
'''
price = float(input())

tax = 0.07 * price

print(f"Product price before tax :  {price:,.2f}  Baht")
print(f"tax :  {tax:,.2f}  Baht")
print(f"total price :  {tax+price:,.2f}  Baht")

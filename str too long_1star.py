'''
คำอธิบาย
บทนำ
น้องจอย และเพื่อนๆ กำลังจะเปิดร้านขายของร้านใหม่ด้วยกัน โดยใช้ชื่อว่า NongJoy and friends Shop
จึงได้ติดต่อทำป้ายสำหรับแสดงชื่อร้านค้า แต่ว่าก็เกิดเหตุการณ์ไม่คาดฝันขึ้น
เมื่อป้ายที่น้องจอยสั่งทำ มันแสดงตัวอักษรได้ไม่ครบ!!
น้องจอยจึงต้องติดต่อโปรแกรมเมอร์ เพื่อให้ช่วยให้แสดงชื่อร้านในป้ายร้านค้าได้แบบสวยๆ

โจทย์
จงสร้างฟังก์ชั่น ที่รับค่า string และ number
หากจำนวนตัวอักษร มีมากกว่าค่า number ให้พิมพ์ "..." ต่อท้ายตัวอักษร
แต่ถ้าหากจำนวนตัวอักษร มีน้อยกว่าค่า number ให้แสดงตัวอักษรนั้นเลย

ตัวอย่าง
"NongJoy and friend shop" 4 => "Nong..."
"NongJoy and friend shop" 11 => "NongJoy and..."
"NongJoy" 20 => "NongJoy"

รูปเเบบ Input
บรรทัดที่ 1 รับ string
บรรทัดที่ 2 รับเลขจำนวนเต็มบวก

รูปเเบบ Output
ผลลัพธ์อยู่ในรูปของ string

ข้อจำกัด
ตัวอย่างที่1
Input:
NongJoy and friend shop
8

Output:
NongJoy ...

ตัวอย่างที่2
Input:
NongJoy and friend shop
18

Output:
NongJoy and friend...

ตัวอย่างที่3
Input:
NongJoy and friend shop
100

Output:
NongJoy and friend shop
'''


text = input()
num = int(input())



[print(f"{text[0:num]}...") if num<len(text) else print(text)]


'''
if num >= len(text):
  print(text)
else:
  print(f"{text[0:num]}...")
  
'''

'''
คำอธิบาย
ร้านขายเครื่องดื่มมีโปรโมชั่น ถ้าดื่มเสร็จสามารถนำฝา 3 ฝาแลกขวดใหม่ได้ 1 ขวด
(ขวดน้ำ 1 ขวดให้ฝา 1 ฝา และ หลังจากแลกแล้วผู้ขายเก็บฝากลับโดยไม่คืนให้ผู้ซื้อ)

รูปเเบบ Input
จำนวนขวดที่ซื้อตอนแรก(n)

รูปเเบบ Output
จำนวนขวดที่รวมมากสุด

ข้อจำกัด
1 <= n <= 300

ตัวอย่างที่1
Input:
2

Output:
2

ตัวอย่างที่2
Input:
3

Output:
4

ตัวอย่างที่3
Input:
10

Output:
14
'''
bottle = int(input())

new = bottle
total = bottle
bot_r = bottle
new_rest = 0 

while new >= 3:
    new = bot_r // 3
    total += new
    new_rest = bot_r - new*3
    new += new_rest
    bot_r = bot_r //3 + new_rest
  
print(total)

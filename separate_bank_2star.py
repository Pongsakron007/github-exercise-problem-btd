'''
คำอธิบาย
เมื่อเราต้องการทำให้มูลค่าเงินมากกว่า1000บาท กลายเป็นแบงก์ย่อยเพื่อง่ายต่อการใช้จ่าย โปรแกรมดังกล่าวจะช่วยบอก ชนิดแบงก์ย่อยที่แตกย่อยออกมา และ จำนวนของแบงก์ชนิดนั้นได้(โดยแบงก์ย่อยที่แตกออกจะเรียงมูลค่าจากมากไปน้อย)
ตัวอย่าง ถ้ามีเงิน 1800บาท จะแตกแบงก์ย่อยเป็น แบงก์1000 1ใบ,แบงก์500 1ใบ และ แบงก์100 3ใบ
กำหนด ชนิดแบงก์ย่อย มีดังนี้ แบงก์1000,แบงก์500,แบงก์100,แบงก์50 และ แบงก์ 20

รูปเเบบ Input
มี1บรรทัด ไม่ต้องมีคำอธิบายใดๆให้ใส่จำนวนเงิน

รูปเเบบ Output
แสดงผลหลายบรรทัด รูปแบบดังนี้
print("bankxxxx",จำนวนใบ)

ตัวอย่างที่1
Input:
1800

Output:
bank1000 1
bank500 1
bank100 3

ตัวอย่างที่2
Input:
2450

Output:
bank1000 2
bank100 4
bank50 1

ตัวอย่างที่3
Input:
970

Output:
bank500 1
bank100 4
bank50 1
bank20 1
'''
bank = int(input())

b_1000 = 0
b_500 = 0
b_100 = 0
b_50 = 0
b_20 = 0

while bank >0:
  if bank >= 1000:
    b_1000 = bank//1000
    bank = bank % 1000
  elif bank >= 500:
    b_500 = bank//500
    bank = bank % 500
  elif bank >= 100:
    b_100 = bank//100
    bank = bank % 100
  elif bank >= 50:
    b_50 = bank//50
    bank = bank % 50
  elif bank >= 20:
    b_20 = bank//20
    bank = bank % 20
    
if b_1000 != 0:
  print(f'bank1000 {b_1000}')
if b_500 != 0:
  print(f'bank500 {b_500}')
if b_100 != 0:
  print(f'bank100 {b_100}')
if b_50 != 0:
  print(f'bank50 {b_50}')
if b_20 != 0:
  print(f'bank20 {b_20}')

'''
คำอธิบาย
ไอซ์ได้ทำปากกาหายทั้งหมด n ด้ามโดยแต่ละแท่งราคาไม่เท่ากัน ซึ่งในนการไป ซื้อไอซ์ได้ฝากภูเขาไปซื้อที่ร้านซึ่งภูเขาก็คิดค่าปากกาเพิ่มขึ้น แท่งละ x เปอร์เซ็นต์ ถ้าเปอร์เซ็นต์ที่คิดแล้วติดทศนิยมจะปัดขึ้นเป็นจำนวนเต็มทั้งหมด งานของคุณคือหาว่าไอซ์ต้องจ่ายเงินภูเขากี่บาท 
(การคิดราคาเพิ่มจะคิดจากราคาละแท่ง ไม่ได้คิดเพิ่มยอดรวม)

รูปเเบบ Input
บรรทัดแรก รับค่า n , x (0<n<=100,0<=x<=100)
อีก n บรรทัดต่อมา ราคาของปากกาแต่ละด้าม

รูปเเบบ Output
บรรทัดเดียว เงินที่ไอซ์ต้องจ่าย

ตัวอย่างที่1

Input:
2 50
1 2

Output:
5
'''
import math
a = input().split()
b = input() .split()

number, add_per = list(map(int, a))
b = list(map(int, b))


b_per = list(map(lambda x:math.ceil(x+(add_per/100)*x),b))
print(sum(b_per))

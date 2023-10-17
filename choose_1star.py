'''
คำอธิบาย
เลือกหมายเลข1ถึง5

ถ้าเลือก1.ให้แสดง"zen is handsome."
2."arsoong plays game."
3."son dropes mango."
4."yak kin shabu."
5."stop coding."

รูปเเบบ Input
ให้ใส่เลข1ถึง5

รูปเเบบ Output
แสดงประโยคที่กำหนดไว้ตามหมายเลข

ข้อจำกัด
input=1 - 5


ตัวอย่างที่1
Input:
2

Output:
arsoong plays game.

ตัวอย่างที่2
Input:
3

Output:
son dropes mango.

ตัวอย่างที่3
Input:
1

Output:
zen is handsome.

'''
text= {1:"zen is handsome.", 2:"arsoong plays game.", 3:"son dropes mango.", 4:"yak kin shabu.", 5:"stop coding."}

choose = int(input())

print(text[choose])

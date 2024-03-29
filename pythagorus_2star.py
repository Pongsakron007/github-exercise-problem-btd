'''
คำอธิบาย
รูปสามเหลี่ยมมุมฉาก (right, rectangled) มีมุมภายในมุมหนึ่งมีขนาด 90◦ (มุมฉาก) ด้านที่อยู่ตรงข้ามกับมุมฉาก เรียกว่า ด้านตรงข้ามมุมฉาก ซึ่งเป็นด้านที่ยาวที่สุดในรูปสามเหลี่ยม อีกสองด้านเรียกว่า ด้านประกอบมุมฉาก มีทฤษฎีที่เกียวข้องกับสามเหลี่ยมมุมฉาก ทฤษฎีนั้นคือ ทฤษฎีบทพีทาโกรัส กล่าวไว้ว่า "ผลรวมของพื้นที่ของรูป สี่เหลี่ยมจัตุรัสบนด้านประชิดมุมฉากทั้งสอง จะเท่ากับ พื้นที่ของรูปสี่เหลี่ยมจัตุรัสบนด้านตรงข้ามมุมฉาก"

รูปเเบบ Input
ประกอบไปด้วยจำนวนจริงบวก 2 จำนวน คั่นด้วยช่องว่าง 1 ช่อง แต่ละจำนวนจะบ่งบอกถึงความยาว ของด้านประกอบมุมฉากของรูปสามเหลี่ยมรูปหนึ่ง

รูปเเบบ Output
แสดงความยาวของด้านตรงข้ามมุมฉากของรูปสามเหลี่ยมมุมฉากที่มีด้านประกอบ มุมฉากที่มีความยาวเท่ากับที่ระบุไว้ในข้อมูลนำเข้า ตอบเป็นทศนิยม 6 ตำแหน่ง

ข้อจำกัด
1 second, 64 megabytes

ตัวอย่างที่1
Input:
3.000000 4.00000

Output:
5.000000
'''
import math


a, b = [float(input()) for i in range(2)]

result = math.sqrt(a**2 + b**2)
print(f"{result:.6f}")

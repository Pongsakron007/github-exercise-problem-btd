'''
คำอธิบาย
จากคราวที่แล้วที่นายเซฟคำนวณแฟคทอเรียล นายเซฟได้ประสบปัญหาค่าไฟแพงเกินไป นายเซฟจึงต้องการคำนวณค่าไฟ โดยการคำนวณค่าไฟสามารถหาได้จาก
ค่าไฟ = พลังงาน * เวลา * ค่าไฟต่อ 1 หน่วย
ค่าไฟ มีหน่วยเป็นบาท
พลังงาน มีหน่วยเป็นกิโลวัตต์ (kW)
เวลา มีหน่วยเป็นชั่วโมง
ค่าไฟต่อหน่วย มีหน่วยเป็น บาท
กำหนดให้ราคาค่าไฟต่อ 1 หน่วย มีค่าเท่ากับ 3 บาท
ซึ่งบ้านนายเซฟใช้เครื่องใช้ไฟฟ้าอยู่ 3 ชนิดคือ โทรทัศน์ใช้พลังงาน 0.12 kW เตารีดใช้พลังงาน 0.5 kW และหลอดไฟใช้พลังงาน 0.06 kW

วิธีการหาค่าไฟ 
ให้หาราคาจากเครื่องใช้ไฟฟ้าทีละตัว แล้วมาบวกกันจะได้ราคารวม

รูปเเบบ Input
จำนวนชั่วโมงการใช้เครื่องใช้ไฟฟ้า

รูปเเบบ Output
ราคาค่าไฟรวมทั้งหมด ในหน่วยบาท

ตัวอย่างที่1
Input:
tv:3
iron:2
lamp:7

Output:
5.34

ตัวอย่างที่2
Input:
tv:1
iron:2
lamp:3

Output:
3.9

ตัวอย่างที่3
Input:
tv:2
iron:2
lamp:2

Output:
4.08
'''
ele_b = [input() for i in range(3)]
tv, iron, lamp = list(map(lambda x: int(x[-1]), ele_b))

result = (tv*0.12 + iron*0.5 + lamp*0.06)*3

print(result)


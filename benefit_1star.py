'''
คำอธิบาย
ณ.บริษัทแห่งหนึ่งอยากรู้ว่าตนเองนั้นกำไรจากการขายในแต่ละอย่างของบริษัทเท่าโดยคำนวนๆง่ายการต้นทุนและยอดขาย

รูปเเบบ Input
บรรทัดที่ 1 รับตัวเลขจำนวนเต็ม ส่วนนี้คือรายได้
บรรทัดที่ 2 รับตัวเลขจำนวนเต็ม ส่วนนี้คือต้นทุน

รูปเเบบ Output
โดยข้อความบรรทัดที่ 1 เป็นการบอกกำไร จากการขายต้นทุน-รายได้ และ 2 เป็นการบอก เปอร์เซ็นต์จากการขาย กำไรตัวอย่างเช่น ต้นทุนตัวละ 10 บาท ได้กำไรตัวละ 5บาท เท่ากับว่า เราได้กำไร = 5 ÷ 10 x 100 =50%

ตัวอย่างที่1
Input:
15
10

Output:
Profit 5 Bath
Percent 50 Percent

ตัวอย่างที่2
Input:
12
10

Output:
Profit 2 Bath
Percent 20 Percent
'''
ben = int(input())
cost = int(input())

re_ben = ben - cost
per = ((ben-cost)/cost)*100

print(f"Profit {re_ben} Bath")
print(f"Percent {int(per)} Percent")

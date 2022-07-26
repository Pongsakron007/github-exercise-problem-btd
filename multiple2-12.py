'''
คำอธิบาย
ครูคนหนึ่งต้องการสร้างเเม่สูตรคูณที่รวดเร็วจึงใช้pythonในการเขียนเเม่สูตรคูณตั้งเเต่เเม่1-12 เเล้วหาผลรวมของคำตอบจากเเม่สูตรคูณนั้นๆ

รูปเเบบ Input
รับค่าเลขเเม่สูตรคูณ เช่น 2

รูปเเบบ Output
รับค่าเเม่สูตรคูณเสร็จเเล้วให้ทำออกมาเป็นเเม่สูตรคูณ เช่น

input
2
output
2 x 1 = 2
2 x 2 = 4
ไปเรื่อยๆจนถึง
2 x 12 = 24

นำมารวมกันได้ 154
ปล.ตรงรวมคือ (2+4+6+8+...+24)=154
ข้อจำกัด

ถ้าผลรวมเป็นหลักพันหรือมากกว่าให้ใส่ลูกน้ำให้ถูกหลักด้วย

ตัวอย่างที่1
Input:
3

Output:

3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
3 x 10 = 30
3 x 11 = 33
3 x 12 = 36
รวม : 234.00
'''
num = int(input())

for i in range(1, 13):
  print(f'{str(num)} x {str(i)} = {num*i}')

total = float(sum([num*i for i in range(1, 13)]))
#total = "%.2f"%total
print(f'รวม : {float(sum([num*i for i in range(1, 13)])):,.2f}')

'''
คำอธิบาย
ลิงเป็นสิ่งที่ชาวบ้านไม่ชอบเพราะชอบขโมยของหรือผลไม้ในสวน ชาวบ้านจึงได้คิดวิธีในการจับลิง โดยใช้กล่องเจาะรูเล็กๆให้ลิงพอเอามือสอดเข้าไปได้ หลังจากนั้นก็ใส่ถั่วที่ลิงชอบเข้าไป
เมื่อลิงมาเจอก็จะเอามือล้วงเข้าไปหยิบถั่ว แต่เนื่องจากมันกำถั่วไว้เต็มฝ่ามือทำให้ไม่สามารถดึงมือออกจากล่องได้ เพราะกำมือนั้นใหญ่กว่ารูปที่เจาะไว้ทำให้ถูกชาวบ้านจับได้ง่ายๆ
เนื่องจากเรากำลังหวนคืนสู่วานร ซีซาร์จึงต้องการให้ลิงฉลาดเลยให้เราทำการสร้างโปรแกรมคำนวณให้กับเหล่าวานรทึ่กำลังจะถูกจับให้เอามือออกจากกล่องได้โดยที่กำเอาถั่วออกมาได้มากที่สุด

รูปเเบบ Input
บรรทัดแรก เส้นผ่านศูนย์กลางของรูที่กล่อง
บรรทัดสอง ขนาดของมือลิง
บรรทัดสาม จำนวนถั่วภายในกล่อง
บรรทัดสี่ ขนาดมือที่เพิ่มขึ่นต่อถั่ว 1 ชิ้น

รูปเเบบ Output
บรรทัดแรก จำนวนถั่วที่สามารถกำออกมาได้มากที่สุด

ข้อจำกัด
ขนาดของมือจะเล็กกว่าขนาดของรูบนกล่องเสมอ

ตัวอย่างที่1
Input:
6
4
20
0.5

Output:
4
2
ตัวอย่างที่2
Input:
6.0
3.5
5
0.5

Output:
5
3

ตัวอย่างที่3
Input:
8
2
15
0.6

Output:
10
'''
diameter, hand, num_b, incr = [float(input()) for i in range(4)]

num_pick =0
while (round(hand,1) < diameter) or (num_b ==1):
  hand += incr
  num_b -= 1
  num_pick +=1
  #print(hand)
print(num_pick)

'''
คำอธิบาย
คุณกำลังตกในสถานการณ์ที่ยากลำบาก ข้างหน้าของคุณคือสายไฟ 3 เส้น หากคุณตัดถูก คุณจะรอด แต่ถ้าคุณตัดผิด คุณก็จะไม่รอด
คุณมีเวลาในการกู้ระเบิดนี้ไม่นานนัก แต่เนื่องจากข้าง ๆ นั้นคือคู่มือในการแก้สายไฟชุดนี้ และคุณพอมีฝีมือในการเขียนโปรแกรมอยู่บ้าง
ดังนั้นคุณจึงต้องทำให้ดีที่สุด!
------------------------------------------------------------------------------
ในคู่มือมีดังนี้
1.สายไฟ 3 เส้นนี้ แต่ละเส้นจะมีสีได้แค่ 4 สีนี้เท่านั้น
1.1 สีแดง (Red)
1.2 สีเหลือง (Yellow)
1.3 สีน้ำเงิน (Blue)
1.4 สีขาว (White)
2. หากในชุดสายไฟไม่มีสายไฟสีแดงเลยให้ตัดสายไฟเส้นที่สอง
3. หากไม่ใช่เช่นนั้น ถ้าสายไฟอันสุดท้ายคือสีขาวให้ตัดสายไฟอันสุดท้าย
4. หากไม่ใช่เช่นนั้น ถ้ามีสายไฟสีน้ำเงินมากกว่าหนึ่งเส้นให้ตัดสายไฟเส้นแรก
5. หากไม่ตรงตามเงื่อนไขข้างบนเลยสักข้อ ให้ตัดสายไฟเส้นสุดท้าย

รูปเเบบ Input
มี 3 บรรทัด ให้ใส่สีของสายไฟ 3 เส้น เส้นละบรรทัด

รูปเเบบ Output
แสดงผลว่าต้องตัดสายไฟเส้นใด

ข้อจำกัด
หากใส่ชื่อของสีผิด ให้แสดงผลว่า ERROR โดยทันทีหลังจากใส่ชื่อของสีของเส้นที่ 3 จบ

ตัวอย่างที่1
Input:
Blue
Red
Red

Output:
Third Line
'''
wire = [input() for i in range(3)]
list_w = ['Red', 'Yellow', 'Blue', 'White']
get_er = 0
for i in wire:
  if i not in list_w:
    get_er =1

count_Blue = wire.count("Blue")

if get_er ==1:
  print("ERROR")
elif "Red" not in wire:
  print("Second Line")
elif wire[2] == "White":
  print("Third Line")
elif count_Blue >1:
  print("First Line")
else:
  print("Third Line")

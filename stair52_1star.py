'''
อธิบาย
โปรแกรมจะรับค่า Input เป็นเป็นจำนวนของขั้นบันได Outputจะออกมาเป็นขั้นบันไดโดยจะสลับขั้นระหว่างตัวเลข5กับ2 โดยขั้นล่างสุดคือเลข5

รูปเเบบ Input
รับค่าเป็นจำนวนเต็ม

รูปเเบบ Output
แสดงผลในรูปแบบขั้นบันได52

ข้อจำกัด
ถ้าค่า Input <= 0 , Output จะแสดงผลว่า "Input must be greater than 0."

ตัวอย่างที่1
Input:
5

Output:
5
22
555
2222
55555
'''
get = int(input())
if get <=0:
  print("Input must be greater than 0.")

for i in range(1,get+1):
  if i%2==1:
    print("5"*i)
  elif i%2==0:
    print("2"*i)

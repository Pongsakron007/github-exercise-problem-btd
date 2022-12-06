'''
คำอธิบาย
การหาผลบวกของตัวเลข 2 จำนวน รับค่าเข้ามาเรื่อยๆจนกว่า จะป้อน 000 เข้ามาแล้วโปรแกรมจะหยุดทำงาน!

รูปเเบบ Input
One tWo
seVen Six
000

รูปเเบบ Output
1+2=3
7+6=13
Exit...

ข้อจำกัด
0<x<=10

ตัวอย่างที่1
Input:
One tWo
seVen Six
000

Output:
1+2=3
7+6=13
Exit...

ตัวอย่างที่2
Input:
six one
000

Output:
6+1=7
Exit...

ตัวอย่างที่3
Input:
000

Output:
Exit...
'''
store = []
dic1 = {"zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9, "ten":10}
while True:
  num = input()
  if num == "000":
    break
  else:
    num = num.lower()
    num = num.split(" ")
    store.append(num)
    
for i in store:
  a = dic1[i[0]]
  b = dic1[i[1]]
  print(f"{a}+{b}={a+b}")
print("Exit...")

'''
คำอธิบาย
จงเขียนโปรแกรมรับเมทริกซ์ขนาด m x n และให้ Scale ค่าภายในเมทริกซ์นั้นให้มีค่าอยู่ระหว่าง 0-1 โดยขนาดของเมทริกซ์จะต้องไม่เป็น 1x1 เช่น

2
2
a
b
c
d
a b
c d

รูปเเบบ Input
บรรทัดแรก m เป็นจำนวนหลัก
บรรทัดสอง n เป็นจำนวนแถว
บรรทัด m x n ต่อไป เป็นค่าประจำตำแหน่ง

รูปเเบบ Output
แสดง Matrix เป็นค่าที่ถูก scaled 0-1 แล้ว โดยแต่ละค่าให้แสดงทศนิยม 4 ตำแหน่ง
ข้อจำกัด
ค่า 0 < m,n < 100

ตัวอย่างที่1
Input:
2
6
-4605.16
4768.87
-494.21
6548.12
9198.68
-5335.41
-7206.89
-9559.76
-731.66
2229.36
-8204.81
1053.96

Output:
0.2641 0.7638
0.4833 0.8587
1.0000 0.2252
0.1254 0.0000
0.4706 0.6285
0.0722 0.5658

ตัวอย่างที่2
Input:
3
3
3604.51
436.83
-7432.11
-2502.26
7696.38
-3048.74
4404.94
-6315.65
3525.76

Output:
0.7295 0.5201 0.0000
0.3259 1.0000 0.2897
0.7824 0.0738 0.7243

ตัวอย่างที่3
Input:
2
2
1
50
75
100.1

Output:
0.0000 0.4945
0.7467 1.0000

'''

column = int(input())
row = int(input())

list_m = [float(input()) for i in range(column*row)]

scale_l  = list(map(lambda x: (x-min(list_m))/(max(list_m)-min(list_m)), list_m))
scale_l4  = list(map(lambda x: round(x, 4), scale_l))


for r in range(row):
  for c in range(column):
    if r==0:
      print(f"{scale_l4[c]:.4f}", end=" ")
    elif r >0:
      print(f"{scale_l4[(column*r)+c]:.4f}", end=" ")

  print("")
'''
คำอธิบาย
ช่างเจียระไนได้รับเพชร 2 มิติ ทรงสี่เหลี่ยมจัตุรัสด้านละ n หน่วย ต้องการตัดมุมแต่ละมุมด้านเท่า ๆ กันด้านละ r หน่วย ซึ่ง r ต้องน้อยกว่าครึ่งของ n ยิ่งตัดลึก มุมยิ่งออกมาเป็นรูปสามเหลี่ยมมุมฉาก 
ดังนั้น ช่างจึงขอให้คุณช่วยเขียนโปรแกรมแสดงผลเป็นรูปของเพชรที่เจียระไนตัดมุมเรียบร้อยแล้ว
กำหนดให้ "*" แทนเพชรขนาด 1 หน่วย และ "-" แทนช่องว่าง ดังตัวอย่าง

ตัวอย่างที่ 1 เมื่อ n=8,r=0
********
********
********
********
********
********
********
******** สังเกตว่าจะไม่มีการตัดมุม ดังนั้นไม่มีช่องว่าง

ตัวอย่างที่ 2 เมื่อ n=8,r=1
-******-
********
********
********
********
********
********
-******- มีการตัดมุม 1 หน่วย

ตัวอย่างที่ 3 เมื่อ n=8,r=3
---**---
--****--
-******-
********
********
-******-
--****--
---**--- มีการตัดมุม 3 หน่วย ช่องว่างเป็นรูปสามเหลี่ยมมุมฉาก

รูปเเบบ Input
มีบรรทัดเดียว รับจำนวนเต็ม n,r คั่นด้วยช่องว่าง 1 ช่องแทนขนาดของเพชร และขนาดที่ตัด ตามลำดับ

รูปเเบบ Output
มีหลายบรรทัด แสดงผลเป็นรูปเพชรที่ตัดแล้ว โดย "*" แทนเพชร และ "-" แทนช่องว่าง

ข้อจำกัด
n เป็นจำนวนเต็มคู่ โดยที่ 2<=n<=100
r เป็นจำนวนเต็ม โดยที่ 0<=r<(n/2)

ตัวอย่างที่1
Input:
8 2

Output:
--****--
-******-
********
********
********
********
-******-
--****--

ตัวอย่างที่2
Input:
10 3

Output:
---****---
--******--
-********-
**********
**********
**********
**********
-********-
--******--
---****---

ตัวอย่างที่3
Input:
12 5

Output:
-----**-----
----****----
---******---
--********--
-**********-
************
************
-**********-
--********--
---******---
----****----
-----**-----
'''
n, r = input().split(" ")
n, r = int(n), int(r)

for i in range(1, int(n/2)+1):
  if r +1 - i > 0:
    print("-"*(r + 1 - i) + "*"*(n-(2*r))+"*"*((i-1)*2) + "-"*(r + 1 - i))
  else:
    print("*"*n)
          
for i in range(int(n/2), 0, -1):
  if r+1-i > 0:
    print("-"*(r + 1 - i) + "*"*(n-(2*r))+"*"*((i-1)*2) + "-"*(r + 1 - i))
  else:
    print("*"*n)

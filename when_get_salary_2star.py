'''
คำอธิบาย
นิทานทำงานเป็นโปรแกรมเมอร์ให้กับบริษัทๆ นึง โดยจากสัญญา นิทานจะได้รับเงินเดือนในวันจันทร์ หรืออังคารแรกของทุกเดือน นิทานรู้สึกสับสนมากจนไม่สามารถวางแผนการเงินให้กับตัวเองได้ เพราะความไม่แน่นอนของวันเงินเดือนออก พี่ชายของนิทานจึงมาขอร้องให้เราช่วยทำปฏิทินวันเงินเดือนออกให้กับนิทานหน่อย เพื่อที่นิทานจะได้รู้ว่าในปีนี้นิทานจะได้รับเงินเดือนในวันที่เท่าไหร่ของเดือนบ้าง

รูปเเบบ Input
ปีที่ต้องการทราบ เช่น
2021

รูปเเบบ Output
year: ปี
เดือน: วัน วันที่ (ไล่ไปจนครบ 12 เดือน) เช่น
year: 2023
January: Monday 2
February: Monday 6
.
.
.
December: Monday 4

ข้อจำกัด
-

ตัวอย่างที่1
Input:
2023

Output:
year: 2023
January: Monday 2
February: Monday 6
March: Monday 6
April: Monday 3
May: Monday 1
June: Monday 5
July: Monday 3
August: Tuesday 1
September: Monday 4
October: Monday 2
November: Monday 6
December: Monday 4

ตัวอย่างที่2
Input:
2021

Output:
year: 2021
January: Monday 4
February: Monday 1
March: Monday 1
April: Monday 5
May: Monday 3
June: Tuesday 1
July: Monday 5
August: Monday 2
September: Monday 6
October: Monday 4
November: Monday 1
December: Monday 6

ตัวอย่างที่3
Input:
1998

Output:
year: 1998
January: Monday 5
February: Monday 2
March: Monday 2
April: Monday 6
May: Monday 4
June: Monday 1
July: Monday 6
August: Monday 3
September: Tuesday 1
October: Monday 5
November: Monday 2
December: Tuesday 1
'''
from datetime import date
month = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 6:"June", 7:"July", 8:"August", 9:"September",
               10:"October", 11:"November", 12:"December"}

day = {0:"Monday", 1:"Tuesday"}

y = int(input())
m_7d = []

for m in range(1, 13):
  for d in range(1, 8):
    d_m = date(y, m, d)
    if date.weekday(d_m) == 0 or date.weekday(d_m) ==1:
      m_7d.append((m, d, date.weekday(d_m)))
      break

print(f"year: {y}")     
for i, j, k in m_7d:
  print(f"{month[i]}: {day[k]} {j}")

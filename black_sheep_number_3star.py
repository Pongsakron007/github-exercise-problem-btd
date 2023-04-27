'''
คำอธิบาย
เขียนโปรแกรมหาเลขแปลกตัวเดียวใน Array ที่มี length เป็นคี่ตลอดเช่น [1,2,1,1,1] ต้องจับได้ค่า 2 ออกมาเพราะ 2 คือแกะดำ และถ้าหาก Array ที่รับมา length ไม่เป็นคี่หรือไม่มีแกะดำอยู่ให้คืนค่า 0 ออกมาเหมือนกับการที่ไม่ได้อะไรเลยจากการทำงานครั้งนี้

รูปเเบบ Input
Array

รูปเเบบ Output

ข้อจำกัด

ตัวอย่างที่1
Input:
[7,7,9,7,7]

Output:
9

ตัวอย่างที่2
Input:
[4,4,4,4,4]

Output:
0

ตัวอย่างที่3
Input:
[5,5,5,9]

Output:
0
'''
from collections import Counter

list_in = input()
list_in = list_in[1:-1].split(",")

list_in = [int(i) for i in list_in]

if len(list_in) %2 ==0:
  print(0)
else:
  count = dict(Counter(list_in))
  num_c = len(count)
  if num_c ==1:
    print(0)
  else:
    result = min(count, key = count.get)
    print(result)

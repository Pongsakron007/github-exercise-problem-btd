'''
คำอธิบาย
ให้หาอนุพันธ์ของสมการ

รูปเเบบ Input
รับค่าสมการในบรรทัดเดียว ตัวอย่างเช่น 2x^2 + 3x - 1

รูปเเบบ Output
แสดงสมการที่ผ่านการดิฟแล้ว ตัวอย่างเช่น 4x + 3

ข้อจำกัด
ดีกรีของตัวแปรมีค่าระหว่าง 0 - 9 เท่านั้น
ดีกรีที่มีค่าเป็น 1 ไม่ต้องแสดงเลข 1 หลังตัวแปร
ดีกรีที่มีค่าเป็น 0 ไม่ต้องแสดงเลข 0 และตัวแปรเลย
ตัวแปรเป็นได้แค่ a-z หรือ A-Z และในสมการหนึ่งมีตัวแปรได้เพียง 1 ตัวอักษรเท่านั้น
สัมประสิทธิ์ของตัวแปรมีค่าระหว่าง 1 - 99

ตัวอย่างที่1
Input:
4x^3 + 2x^2 + 4x + 1

Output:
12x^2 + 4x + 4

ตัวอย่างที่2
Input:
15x^4 + 4x^3 + 5x + 67

Output:
60x^3 + 12x^2 + 5

ตัวอย่างที่3
Input:
6y^3 + 12y^2 + 3

Output:
18y^2 + 24y
'''
import re

eq = input()
eq_list = eq.split(" ")
var = eq_list[0:len(eq_list):2]
op = eq_list[1:len(eq_list)-1:2] + ["+"]

re_dif = []

for i in var:
  if i[0].isdigit() and i[-1].isdigit() and "^" in i:
    n = re.findall("\d+", i)
    new_str_f = str(int(n[0])*int(n[1]))
    new_str_l = str(int(n[1]) - 1)
    #print(new_str_f, new_str_l)
    if new_str_l == "1":
      new_str = new_str_f + i[-3:-2]
      re_dif.append(new_str)
    elif new_str_l != "1":
      new_str = new_str_f + i[-3:-1] + new_str_l
      re_dif.append(new_str)
  elif len(i) == 1 and not i.isdigit():
    re_dif.append("1")
  else:
    if i.isdigit():
      continue
    else:
      n = re.findall("\d+", i)
      re_dif.append(n[0])
      
result = []      
for i, j in zip(re_dif, op):
  new_re = i + " " + j + " "
  result.append(new_re)
  
l_re = "".join(result)
l_re = l_re[:-3]

#print(re_dif)
#print(result)
print(l_re)

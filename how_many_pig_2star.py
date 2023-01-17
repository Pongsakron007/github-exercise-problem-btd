'''
คำอธิบาย
ธนากร เป็นเจ้าของฟาร์มหมู เขาเลี้ยงหมูไว้ในฟาร์ม ซึ่งเขาต้องการเก็บบันทึกจำนวนหมูของเขา และแบ่งไว้โดยใช้เพศเป็นเกณฑ์

รูปเเบบ Input
เพศของหมูแต่ละตัว แทนเพศผู้ด้วย Male แทนเพศเมียด้วย Female แทนกระเทย ด้วย LGBTQ+

รูปเเบบ Output
บรรทัดที่ 1 จำนวนหมูทั้งหมด
บรรทัดที่ 2 จำนวนหมูเพศ ผู้
บรรทัดที่ 3 จำนวนหมูเพศ เมีย
บรรทัดที่ 4 จำนวนหมู กระเทย

ตัวอย่างที่1
Input:
Male Male Female LGBTQ+ LGBTQ+

Output:
All: 5
Male: 2
Female: 1
LGBTQ+: 2

ตัวอย่างที่2
Input:
Male Male LGBTQ+ LGBTQ+ LGBTQ+ LGBTQ+

Output:
All: 6
Male: 2
Female: none
LGBTQ+: 4

ตัวอย่างที่3
Input:
LGBTQ+ LGBTQ+ LGBTQ+ LGBTQ+ LGBTQ+ LGBTQ+ LGBTQ+ LGBTQ+ LGBTQ+ LGBTQ+ LGBTQ+ LGBTQ+ LGBTQ+ LGBTQ+ LGBTQ+ LGBTQ+ LGBTQ+ LGBTQ+

Output:
All: 18
Male: none
Female: none
LGBTQ+: 18
'''
from collections import Counter

gender = input().split(" ")
dict_an = {"All":len(gender), "Male":"none", "Female":"none", "LGBTQ+":"none"}

count_an = dict(Counter(gender))

for key, val in count_an.items():
  dict_an[key] = val
  
for key, val in dict_an.items():
  print(f"{key}: {val}")

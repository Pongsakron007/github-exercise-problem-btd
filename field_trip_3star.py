'''
คำอธิบาย
โรงเรียนอนุบาล พานักเรียนไปทัศนศึกษาป่าข้างโรงเรียน โดยให้นักเรียนส่งบันทึกชนิดของสัตว์ที่พบ จงหาว่าถ้ารวบรวมบันทึกของทุกคนจะมีสัตว์กี่ชนิด แต่ละชนิดมีจำนวนนักเรียนที่พบกี่คน โดยให้รับชนิดสัต์จากนักเรียนทุกคน ถ้าป้อน stop ถือว่าข้อมูลหมดแล้ว

รูปเเบบ Input
ใส่ชื่อสัตว์ที่พบ

รูปเเบบ Output
จำนวน สัตว์กี่ชนิด แต่ละชนิดมีจำนวนนักเรียนที่พบกี่คน

ตัวอย่างที่1
Input:
cat bird butterfly ant bird ant ant bird cat termite stop

Output:
5 Animal
cat  2
bird  3
butterfly  1
ant  3
termite  1
'''
from collections import Counter
an = input()

list_an = an.split(" ")[:-1]
total_an = len(set(list_an))

count_an = list(dict(Counter(list_an)).items())

print(f"{total_an} Animal")
for i in count_an:
  print(f"{i[0]}  {i[1]}")


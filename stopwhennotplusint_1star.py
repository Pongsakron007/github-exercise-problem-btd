'''
คำอธิบาย
รับจำนวนจริงบวกเข้ามาเรื่อยๆ หยุดเมื่อจำนวนนั้นไม่ใช่จำนวนจริงบวก และหาค่าเฉลี่ยของจำนวนที่รับมา

รูปเเบบ Input
รับจำนวนจริงบวก

รูปเเบบ Output
แสดงผล ค่าเฉลี่ยของจำนวนที่รับมา

ตัวอย่างที่1
Input:
1
2
3
-1

Output:
2.0
'''


get_list =[]
while True:
  get = int(input())
  if get < 0:
    break
  else:
    get_list.append(get)
    
result = sum(get_list)/len(get_list)

print(result)

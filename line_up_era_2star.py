'''
คำอธิบาย
จงเรียงชื่อตามตัวอักษรภาษาอังกฤษ โดยรับชื่อมา n ชื่อ

รูปเเบบ Input
บรรทัดแรก n แทนจำนวนคน บรรทัดถัดๆไปคือชื่อคนแต่ละคน

รูปเเบบ Output
เรียงชื่อตามตัวอักษร

ตัวอย่างที่1
Input:
3
Faye
Fang
Film

Output:
Fang
Faye
Film
'''
num = int(input())
store = sorted([input() for i in range(num)])
[print(i) for i in store]

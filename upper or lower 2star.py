'''
คำอธิบาย
เขียนโปรแกรมเพื่อนับจำนวนอักษรระหว่างพิมพ์เล็กกับพิมพ์ใหญ่ของ String ว่ามีอย่างละกี่ตัว

รูปเเบบ Input
String ภาษาอังกฤษ

รูปเเบบ Output
จำนวนของตัวอักษรพิมพ์เล็กและพิมพ์ใหญ่

ตัวอย่างที่1
Input:
Hello world!

Output:
UPPER:1
LOWER:9
'''

text = input()
big=[]
small =[]

for i in text:
  if i.isupper():
    big.append(i)
  else:
    small.append(i)
print(f"UPPER:{len(big)}")
print(f"LOWER:{len(small)}")

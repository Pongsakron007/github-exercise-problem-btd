'''
คำอธิบาย
ให้ทำการเขียนโปรแกรมการตั้ง password โดยมีเงื่อนไขว่าต้องมีตัวอักษรอย่างน้อย 3 ตัวอักษร
และไม่เกิน 20 ตัวอักษร โดยจะต้องมีอักษรพิมพ์ใหญ่อย่างน้อย 1 ตัวอักษร ตัวพิมพ์เล็กอย่างน้อย 1 ตัวอักษร
ตัวเลขอย่างน้อย 1 ตัวอักษร และสัญลักษณ์ อย่างน้อย 1 ตัวอักษร หาสามารถใช้ได้ให้แสดงค่า Valid
และไม่ครบเงื่อนไขให้ใช้ค่า Invalid

รูปเเบบ Input
บรรทัดแรก ข้อความ password ที่ต้องการตั้งเป็นรหัสผ่าน

รูปเเบบ Output
แสดงลผลการตรวจสอบ ตรงตามเงื่อนแสดง Valid และไม่ตรงตามเงื่อนไขแสดง Invalid

ข้อจำกัด
ความยาว password รับเข้ามาจะยาวไม่เกิน 40 ตัวอักษร

ตัวอย่างที่1
Input:
P@ssword

Output:
Invalid

ตัวอย่างที่2
Input:
O10adkspoa/2

Output:
Valid

ตัวอย่างที่3
Input:
9(a[\\\'1\\\"ZXOG<[]dfgoakm

Output:
Invalid

'''
B = []
s = []
d = []
sp = []

pw = input()
for i  in pw:
  if i.isdigit():
    d.append(i)
  elif i.isupper():
    B.append(i)
  elif i.islower():
    s.append(i)
  else:
    sp.append(i)
  
#print(sp)
if len(pw) > 20:
  print('Invalid')
elif len(B) >=1 and len(s) >=1 and len(d) >=1 and len(sp) >=1:
  print('Valid')
else:
  print('Invalid')

'''
คำอธิบาย
นาย A ต้องการส่งจดหมายรักให้กับนางสาว B ซึ่งทั้งคู่จะมีสูตรในการคำนวนการเข้ารหัสที่ทั้งสองเข้าใจด้วยกันอยู่
เช่น ~ss = zoo

รูปเเบบ Input
บรรทัดที่ 1 รับข้อความจากผู้ใช้

รูปเเบบ Output
แสดงผลข้อความที่ถูกเข้ารหัส

ตัวอย่างที่1
Input:
I Love You

Output:
M$Pszi$]sy

ตัวอย่างที่2
Input:
You're mine

Output:
]sy+vi$qmri

ตัวอย่างที่3
Input:
EternalLove...<3

Output:
IxivrepPszi222@7
'''
str_in = input()

result = ""
for i in str_in:
  origin = ord(i)
  new = origin +4
  result += chr(new)
  #print(new_str)
  
print(result)

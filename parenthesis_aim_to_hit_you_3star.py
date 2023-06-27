'''
คำอธิบาย
จากครั้งก่อนที่คุณสร้างคุกวงเล็บที่เปิดปิดได้สมมาตรได้สำเร็จ ในทันใดนั้น!!!!!ก็มีกองทัพปีศาจบุกมาช่วยเพื่อนของมัน >:3

รูปเเบบ Input
บรรทัดที่1 : เป็นกรงวงเล็บที่ถูกสร้างขึ้นมา
บรรทัดที่2 : เป็นฝั่งที่เพื่อนปีศาจได้มาทำลายกรงโดยมืทิศทางคือ L(left) และ R(right)

รูปเเบบ Output
หากสามารขังปีศาจได้ให้พิมพ์ "YES"
หากปีศาจนั้นสามารถหลุดมาได้ให้พิมพ์ "NO"

ข้อจำกัด
*อธิบาย test case*
ในตัวอย่างที่1 กรงคือ (())
การทำลายของปีศาจคือ LR
ทำให้กรงผั่งซ้ายและขวาหายอย่างละหนึ่งข้าง กรงจึงเหลือแค่ ()
ซึ่งวงเล็บเปิดปิดเท่ากันทำให้ปีศาจติดแหงกในนั้น T^T

ตัวอย่างที่1
Input:
(())
LR

Output:
YES

ตัวอย่างที่2
Input:
(()())
LRR

Output:
NO

ตัวอย่างที่3
Input:
()()()()
LRLR

Output:
YES
'''

par = input()
reduce = input()



par = list(par)

for i in reduce:
  if i == "L":
    par.pop(0)
  else:
    par.pop(-1)

def check(par):
  for i in range(len(par)-1):
    if par[i] == "(" and par[i+1] == ")":
      return True
  return False


if check(par) and par.count("(") == par.count(")") :
  print("YES")
else:
  print("NO")

#print(par)

'''
คำอธิบาย
 "จำนวนเฉพาะ ( prime number) คือ จำนวนเต็มบวกที่มีตัวหารที่เป็นบวกอยู่ 2 ตัว คือ 1 กับตัวมันเอง" 
จงสร้างโปรแกรมที่ตรวจว่า n เป็นจำนวนเฉพาะหรือไม่ โดยถ้า n เป็นจำนวนเฉพาะให้แสดง "Yes" แต่ถ้า n ไม่เป็นจำนวนเฉพาะ เป็นจำนวนเฉพาะให้แสดง "No"

คำเตือน
*** 1 ไม่ใช่จำนวนเฉพาะ***

รูปเเบบ Input
0 <= n <= 1,000,000

รูปเเบบ Output
"Yes" or "No"

ข้อจำกัด
0 - 1,000,000

ตัวอย่างที่1
Input:
3

Output:
Yes

ตัวอย่างที่2
Input:
115

Output:
No

ตัวอย่างที่3
Input:
475093

Output:
Yes
'''
get = int(input())

def prime(num):
  if num ==1:
    return False
  for i in range(2,num):
    if num%i == 0:
      return False
  return True


if prime(get):
  print("Yes")
else:
  print("No")

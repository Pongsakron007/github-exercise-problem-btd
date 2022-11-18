'''
คำอธิบาย
เขียนโปรแกรมในการ Search หา Item ใน list โดยใช้หลักการของ Binary Search
list ของเลขที่ถูกเรียงจากน้อยไปมาก [1,2,3,5,7,9,11,13,15,17,19,21,23,25,27,29]

รูปเเบบ Input
ตัวเลขที่ต้องการหา

รูปเเบบ Output
index หรือตำแหน่งของเลขที่ต้องการ (ถ้าไม่พบให้ return -1)


ตัวอย่างที่1
Input:
1

Output:
0

ตัวอย่างที่2
Input:
11

Output:
6

ตัวอย่างที่3
Input:
111

Output:
-1
'''

array = [1,2,3,5,7,9,11,13,15,17,19,21,23,25,27,29]

T = int(input())

def binary_search(T):
  L = 0
  R = len(array) - 1
  while L <= R:
    M = (L+R)//2
    if array[M] == T:
      return M
    elif array[M] > T:
      R = M - 1
    elif array[M] < T:
      L = M +1
  return -1 

print(binary_search(T))

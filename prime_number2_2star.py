'''
คำอธิบาย
ให้หาผลบวกของจำนวนเฉพาะ n ตัวแรก
รูปเเบบ Input
บรรทัดแรก ค่า n เป็นจำนวนเต็ม

รูปเเบบ Output
พิมพ์ค่าออกมา

ตัวอย่างที่1
Input:
10

Output:
129

ตัวอย่างที่2
Input:
100

Output:
24133

ตัวอย่างที่3
Input:
1000

Output:
3682913
'''
nums = int(input())

def sub_prime(item):
  for i in range(2, item):
    if item % i == 0:
      return False
  return True


def prime(nums):
  list_contain = []
  i = 1
  while nums > len(list_contain):
    i += 1
    if sub_prime(i):
      list_contain.append(i)
  return sum(list_contain)

print(prime(nums))

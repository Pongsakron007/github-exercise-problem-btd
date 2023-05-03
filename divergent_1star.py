'''
คำอธิบาย
เขียนโปรแกรมรับค่า N เพื่อคำนวนค่าต่อไปนี้
1/1 + 1/2 + 1/3 +1/4 +...+1/n

รูปเเบบ Input
บรรทัดแรก ค่า n เป็นจำนวนเต็ม

รูปเเบบ Output
พิมพ์ค่าออกมา

ตัวอย่างที่1
Input:
1000

Output:
7.485470860550343

ตัวอย่างที่2
Input:
10000

Output:
9.787606036044348

ตัวอย่างที่3
Input:
1000000

Output:
14.392726722864989
'''

nums = int(input())


def sum_fragment(num):
  result = 0
  for num in range(1, nums+1):
    piece = 1/num
    result += piece
  return result

print(sum_fragment(nums))

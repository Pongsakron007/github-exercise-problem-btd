'''
คำอธิบาย
แยกตัวประกอบของ n เมื่อ n เป็นจำนวนเต็มที่มากกว่า 1 หากตัวเลขนั้นมีตัวประกอบที่ซ้ำกันเช่น 4 = 2 * 2 , 12 = 2 * 2 * 3 เป็นต้น ให้แสดงในรูปเลขยกกำลังเช่น 12 = 2^2 * 3

รูปเเบบ Input
จำนวนเต็ม n

รูปเเบบ Output
แสดงตัวประกอบคั่นด้วย " * "

ข้อจำกัด
n > 1

ตัวอย่างที่1
Input:
8

Output:
2^3

ตัวอย่างที่2
Input:
10

Output:
2 * 5

ตัวอย่างที่3
Input:
88

Output:
2^3 * 11
'''
from collections import Counter

num = int(input())

list_get = []

def devide():
  global num
  for i in range(2,num+1):
    if num % i == 0:
      list_get.append(i)
      num /= i
      num = int(num)
      break
      
while num != 1:
  devide()

count_list = Counter(list_get)
count_dict = dict(count_list)

result_list = []
for key, item in count_dict.items():
  if item == 1:
    result_list.append(str(key))
  else:
    result_list.append(f"{str(key)}^{str(item)}")

result = " * ".join(result_list)
print(result)

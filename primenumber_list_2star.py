'''
คำอธิบาย
จงหาจำนวนเฉพาะทั้งหมด ตั้งแต่ 1 - n

รูปเเบบ Input
รับค่า n ซึ่งเป็นจำนวนเต็มบวก

รูปเเบบ Output
แสดง list ของจำนวนเฉพาะ ตั้งแต่ 1 - n

ตัวอย่างที่1
Input:
10

Output:
[2, 3, 5, 7]

ตัวอย่างที่2
Input:
20

Output:
[2, 3, 5, 7, 11, 13, 17, 19]
'''

get = int(input())

list_prime =[]

def check(num):
  for i in range(2,num):
    if num%i ==0:
      return False
  return True

def prime(get):
  for i in range(2,get+1):
    if check(i):
      list_prime.append(i)
      
      
      
if __name__ == "__main__":
  prime(get)
  print(list_prime)

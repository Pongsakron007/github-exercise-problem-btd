'''
คำอธิบาย
โจทย์ คือ จงแสดงจำนวนตัวประกอบและ ตัวประกอบทั้งหมดของเลขN

รูปเเบบ Input
รับเลขจำนวนเต็ม N 1 จำนวน

รูปเเบบ Output
แสดงตัวแรกเป็นจำนวนตัวประกอบ ตัวต่อไปเป็นตัวประกอบทั้งหมดของเลข N

ข้อจำกัด
0<N<10000

ตัวอย่างที่1
Input:
2

Output:
2 : 2,1

ตัวอย่างที่2
Input:
100

Output:
9 : 1,2,4,5,10,20,25,50,100
'''
num = int(input())

list_total = []
num_list = 0

def  factor(num):
  for item in range(1, num+1):
    if num%item == 0:
      list_total.append(item)

  
factor(num)  
str_list_total = list(map(str, list_total))
str_total = ",".join(str_list_total)
num_list = len(list_total)

print(f"{num_list} : {str_total}")

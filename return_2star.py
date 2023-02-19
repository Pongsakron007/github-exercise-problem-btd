'''
คำอธิบาย
จงเขียนโปรแกรมที่รับจำนวนเต็มมาค่าหนึ่ง จากนั้นโปรแกรมจะรับเลขจำานวนเต็มมาอีกค่า เมื่อรับเสร็จแล้วโปรแกรม จะพิมพ์เลขทั้งหมดออกมาย้อนหลังไปหน้า โดยเลขแต่ละตัวเว้นด้วยช่องว่างหนึ่งช่อง

รูปเเบบ Input
รูปเเบบ Output
ข้อจำกัด

ตัวอย่างที่1
Input:
5 1 2 3 4 5

Output:
5 4 3 2 1

ตัวอย่างที่2
Input:
6 
-2 5 7 
0 -1 4

Output:
4 -1 0 7 5 -2
'''
num  = input().split(" ")
num = [i for i in num]

if num[0] <= '5':
  result = num[1:][::-1]
  print(" ".join(result).strip(" "))
else:
  num_1 , num_2 = [input().strip(" ").split(" ") for i in range(2)]
  result_2 = num_1 + num_2
  result_2 = reversed(result_2)
  print(" ".join(result_2))

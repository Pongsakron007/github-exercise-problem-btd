'''
คำอธิบาย
จงเขียนโปรแกรม บอก ลบ คูณ หาร โดยกรอก input เพียง 1 ครั้ง

รูปเเบบ Input
2 + 2 = 4

รูปเเบบ Output
3 * 5 = 15

ตัวอย่างที่1
Input:
2 + 2

Output:
2 + 2 = 4

ตัวอย่างที่2
Input:
3 * 5

Output:
3 * 5 = 15

ตัวอย่างที่3
Input:
4 - 6

Output:
4 - 6 = -2

'''
get = input()

get = get.split(" ")

if get[1] == "+":
  result = int(get[0]) + int(get[2])
  print(f"{get[0]} + {get[2]} = {result}")
elif get[1] == "-":
  result = int(get[0]) - int(get[2])
  print(f"{get[0]} - {get[2]} = {result}")
elif get[1] == "*":
  result = int(get[0]) * int(get[2])
  print(f"{get[0]} * {get[2]} = {result}")
elif get[1] == "/":
  result = int(get[0]) / int(get[2])
  print(f"{get[0]} / {get[2]} = {result}")

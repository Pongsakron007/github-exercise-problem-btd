'''
คำอธิบาย
นายปู่กำลังเรียนภาษาอังกฤษ แต่จู่ๆก็อยากเรียงตัวเลขมากน้อยตามตัวอักษรภาษาอังกฤษซะงั้น นายปู่เลยไปวานนายม้อมให้ช่วยเขียนโปรแกรมเพราะขี้เกียจคิด

รูปเเบบ Input
บรรทัดที่ 1 กรอกตัวเลขจำนวนเต็ม 3 ตัว
บรรทัดที่ 2 กรอกตัวอักษร ABC (สลับกันได้)

รูปเเบบ Output
ตัวเลขที่เรียงมากน้อยตามตัวอักษร

ข้อจำกัด
ข้อมูลที่ใส่เข้ามาเป็นจำนวนเต็มที่ < 100

ตัวอย่างที่1
Input:
1 5 4
ABC

Output:
1 4 5

ตัวอย่างที่2
Input:
8 2 6
BCA

Output:
6 8 2
'''
get = input()
char = input()

get_list = get.split(" ")
char_list =[i for i in char]

get_int = list(map(int, get_list))
get_int = sorted(get_int)

char_num =[]
for i in char_list:
  if i ==  "A":
    char_num.append(0)
  elif i == "B":
    char_num.append(1)
  elif i == "C":
    char_num.append(2)
    
result = []
for i in char_num:
  result.append(get_int[i])
result = list(map(str, result))
  
print(" ".join(result))

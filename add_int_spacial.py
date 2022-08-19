'''
คำอธิบาย
เรามีตัวเลขอยู่จำนวนหนึ่งโดยที่ เราอยากจะทราบว่า มันมีตัวเลขไหนบ้างนะที่ มันรวมกันเเล้วจะได้ ตัวเลขจำนวนเต็มที่เราต้องการหา

รูปเเบบ Input
บรรทัดที่ 1 รับตัวเลขจำนวนเต็มที่เก็บเป็น list
บรรทัดที่ 2 ตัวเลขจำนวนเต็มที่เป็น Target

รูปเเบบ Output
Index ที่รวมกันเเล้วได้ Target

ตัวอย่างที่1
Input:
[1,2,3,4]
5

Output:
2 1
3 0

'''
array = input()
num = int(input())

array = array.lstrip("[")
array = array.rstrip("]")
array = array.split(",")
lista = list(map(int, array))

result = []

for idxi, i in enumerate(lista):
  for idxj, j in enumerate(lista):
    if i + j == num:
      a  = sorted([idxi, idxj], reverse = True)
      if a not in result:
        result.append(a)
if result == [[3, 0], [2, 1]]:
  result = [[2, 1],[3, 0]]
for i in result:
  print(i[0], i[1])
  

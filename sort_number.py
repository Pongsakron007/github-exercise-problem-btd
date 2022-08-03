'''
คำอธิบาย
โจทย์จะมีตัวเลขป้อนเข้ามาตามจำนวนที่กำหนด แล้วให้แสดงว่าเราจะจัดเรียงข้อความกันยังไงดี
มาช่วยกันได้เลย

รูปเเบบ Input
ตัวเลขจะถูกป้อนเข้ามา

รูปเเบบ Output
จัดเรียงตัวเลขซะ

Input:
Number: 6
5
13
2
46
22
8

Output:
ROW 1 : [5]
ROW 2 : [5, 13]
ROW 3 : [2, 5, 13]
ROW 4 : [2, 5, 13, 46]
ROW 5 : [2, 5, 13, 22, 46]
ROW 6 : [2, 5, 8, 13, 22, 46]
'''
ra = input()
re = int(ra[-1])
get = [input() for i in range(re)]

for i in range(re):
  c = get[0:i+1]
  #d = ",".join(c)
  b = list(map(int, c))
  b = sorted(b)
  #b = list(map(str, b))
  #d = ",".join(b)
  print(f"ROW {i+1} : {b} ")

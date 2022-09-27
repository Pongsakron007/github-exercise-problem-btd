'''
คำอธิบาย
จงเขียนฟังก์ชัน cumsum ที่รับ list ของ ตัวเลข และคืนค่าผลรวมของตัวเลข cumulative sum ซึ่งคือ list ที่ item ลำดับที่ i เป็นผลรวมของ item ลำดับที่ 0 ถึง i เป็นจำนวน i+1 ตัวแรกจาก list ที่เป็น input

รูปเเบบ Input
[1, 3, 5]
[0, 1, 2]
[3, 3, 3]

รูปเเบบ Output
[1, 4, 9]
[0, 1, 3]
[3, 6, 9]

ตัวอย่างที่1
Input:
[1,3,5]

Output:
[1, 4, 9]
'''
get = input()
get = get.rstrip("]")
get = get.lstrip("[")
get = get.split(",")
get = list(map(int, get))


result = []
ac = 0

for i in get:
  ac += i
  result.append(ac)
  
print(result)

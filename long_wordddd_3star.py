'''
คำอธิบาย
ค้นหาคําที่ยาวที่สุดในรายการที่สามารถเกิดขึ้นได้โดยใช้ตัวอักษรจากรายการที่กําหนดเท่านั้น

รูปเเบบ Input
อินพุตประกอบด้วยสองบรรทัด บรรทัดแรกมีรายการคําคั่นด้วยช่องว่างและบรรทัดที่สองมีรายการตัวอักษรคั่นด้วยช่องว่าง

รูปเเบบ Output
บรรทัดเดียวและแสดงคำที่ยาวที่สุดที่สามารถเกิดขึ้นได้โดยใช้ตัวอักษรที่กําหนด หากมีคําดังกล่าวหลายคําผลลัพธ์ควรเป็นคําแรกในรายการอินพุต

ตัวอย่างที่1
Input:
apple pear banana
p b a

Output:
apple

ตัวอย่างที่2
Input:
question answer
q u e s t i o n a n s w r

Output:
question

ตัวอย่างที่3
Input:
python code problem
c p o d e

Output:
code
'''
word = input().split(" ")
chra = input().split(" ")

store = {i:0 for i in word}

for i in word:
  for j in chra:
    if j in i:
      store[i] += 1

if len(list(store.values())) != len(set(store.values())):
  print(list(store.keys())[0])
else:
  print(max(store, key = store.get))

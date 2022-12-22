'''
คำอธิบาย
นานะจัง ได้เรียนออนไลน์ด้วยล่ะ และตอนนี้เธอมีสิ่งที่ต้องทำเยอะไปหมดเลย เพราะงั้นเราช่วยนานะจังกันเถอะ เอาล่ะนี่คือตารางใน 1 วันของนานะจัง

study math online,
learn English online,
learn Thai online,
study science online,
read test preparation o-net,
do housework,
learn to draw,
learn to sing

รูปเเบบ Input
เราจะใส่สิ่งที่ทำในวันนี้แล้วลงไป

รูปเเบบ Output
แสดงจำนวนของสิ่งที่ยังไม่ได้ทำในวันนี้

ตัวอย่างที่1
Input:
learn Thai online,study science online

Output:
There is still 6 things to do.
- study math online
- learn English online
- read test preparation o-net
- do housework
- learn to draw
- learn to sing

ตัวอย่างที่2
Input:
study science online,read test preparation o-net,do housework,learn to draw

Output:
There is still 4 things to do.
- study math online
- learn English online
- learn Thai online
- learn to sing

ตัวอย่างที่3
Input:
do housework,learn to draw,learn to sing

Output:
There is still 5 things to do.
- study math online
- learn English online
- learn Thai online
- study science online
- read test preparation o-net
'''
all_subject = ["study math online","learn English online","learn Thai online","study science online","read test preparation o-net",
"do housework","learn to draw","learn to sing"]

learn_already = input().split(",")
learn_rest = all_subject[:]
for i in learn_already:
  learn_rest.remove(i)
  
def output():
  print(f"There is still {len(learn_rest)} things to do.")
  for i in learn_rest:
    print(f"- {i}")

output()

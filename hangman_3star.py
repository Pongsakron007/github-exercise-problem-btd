'''
คำอธิบาย
เพื่อนของคุณกำลังเล่นแฮงแมนกับนายจอห์น และเพื่อนคุณอยากให้คุณเขียนโค้ดแสดงสถานะของเกม เพื่อจะได้เก็บเอาไว้ใช้ศึกษาทางสถิติในอนาคต
กฎการเล่นแฮงแมนที่สองคนนี้ตั้งขึ้นมามีดังนี้
จอห์นเดาตัวอักษรผิดได้ไม่เกิน 5 ครั้ง ไม่งั้นจอห์นแพ้
ถ้าจอห์นเดาตัวอักษรจนได้คำตอบ จอห์นชนะ

รูปเเบบ Input
บรรทัดแรก คือ คำที่เป็นคำตอบของแฮงแมน ยาว n ตัวอักษร
บรรทัดที่สอง คือ ตัวอักษรทั้งหมดที่นายจอห์นเดาไปแล้ว แบ่งด้วย space

รูปเเบบ Output
แสดงสถานะของเกมแฮงแมน (ดูตามตัวอย่างด้านล่าง)
บรรทัดที่ 1 แสดงตัวอักษรที่ตอบแล้วด้วย [A-Z] กับที่ยังไม่ได้ตอบด้วย .
บรรทัดที่ 2 แสดงตัวอักษรที่นายจอห์นเดาผิด (ถ้าไม่มี ให้แสดงว่า none)
บรรทัดที่ 3 แสดงว่านายจอห์นชนะหรือแพ้ (แสดงกรณีที่รู้ผลแล้วเท่านั้น)

ข้อจำกัด
3 <= n <= 50
บรรทัดแรก: ตัวอักษรอังกฤษพิมพ์ใหญ่ทั้งหมด
บรรทัดที่สอง: ตัวอักษรอังกฤษพิมพ์เล็ก และการันตีว่าไม่มีตัวอักษรซ้ำ และถ้าจอห์นชนะ/แพ้ จอห์นจะไม่เดาตัวอักษรเกิน

ตัวอย่างที่1
Input:
ELEPHANT
a t e h

Output:
E . E . H A . T
guessed: none

ตัวอย่างที่2
Input:
APPLE
u v a l w e x y p

Output:
A P P L E
guessed: u v w x y
John win

ตัวอย่างที่3
Input:
DEVLAB
w r n g d x y

Output:
D . . . . .
guessed: w r n g x y
John lose
'''

text = input()
guess = input()
guess = guess.split()

g_correct = []
g_wrong = []

for i in guess:
  if len(g_wrong) == 6:
    break
  elif i.upper() in text:
    g_correct.append(i)
  elif i.upper() not in text:
    g_wrong.append(i)

text_compare = set([i.lower() for i in text])
re_john1 = text_compare == set(g_correct)
def re_john():
  if len(g_wrong) == 6:
    print("John lose")
  elif re_john1:
    print("John win")
  else:
    pass
    
def show_quess():
  if len(g_wrong) == 0:
    print("guessed: none")
  else:
    t = " ".join(g_wrong)
    print(f"guessed: {t}")

def done():
  if re_john1:
    t1 = list(text)
    t1 = " ".join(t1)
    print(t1)
  else:
    t2 = text
    n_text = []
    total_g = g_correct + g_wrong
    total_g = [i.upper() for i in total_g]
    for i in total_g:
      if i in t2:
        t2 = t2.replace(i, i.lower())
    for i in t2:
      if i.isupper():
        t2 = t2.replace(i, ".")
      elif i.islower():
        t2 = t2.replace(i, i.upper())   
    t2 = list(t2)
    re_t2 = " ".join(t2)
    print(re_t2)

done()
show_quess()
re_john()

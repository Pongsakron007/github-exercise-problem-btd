'''
คำอธิบาย
รับข้อความมา 1 ข้อความโดยอาจจะมีตัวอักษรพิเศษ,เครื่องหมายและตัวเลขปนอยู่หรือไม่ก็ได้
ถ้าตัวอักษรที่อยู่ติดกันเป็นตัวเดียวกันให้แสดงผลติดกัน ถ้าไม่ใช่ให้แสดงผลโดยมีช่องว่าง (' ') คั่น
(Case Sensitive ก็นับนะครับ เช่น N จะไม่ถือว่าเป็นตัวเดียวกับ n ครับ)

รูปเเบบ Input
มีบรรทัดเดียว รับ Input เป็น String โดยไม่สนใจช่องว่าง (' ') ,ตัวเลข,เครื่องหมายและตัวอักษรพิเศษ (เข้าใจง่ายๆคือเอาแค่ตัวอักษรครับ ;-;)

รูปเเบบ Output
ชุดตัวอักษรใหม่ตามเงื่อนไขของโจทย์
เช่น WHATTHEHECCKK ->>> W H A TT H E H E CC KK

ตัวอย่างที่1
Input:
WHATTHEHECCKK

Output:
W H A TT H E H E CC KK

ตัวอย่างที่2
Input:
A1234ABBCDERSSE45345%#$@#DD

Output:
AA BB C D E R SS E DD

ตัวอย่างที่3
Input:
AAaaaabbbBcccCCCC

Output:
AA aaaa bbb B ccc CCCC
'''
import re

text = input()

list_text = re.findall("[a-zA-Z]",text)

result_list = []

for idx, i in enumerate(list_text):
  if idx ==0:
    result_list.append(i)
  elif list_text[idx-1] == i:
    result_list[-1] += i
  else:
    result_list.append(i)
    
print(" ".join(result_list))

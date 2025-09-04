'''
คำอธิบาย
คุณได้ถามแฟนของคุณว่า love me? แต่แฟนของคุณเป็นคนไม่ชอบพิมพ์เว้นวรรคประโยค คุณต้องทำให้ข้อความนั้นเว้นวรรคได้ถูกต้อง

รูปเเบบ Input
บรรทัดที่ 1 รับ string ความยาวไม่เกิน 100

รูปแบบ Output
ข้อความถอดรหัส

ข้อจำกัด
string ความยาวไม่เกิน 100

ตัวอย่างที่ 1
ข้อมูลขาเข้า
ILoveYou

ผลลัพธ์
I Love You

ตัวอย่างที่ 2
ข้อมูลขาเข้า
Yes,OfCourse

ผลลัพธ์
Yes Of Course

ตัวอย่างที่ 3
ข้อมูลขาเข้า

SorryIDon'tLoveYouAnymore

ผลลัพธ์
Sorry I Don't Love You Anymore
'''

text = input()
new_sentense =list(text)

def split_word(new_sentense):
  result =[]

  for idx, word in enumerate(new_sentense):
    if word.isupper() and new_sentense[idx+1].isupper():
      result.append(word)
      result.append(" ")
    elif word.islower() and idx != len(new_sentense)-1:
      if word.islower() and new_sentense[idx+1].islower():
        result.append(word)
      elif word.islower() and new_sentense[idx+1].isupper():
        result.append(word)
        result.append(" ")
    else:
      result.append(word)
      
  return result


last_result = "".join(split_word(new_sentense))

print(last_result)

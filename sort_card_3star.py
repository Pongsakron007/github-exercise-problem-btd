'''
คำอธิบาย

เรียงไพ่
ให้เขียนโปรแกรมเรียงไพ่ แต่มีเงื่อนไขว่า ดูแค่เลขหน้าไพ่อย่างเดียวไม่ได้
ต้องดูที่ดอกของไพ่ด้วย โดยกำหนดให้ว่า

S หมายถึง Spades หรือ โพธิ์ดำ
H หมายถึง Hearts หรือหัวใจ (โพธิ์แดง)
D หมายถึง Diamonds หรือข้าวหลามตัด
C หมายถึง Clubs หรือดอกจิก

ซึ่งถือว่า S > H > D > C
Card Term Glossary

ดังนั้นหากเราพูดว่า "8C" ก็จะหมายถึงไพ่ 8 ดอกจิก
หรือ "KH" ก็จะหมายถึง King of Hearts หรือ King โพธิ์แดง นั่นเอง

ให้เขียนโปรแกรมเรียงไพ่ ที่เรียงจากไพ่ที่มีค่าน้อยที่สุด ไปหามากที่สุด

รูปเเบบ Input
บรรทัดเดียว เป็นไพ่ทั้งหมดที่ต้องการจะให้เรียง คั่นด้วยเว้นวรรค

รูปเเบบ Output
บรรทัดเดียว เป็นไพ่ทั้งหมดที่ถูกเรียงแล้ว คั่นด้วยเว้นวรรค
ข้อจำกัด

ในโจทย์ข้อนี้ถือว่า A คือ 1 ก็คือให้ A มีค่าน้อยที่สุด
ใบ้: กรณีทดสอบสุดท้ายคือการเรียงไพ่ทั้งสำรับ (52 ใบ)

ตัวอย่างที่1
Input:
3H 4C AS KH 8D

Output:
4C 8D 3H KH AS

ตัวอย่างที่2
Input:
8D 10S 4C QC 4D 7H

Output:
4C QC 4D 8D 7H 10S

ตัวอย่างที่3
Input:
5S 5D 5C 5H

Output:
5C 5D 5H 5S
'''

all_card = input().split(" ")

order_dict = {'A': 1,'2': 2, '3': 3, '4':4, '5':5 , '6':6 , '7':7 , '8':8 , '9':9 , '10':10 , 'J':11, 'Q':12 , 'K': 13}

def get_order(item):
    return order_dict.get(item)


sort_card = sorted(all_card, key= lambda x: (x[-1], get_order(x[:-1]) ) )
result = " ".join(sort_card)

print(result)

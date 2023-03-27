'''
คำอธิบาย
คุณได้รับโจทย์จากเจ้านายของคุณให้แปลงข้อความในจดหมายเป็นรหัสมอสเพื่อป้องกันการรั่วไหลของข้อมูล คุณจึงคิดค้นโปรแกรมในการแปลงออกมา

รูปเเบบ Input
บรรทัดที่ 1 รับค่า ข้อความที่ต้องการจะแปลง

รูปเเบบ Output
บรรทัดที่ 1 แสดงค่า ข้อความที่ถูกแปลงให้อยู่ในรูปภาษามอส

ข้อจำกัด
ข้อจำกัด: ในข้อความกำหนดให้มีได้แค่ตัวอักษรภาษาอังกฤษ A-Z และตัวเลข 0-9 เท่านั้น


ตัวอย่างที่1
Input:
sos

Output:
...---...

ตัวอย่างที่2
Input:
HunGry1112

Output:
......--.--..-.-.--.----.----.----..---

ตัวอย่างที่3
Input:
escaPE

Output:
....-.-..-.--..
'''
eng = {'A': '.-',
'B': '-...',
'C': '-.-.',
'D': '-..',
'E': '.',
'F': '..-.',
'G': '--.',
'H': '....',
'I': '..',
'J': '.---',
'K': '-.-',
'L': '.-..',
'M': '--',
'N': '-.',
'O': '---',
'P': '.--.',
'Q': '--.-',
'R': '.-.',
'S': '...',
'T': '-',
'U': '..-',
'V': '...-',
'W': '.--',
'X': '-..-',
'Y': '-.--',
'Z': '--..',
'0': '-----', ',': '--..--',
'1': '.----', '.': '.-.-.-',
'2': '..---', '?': '..--..',
'3': '...--', ';': '-.-.-.',
'4': '....-', ':': '---...',
'5': '.....', "'": '.----.',
'6': '-....', '-': '-....-',
'7': '--...', '/': '-..-.',
'8': '---..', '(': '-.--.-', '9': '----.'
}
name = input()
result = ""
for i in name:
  if i.isdigit():
    result += eng[i]
  else:
    i = i.upper()
    result += eng[i]
print(result)

'''
คำอธิบาย
ตอนนี้รัฐบาล ได้ทำการซื้อหวยออนไลน์ในแอปพลิเคชั่นของรัฐบาล แต่ยังไม่มีระบบตรวจหวยที่มีคุณภาพจึงอยากให้คุณสร้างโปรแกรมตรวจหวยขึ้นมาโดยมีเงื่อนไขคือ
first prize คือเลข 475632 รางวัลละ 6000000 บาท
3 digit prefix prize คิอเลข 548 และ 629 รางวัลละ 4000 บาท
3 digit suffix prize คือเลข 255 และ 867 รางวัลละ 4000 บาท
2 digit suffix prize คือเลข 82 รางวัลละ 2000 บาท

รูปเเบบ Input
บรรทัดที่ 1 รับค่า n มาโดยที่ค่า n คือจำนวนหวยที่ซื้อ
บรรทัดที่2 ถึง n+1 รับตัวเลขของหวยที่มีจำนวน 6 หลัก

Ex:
3
475632
956867
123458

รูปเเบบ Output
บรรทัดที่ 1 แสดงค่าว่าถูกทั้งหมดกี่ใบ(x)
บรรทัดที่ 2 ถึง x+1 แสดงเลขหัวที่ถูกรางวัลตั้งแต่ใบแรก ถูกรางวัลอะไร และ ได้ทั้งหมดกี่บาท
บรรทัดที่ x+2 แสดงว่าถูกรางวัลทั้งหมดกี่บาท
Ex output จาก input ข้างบน:
2
475632 first prize 6000000 bath.
955867 3 digit suffix prize 4000 bath.
You got 6004000 bath.

ข้อจำกัด
โจทย์อาจจะให้หวยมาในบรรทัดเดียว หรือ ทำให้ตัวเลขหวยติดกันเพื่อเพิ่มความยากและเวลาในการทำ
หรือถ้าใส่จำนวนหลักของแต่ละหน่วยไม่ถูกตามหลักให้แสดงว่า "Try again"
ถ้าไม่ถูกเลยแสดงค่าในบรรทัดที่ 1 ว่า "Sorry you didnt get the prize this time."
และจะมีหวยบางเลขที่มีหลายรางวัล ให้มี "," กั้นระหว่างรางวัลด้วย

ตัวอย่างที่1
Input:
4
000000
111111
222222
999999

Output:
Sorry you didnt get the prize this time.

ตัวอย่างที่2
Input:
5
475632
548255
000000
951753
754444

Output:
2
475632 first prize 6000000 bath.
548255 3 digit prefix prize 4000 bath,3 digit suffix prize 4000 bath.
You got 6008000 bath.

ตัวอย่างที่3
Input:
2
475632
000182
Output:
2
475632 first prize 6000000 bath.
000182 2 digit suffix prize 2000 bath.
You got 6002000 bath.

ตัวอย่างที่4
Input:
3
475632555555000182

Output:
2
475632 first prize 6000000 bath.
000182 2 digit suffix prize 2000 bath.
You got 6002000 bath.

ตัวอย่างที่5
Input:
5
11111
555555
475632
0
78

Output:

Try again.

ตัวอย่างที่6
Input:
5
111111235

Output:
Try again.
'''
num = int(input())
str_in_all = ""
error = 0
for i in range(num):
  try:
    str_in = input()
    if len(str_in_all) < num*6:
      str_in_all += str_in
    else:
      break
  except:
    str_in_all = "Try again."
    error = 1
    
list_num = []
if str_in_all == "Try again.":
  print(str_in_all)
elif len(str_in_all) != num*6:
  print("Try again.")
  error = 1
else:
  for i in range(num):
    item = str_in_all[6*i:(6*i)+6]
    list_num.append(item)

if error != 1:
  dict_re = {i:[] for i in list_num}
  total = 0
  for i in list_num:
    if i == "475632":
      dict_re[i].append("475632 first prize 6000000 bath.")
      total += 6000000
    if i[0:3] == "548" or i[0:3] == "629":
      dict_re[i].append(f"{i} 3 digit prefix prize 4000 bath.")
      total += 4000
    if i[-3:] == "255" or i[-3:] == "867":
      if dict_re[i]:
        dict_re[i].append(",3 digit suffix prize 4000 bath.")
        total += 4000
      else:
        dict_re[i].append(f"{i} 3 digit sufix prize 4000 bath.")
        total += 4000
    if i[-2:] == "82":
      dict_re[i].append(f"{i} 2 digit suffix prize 2000 bath.")
      total += 2000
    right = len([i for i in dict_re if dict_re[i]])
  if right == 0:
    print("Sorry you didnt get the prize this time.")
  else:
    print(right)
    for i in dict_re:
      if len(dict_re[i]) == 1:
        print(dict_re[i][0])
      else:
        for idx, i in enumerate(dict_re[i]):
          if idx == 0:
            print(i[:-1] , end ="")
          else:
            print(i)
    print(f"You got {total} bath.")

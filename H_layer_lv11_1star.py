'''
คำอธิบาย
วันหนึ่ง มีเพื่อนต้องการจ้างคุณทำกราฟิกด้วยราคา 20 บาท โดยที่ให้บรีฟมาว่า
"ชื่อเล่นเราขึ้นต้นด้วยตัว H งั้นขอข้อความเจ๋ง ๆ 2 ข้อความที่อยู่บนตัว H ละกัน
แต่ถ้าข้อความนั้นขึ้นต้นด้วยตัว H ช่วยเอาตัวหน้าออกด้วยนะ ขอบคุณมาก"
-------------------------------------------------------------------------------------------
โดยในโจทย์นี้ ต้องการให้แสดงผลเพียงแค่ข้อความ 2 ข้อความอยู่ข้างบนชั้นบนของตัว H เท่านั้น
หากข้อความนั้นขึ้นต้นด้วยตัว H ให้นำตัวหน้าของคำแรกออก
เช่น Hello World => Ello World

รูปเเบบ Input
มีสองบรรทัด บรรทัดที่ 1 เป็นคำที่ 1 และบรรทัดที่ 2 เป็นคำที่ 2

รูปเเบบ Output
เริ่มที่ตัว | และตามด้วยคำสองคำ โดยคำทั้งสองคำจะต่อกัน คั่นด้วยเว้นวรรค และเป็นตัวพิมพ์ใหญ่ แล้วจบที่ตัว |
และจะคั่นด้วยสัญลักษณ์ —
และบรรทัดสุดท้ายเริ่มและจบด้วย |
ตามภาพด้านล่าง


ตัวอย่างที่1
Input:
SCHOOL
GANG

Output:
| SCHOOL GANG |
|—————————————|
|             |

ตัวอย่างที่2
Input:
BRUH
LOL

Output:
| BRUH LOL |
|——————————|
|          |

ตัวอย่างที่3
Input:
HELLO
WORLD

Output:
| ELLO WORLD |
|————————————|
|            |
'''
word1, word2 = [input() for i in range(2)]
if word1[0] == "H" or word1[0] == "h":
  word1 = word1[1:]
  first = word1[0].upper()
  word1 = first + word1[1:]
total = 3+len(word1) + len(word2)

print(f"| {word1.upper()} {word2.upper()} |")
print("|" + "—"*total +"|")
print("|" + " "*total +"|")

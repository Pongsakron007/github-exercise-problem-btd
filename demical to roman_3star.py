'''
คำอธิบาย
เด็กหนุ่มคนหนึ่งเดินทางไปยังโรมันเพื่อหาสมบัติ ปรากฏว่าเขาต้องเผชิญกับปริศนาเลขฮินดูอารบิกซึ่งจำเป็นจะต้องไขมันออกมาเป็นตัวเลขโรมันและบอกอย่างถูกต้องจึงจะสามารถเข้าถึงห้องสมบัติได้
ตัวอักษรเลขโรมันจะมี I = 1 , V = 5 , X = 10 , L = 50 , C = 100 , D = 500 , M = 1000

รูปเเบบ Input
จำนวนเต็ม

รูปเเบบ Output
ตัวเลขโรมัน เช่น XIX , CVIII , MMCLVII

ข้อจำกัด
ตั้งแต่ 1 - 4,000

ตัวอย่างที่1
Input:
345

Output:
CCCXLV

ตัวอย่างที่2
Input:
2640

Output:
MMDCXL

ตัวอย่างที่3
Input:
865

Output:
DCCCLXV
'''

num = int(input())
list_roman = ["I", "V", "X", "L", "C", "D", "M"]
list_num = [int(i) for i in str(num)][::-1]
result = ""
count = [i for i in range(len(list_num)+1)]
for i, j, k in zip(list_num, list_roman[::2], count):
  if i == 1:
    result = j + result
  elif i == 2:
    result = j*2 + result
  elif i == 3:
    result = j*3 + result
  elif i == 4:
    result = j + list_roman[(k*2)+1] + result
  elif i == 5:
    result = list_roman[(k*2)+1] + result
  elif i == 6:
    result = list_roman[(k*2)+1] + j + result
  elif i == 7:
    result = list_roman[(k*2)+1] + j*2 +result
  elif i == 8:
    result = list_roman[(k*2)+1] + j*3 + result
  elif i == 9:
    result = j + list_roman[(k*2)+2] + result
    
print(result)

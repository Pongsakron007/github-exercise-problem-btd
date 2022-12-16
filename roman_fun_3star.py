'''
คำอธิบาย
ให้แปลงเลข Roman เป็นจำนวนเต็ม(เลขฐาน 10)
I       1
V      5
X      10
L       50
C      100
D      500
M     1000

รูปเเบบ Input
รับค่าเป็น String (เลขโรมัน)

รูปเเบบ Output
ออกมาเป็นจำนวนเต็ม

ตัวอย่างที่1
Input:
III

Output:
3

ตัวอย่างที่2
Input:
LVIII

Output:
50

ตัวอย่างที่3
Input:
MCMXCIV

Output:
1994
'''

roman = input()
dic_ro = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M": 1000}

roman = [i for i in roman][::-1]

result = 0
for idx, i in enumerate(roman):
  #print(dic_ro[i])
  if idx == 0:
    result += dic_ro[i]
  elif idx > 0 and idx < len(roman)-  1:
    if dic_ro[i] >= dic_ro[roman[idx-1]]:
      result += dic_ro[i]
    else:
      result -= dic_ro[i]
  elif idx == len(roman) - 1:
    result+= dic_ro[i]
    
print(result)

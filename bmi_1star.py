'''
คำอธิบาย
ให้เขียนโปรแกรมคำนวณค่า BMI (Body Mass Index) ของผู้ใช้งาน โดยโปรแกรมจะรับค่าน้ำหนัก (kg) และส่วนสูง (m) จากผู้ใช้งาน แล้วคำนวณหาค่า BMI โดยใช้สูตร BMI = น้ำหนัก (kg) / (ส่วนสูง (m))^2 และแสดงผลค่า BMI พร้อมกับคำแนะนำสุขภาพของผู้ใช้งานตามตารางดังนี้
น้อยกว่า 18.5: Underweight
18.5 - 22.9: Normal weight
23 - 24.9: Overweight
25 - 29.9: Obesity class 1
30 - 39.9: Obesity class 2
40 ขึ้นไป: Obesity class 3
รูปเเบบ Input
Number

รูปเเบบ Output
String

ตัวอย่างที่1
Input:
60
1.7

Output:
Normal weight

ตัวอย่างที่2
Input:
70
1.7

Output:
Overweight

ตัวอย่างที่3
Input:
100
1.5

Output:
Obesity class 3
'''
w = int(input())
h = float(input())

def bmi(w, h):
  result = w/h**2
  return result

re = bmi(w, h)
if re < 18.5:
  print("18.5: Underweight")
elif 18.5 <= re < 22.9:
  print("Normal weight")
elif 23 <= re < 24.9:
  print("Overweight")
elif 25 <= re < 29.9:
  print("Obesity class 1")
elif 30 <= re < 39.9:
  print("Obesity class 2")
else:
  print("Obesity class 3")

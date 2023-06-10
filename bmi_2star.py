'''
คำอธิบาย
ค่า BMI เป็นค่าที่ใช้วัดความอ้วน เพื่อประเมินหาไขมันส่วนเกินในร่างกาย เพื่อคํานวณความเสี่ยงในการเป็นโรค
สูตรการคํานวณ คือ
weight/height^2
ซึ่ง weight มีหน่วยเป็น กิโลกรัม (kg) และ height มีหน่วยเป็น เมตร (m)

จงเขียนโปรแกรมหาค่า BMI โดยบอกว่าค่า BMI ที่ได้นั้นเป็นเช่นไรเมื่อเทียบกับเกณฑ์ ดังนี้
- Underweight เมื่อค่า BMI น้อยกว่า 18.5
- Normal weight เมื่อค่า BMI มีค่าตั้งแต่ 18.5 แต่ไม่ถึง 25
- Overweight เมื่อค่า BMI มีค่าตั้งแต่ 25 แต่ไม่ถึง 30
- Obesity เมื่อค่า BMI มีค่าไม่ต่ำกว่า 30

รูปเเบบ Input
บรรทัดแรก รับค่าน้ําหนักในหน่วยกิโลกรัม
บรรทัดที่สอง รับค่าส่วนสูงในหน่วยเมตร

รูปเเบบ Output
บรรทัดแรก แสดงรูปแบบข้อความ “BMI is {ค่าBMI}” โดยผลลัพธ์จะมีทศนิยม 1 ตำแหน่ง
บรรทัดที่สอง แสดงข้อความผลลัพธ์ของค่า BMI ตามเกณฑ์ข้างต้น

ตัวอย่างที่1
Input:
56
1.65

Output:
BMI is 20.6
Normal weight
'''
weight, height = [input() for i in range(2)]

bmi = int(weight)/float(height)**2

if bmi < 18.5:
  print(f"BMI is {bmi:.1f}")
  print("Underweight")
elif bmi < 25:
  print(f"BMI is {bmi:.1f}")
  print("Normal weight") 
elif bmi < 30:
  print(f"BMI is {bmi:.1f}")
  print("Overweight")  
else:
  print(f"BMI is {bmi:.1f}")
  print("Obesity")  

'''
คำอธิบาย
เรื่องมีอยู่ว่าการเขียนข้อแบบปกตินั้นบางครั้งอาจจะทำให้ดูน่าเบื่อไปซะบ้าง งั้นลองมาเปลี่ยนข้อความกันเถอะ

รูปเเบบ Input
เมื่อทำการใส่ข้อความลงไปให้ทำการเปลี่ยนลำดับคี่เป็นตัวพิมพ์เล็กและลำดับคู่เป็นตัวพิมพ์ใหญ่

รูปเเบบ Output
ลำดับของชื่อจะเริ่มด้วยตัวพิมพ์เล็กถัดจะเป็นตัวพิมพ์ใหญ่สลับกันไปเรื่อยๆ

ตัวอย่างที่1
Input:
python

Output:
pYtHoN
'''

text = input()
a=""
for idx, i in enumerate(text):
  if idx%2==0:
    a+=i
  else:
    i = i.upper()
    a+=i    
print(a)

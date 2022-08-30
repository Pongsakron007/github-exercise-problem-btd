'''
คำอธิบาย
จงเขียนโปรแกรมคำนวน คะแนนร้อยละของคะแนนเต็ม 80

รูปเเบบ Input
ป้อนตัวเลข 1 จำนวน คือคะแนนที่ได้

ยกตัวอย่างเช่น คะแนน 30 คิดจาก
คะแนนที่ได้ / 80 * 100

รูปเเบบ Output
30 / 80 * 100 = 37.5%

ตัวอย่างที่1
Input:
30

Output:
คะแนนของคุณ : 30.0 
คิดเป็นร้อยละ : 37.5%
'''
get = float(input())

per = (get/80)*100

print(f"คะแนนของคุณ : {get}")
print(f"คิดเป็นร้อยละ : {per:.1f}%")

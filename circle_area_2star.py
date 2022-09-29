'''
คำอธิบาย
จากครั้งที่แล้ว คุณครูได้สั่งการบ้านว่าให้สร้างโปรแกรมหาเส้นรอบรูปไปครั้งที่แล้ว ครั้งนี้คุณครูได้สั่งการบ้านมาให้หมีพูการบ้านคือหาพื้นที่วงกลม โดยให้ใส่รัศมีของวงกลมและให้แสดงพื้นที่ของวงกลมทางหน้าจอ

รูปเเบบ Input
บรรทัดที่ 1 รับตัวเลขจำนวนเต็ม

รูปเเบบ Output
แสดงพื้นที่ของวงกลม

ตัวอย่างที่1
Input:
5

Output:
78.54

ตัวอย่างที่2
Input:
99

Output:
30790.75

ตัวอย่างที่3
Input:
51

Output:
8171.28
'''

r = int(input())

area = (3.141592653589793)*r**2

print(f"{area:.2f}")

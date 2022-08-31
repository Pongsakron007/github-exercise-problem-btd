'''
คำอธิบาย
โปรแกรมของเราจะต้องรับค่า input มาหนึ่งตัว
และจากนั้นจะต้องเอาตัวเลขจาก1-จำนวนที่ป้อนมา ไปยกกำลังกับ5
แล้วresult ที่จากการยกกำลังมาบวกกัน

INPUT = 5

OUTPUT = 4425 
1^5 + 2^5 + 3^5 + 4^5 + 5^5

INPUT = 3
OUTPUT = 276 
1^5 + 2^5 + 3^5

รูปเเบบ Input
รับinput มาแค่อันเดียว

รูปเเบบ Output
แสดงผลบวกทั้งหมด

ตัวอย่างที่1
Input:
5

Output:
4425
'''
print(sum(i**5 for i in range(int(input())+1)))

'''
คำอธิบาย
จงเขียนโปรแกรมที่รับจำนวนเต็มจากผู้ใช้มาทั้งหมด 3 ตัว จากนั้นโปรแกรมจะพิมพ์จำานวนทั้งสาม ออกมาโดยเรียงจากค่าน้อยไปหามาก (ลุยโลดด)

รูปเเบบ Input

รูปเเบบ Output

ตัวอย่างที่1
Input:
9 8 7

Output:
7 8 9

ตัวอย่างที่2
Input:
7 7 6

Output:
6 7 7

ตัวอย่างที่3
Input:
9 7 8

Output:
7 8 9
'''
num = " ".join(sorted(input().strip(" ").split(" ")))
print(num)

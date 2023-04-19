'''
คำอธิบาย
รับค่า A และ B
โดยให้ A ยกกำลัง B

รูปเเบบ Input
รับค่าตัวแปร A
รับค่าตัวแปร B

รูปเเบบ Output
ผลลัพธ์ของการยกกำลัง

ตัวอย่างที่1
Input:
2
2

Output:
4

ตัวอย่างที่2
Input:
7
3

Output:
343

ตัวอย่างที่3
Input:
5
0

Output:
1
'''

base, power = [int(input()) for i in range(2)]
result = base**power
print(result)

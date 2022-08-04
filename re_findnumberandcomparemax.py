'''
คำอธิบาย
ง่ายๆ ให้ใช้ operator == ในการเปรียบค่ามากกว่าหรือน้อยกว่า

รูปเเบบ Input
รับinputเป็นstring

รูปเเบบ Output
แสดงออกมาเป็นตัวเลขที่มากกว่า


ตัวอย่างที่1
Input:
2==3

Output:
3
'''
import re

get = input()
get2 = re.findall("[0-9]+",get)
get2_int = list(map(int, get2))
print(max(get2_int))

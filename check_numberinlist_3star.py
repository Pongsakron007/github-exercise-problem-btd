'''
คำอธิบาย
จงเขียนโปรแกรม ค้นหาตัวเลขโดยกำหนดชุดข้อมูลตัวเลขดังนี้
9 11 16 19 20 21 22 29 31 39 40 90 95
หากค้นหาแล้ว ไม่มีข้อมูล ในชุดตัวเลขข้างต้นให้แสดงข้อความ Not Found 
หากค้นหาแล้ว มีข้อมูล ในชุดข้อมูลข้างต้นให้แสดงข้อความ Found
รูปเเบบ Input
20

รูปเเบบ Output
มีข้อมูล

ตัวอย่างที่1
Input:
95

Output:
Found
'''
list_a = [9, 11, 16, 19, 20, 21, 22, 29, 31, 39, 40, 90, 95]
[print("Found") if int(input()) in list_a else print("Not Found")]

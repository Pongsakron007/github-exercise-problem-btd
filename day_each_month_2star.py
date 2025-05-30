'''
คำอธิบาย
เดือน มกราคม,มีนาคม,พฤษภาคม,กรกฎาคม,สิงหาคม,ตุลาคม,ธันวาคม
มี 31 วัน

เดือน เมษายน,มิถุนายน,กันยายน,พฤศจิกายน
มี 30 วัน

เดือน กุมภาพันธ์
มี 28-29 วัน

รูปเเบบ Input
เลขของเดือน เช่น มกราคม = 1 ,กุมภาพันธ์ = 2 ฯลฯ

รูปแบบ Output
เดือนนั่นมีกี่วัน

ข้อจำกัด
1 <= n <= 12

ตัวอย่างที่ 1
ข้อมูลขาเข้า
1

ผลลัพธ์
31

ตัวอย่างที่ 2
ข้อมูลขาเข้า

2

ผลลัพธ์
28-29

ตัวอย่างที่ 3
ข้อมูลขาเข้า
4

ผลลัพธ์
30
'''
map_month_day = {1:"31", 2:"28-29", 3:"31", 4:"30", 5:"31", 6:"30",
                7:"31", 8:"31", 9:"30", 10:"30", 11:"30", 12:"31"}

num = int(input())

print(map_month_day.get(num, "num not in 1 - 12"))



'''
คำอธิบาย
น้องใหม่อยากรู้ว่าในช่วง 0 จนถึง n มีจำนวนเฉพาะอยู่กี่ตัวกันนะ
โดยที่ n คือจำนวนเต็มบวกใด ๆ

รูปเเบบ Input
รับค่าจำนวนเต็มบวก 1 จำนวน เช่น

12

รูปเเบบ Output
แสดง output ในรูปแบบข้อความดังนี้
จำนวนเฉพาะในช่วง 0 ถึง 12

มีอยู่ 5 จำนวน

ถ้าจำนวนที่รับมามีค่าน้อยกว่าหรือเท่ากับ 0 ให้แสดง output ว่า
ไม่สามารถหาได้
'''

get = int(input())

def prime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

count = 0
for i in range(2,get+1):
    if prime(i) == True:
        count +=1

print(f"จำนวนเฉพาะในช่วง 0 ถึง {get}")
print(f"มีอยู่ {count} จำนวน")


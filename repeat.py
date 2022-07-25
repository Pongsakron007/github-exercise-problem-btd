'''
คำอธิบาย
ให้ทำการสร้างพีรมิดจากข้อความที่ได้รับตามตัวอย่าง

รูปแบบ input
ข้อความสั้นๆ 1 ข้อความ

รูปแบบ output
พีระมิดที่สร้างจากข้อความ

ข้อจำกัด
ความยาวของข้อความไม่เกิน 20 ตัวอักษรและไม่มีเว้นวรรค


input: Python

output:
          P
        y P y
      t y P y t
    h t y P y t h
  o h t y P y t h o
n o h t y P y t h o n

'''
first = input()
a = first[1:][::-1]

last = a + first
#print(last_in)
for row in range(1,len(first)+1):
    for column in range(0,len(last)+1):
        if column < len(first)-row:
            print(" ",end="")
    g = last[len(first)-row:len(first)+row-1]
    for char in g:
        print(char,end="")
    print("")

            

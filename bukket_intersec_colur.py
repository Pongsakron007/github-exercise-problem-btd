'''
รูปเเบบ Input:
ถังที่ หนึ่ง สอง สาม มีลูกบอลสีอะไรอยู่บ้าง

รูปเเบบ Output:
สีของลูกบอลที่มีอยู่ในถังที่หนึ่งและสอง แต่ไม่มีอยู่ในถังที่สาม (กรณีที่ไม่มีลูกบอลสีใดเลยที่ตรงตามเงื่อนไข ให้ผลลัพธ์ออกเป็น none)

Input:
b1=[red,green,blue] b2=[black,green,white] b3=[blue]

Output:
green
'''
get_input = input().split()
#print(get_input)
a1 = []
b1 = []
c1 =[]

for i,value in enumerate(get_input):
    if i == 0:       
        d = value[4:-1]
        #print(d)
        d = d.split(",")
        a1 += d
    elif i == 1:       
        d = value[4:-1]
        d = d.split(",")
        b1 += d
    elif i == 2:
        d = value[4:-1]
        d = d.split(",")
        c1 += d
a1 = set(a1)
b1 = set(b1)
c1 = set(c1)

r1 = b1.intersection(a1)
r2 = r1.difference(c1)
#print(r1)
#print(r2)
#print(r2.issubset(c1))

if len(r2) == 0:
    print("none")   
elif len(r2) >= 1:   
    m1 =""
    for i in r2:
        m1 += ","+i
    m1 = m1.lstrip(",")
    print(m1)



'''
คำอธิบาย
ให้สลับเลขระหว่างหลักสิบกกับหลักหน่วยแล้วนำมาบวกกัน

รูปเเบบ Input
36
+
25

รูปเเบบ Output
63 + 52 = 115

ข้อจำกัด
9>n <=99และ 9>m<=99

'''

myInput = [input() for i in range(3)]
myInput = [myInput[0], myInput[2]]
t=[]
for i in myInput:
	j = int(i[::-1])
	t.append(j)
t = list(map(int, t))
total = sum(t)

print(f"{t[0]} + {t[1]} = {total}")

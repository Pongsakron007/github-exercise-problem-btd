'''
คำอธิบาย
หลังจากนายเซฟประสบปัญหาค่าไฟ เขาจึงย้ายไปอยู่ต่างประเทศ แล้วบังเอิญพบสาวข้างบ้านหน้าตาน่ารัก นายเซฟจึงตกหลุมรัก อยากจะส่งจดหมายไปหาเขา แต่ถ้าหากส่งจดหมายเป็นภาษาอังกฤษ ซึ่งหากแม่ของนายเซฟจับได้ก็จะดุด่าเอา นายเซฟจึงต้องหาวิธีทำโค้ดลับเพื่อที่จะไม่ให้แม่จับได้ โดยนายเซฟได้เปลี่ยนจาก A-Z เป็นเลข 1-26 ดังนี้
A=1 B=2 C=3 D=4 E=5 F=6 G=7 H=8 I=9 J=10 K=11 L=12 M=13 N=14 O=15 P=16 Q=17 R=18 S=19 T=20 U=21 V=22 W=23 X=24 Y=25 Z=26
นายเซฟจะบอกรักสาวข้างบ้านได้หรือไม่ โปรดติดตามตอนต่อไป ...

รูปเเบบ Input
คำภาษาอังกฤษ ที่นายเซฟอยากจะบอกรักสาวข้างบ้าน

รูปเเบบ Output
code ลับที่นายเซฟกำหนด

ข้อจำกัด
input จะมาเป็นตัวพิมพ์เล็กทั้งหมด
ตัวอักษรในประโยคจะเรียงชิดติดกัน และไม่มีจุด

ตัวอย่างที่1
Input:
iloveyou

Output:
91215225251521

ตัวอย่างที่2
Input:
letter

Output:
1252020518

ตัวอย่างที่3
Input:
riw

Output:
18923
'''
dict_code = {"a":1, "b":2,"c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9,
             "j":10, "k":11, "l":12, "m":13, "n":14, "o":15,
             "p":16, "q":17, "r":18, "s":19, "t":20, "u":21, "v":22,
             "w":23, "x":24, "y":25, "z":26}

code = input()
[print(dict_code[i], end ="") for i in code]  
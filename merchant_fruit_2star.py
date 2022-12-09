'''
คำอธิบาย
แม่ค้าขายผลไม้ ณ ย่านอารีย์ เห็นว่าคุณมีฝีมือในการเขียนโปรแกรมค่อนข้างมาก จึงอยากวานให้คุณเขียนโปรแกรมหาจำนวนชนิดของผลไม้ในตระกร้าที่ลูกค้าประจำแต่ละคนซื้อ และ หาว่าลูกค้าคนไหนซื้อผลไม้ต่างชนิดกันมากที่สุด เพื่อนำไปทำสถิติบางอย่าง

รูปเเบบ Input
ผลไม้ทั้งหมดที่มีอยู่ในตระกร้าของนาย A, B และ C

รูปเเบบ Output
ใครซื้อผลไม้ต่างชนิดกันมากที่สุด

ข้อจำกัด
ไม่นับผลไม้ชนิดเดียวกันซ้ำ

ตัวอย่างที่1
Input:
A: apple orange grape orange B: mango mango grape C: banana banana

Output:
A

ตัวอย่างที่2
Input:
A: papaya apple B: watermelon coconut coconut C: pineapple strawberry strawberry avocado   

Output:
C

ตัวอย่างที่3
Input:
A: cherry B: guava melon pear C: guava kiwi

Output:
B
'''
fruit = input()

fruit = fruit.split(":")

a = fruit[1][0:-1].split()
b = fruit[2][0:-1].split()
c = fruit[3].split()

a= set(a); A = list(a)
b = set(b); B = list(b) 
c = set(c); C= list(c)

total = {"A":len(A), "B":len(B), "C":len(C)}

result = max(total, key=total.get)

print(result)

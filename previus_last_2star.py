'''
คำอธิบาย
มีคะเเนนสอบ ของ นักเรียน 10 คน ให้ หาว่าคะเเนน น้อยรองสุดท้ายคือเท่าไหร่

รูปเเบบ Input
รับคะเเนนของนักเรียน 10 คน

รูปเเบบ Output
ให้เเสดงคะเเนนน้อยรอง คะเเนนน้อยสุด

ข้อจำกัด
ข้อมูลที่ Input จะมีค่าตั้งแต่ 0 - 1,000,000

ตัวอย่างที่1
Input:
10,20,30,45,12,45,24,77,55,80

Output:
12
'''
print(sorted(list(map(int, input().split(","))))[1])
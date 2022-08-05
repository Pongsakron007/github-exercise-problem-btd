'''
คำอธิบาย
สะท้อนข้อความดังกล่าว

รูปเเบบ Input
คำเดียว

รูปเเบบ Output
วัตถุ+ภาพสะท้อน

ข้อจำกัด
ข้อความมีตัวอักษรอย่างน้อย 1 ตัว

Input: ant

Output: antna

'''

string = input()
string2  = string[0:len(string)-1][::-1]

string3 = string+string2

print(string3)

'''
คำอธิบาย
จงเขียนโปรแกรมเพื่อแปลง list เป็น array แล้วเรียงจากมากไปน้อย

รูปเเบบ Input
รับ list สมาชิกไม่เกิน 10 ตัว (สมาชิกแต่ละตัวมีค่าไม่เกิน 5 หลัก)

รูปเเบบ Output
มีบรรทัดเดียว ข้อมูลใน array เรียงจากมากไปน้อย

ข้อจำกัด
ข้อมูลที่ Input จะมีค่าตั้งแต่ -9999 - 99999 และจำนวนของข้อมูลใน list ไม่เกิน 10 ตัว

ตัวอย่างที่1
Input:
[230,450,-270,180,860,100]

Output:
860 450 230 180 100 -270

ตัวอย่างที่2
Input:
[1,2,3,3,4,5]

Output:
5 4 3 3 2 1

ตัวอย่างที่3
Input:
[-9999,999,9999,99,99999,9]

Output:
99999 9999 999 99 9 -9999
'''
input_btd = input()
input_btd = input_btd.rstrip("]")
input_btd = input_btd.lstrip("[")
input_btd = input_btd.split(",")

int_in = list(map(int, input_btd))
result_list = sorted(int_in)[::-1]
result_list = list(map(str, result_list))
result = " ".join(result_list)

print(result)

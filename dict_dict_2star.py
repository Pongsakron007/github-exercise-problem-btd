'''
คำอธิบาย
จงเขียนฟังก์ชันชื่อ duplicate_id เพื่อตรวจสอบ list ของรหัสนักศึกษาที่รับมาเป็น input ว่ามีค่าซ้ำปรากฎอยู่ใน list หรือไม่
โดยฟังก์ชันต้องคืนค่า True เมื่อมีค่าซ้ำปรากฎใน list และคืนค่า False เมื่อไม่มีค่าซ้ำปรากฎ 
ทั้งนี้ต้องใช้ dictionary ในการ check ค่าซ้ำ และห้ามใช้ build-in function ใดๆ

รูปเเบบ Input
id_list = [650109090001, 650109090002, 650109090003, 650109090004, 650109090005]
id_list = [650109090001, 650109090002, 650109090001, 650109090004, 650109090005]


รูปเเบบ Output
False
True

ข้อจำกัด
ต้องใช้ dictionary ในการ check ค่าซ้ำ และห้ามใช้ build-in function ใดๆ

ตัวอย่างที่1
Input:
[650109090001, 650109090002, 650109090003, 650109090004, 650109090005]

Output:
False

ตัวอย่างที่2
Input:
[650109090001, 650109090002, 650109090001, 650109090004, 650109090005]

Output:
True
'''
list_id = input()
list_id = list_id.rstrip("]")
list_id = list_id.lstrip("[")
list_id = list_id.split(",")
list_id = list(map(int, list_id))


def check_dup(list_id):
  list_get = []
  for i in list_id:
    if i in list_get:
      return True
    elif i not in list_get:
      list_get.append(i)
  return False


print(check_dup(list_id))

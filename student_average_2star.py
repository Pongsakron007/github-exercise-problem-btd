'''
คำอธิบาย
ให้รับค่านักศึกษาทั้งหมด(n) และก็รับข้อมูล n บรรทัดโดยในแต่ละบรรทัดจะประกอบไปด้วยรหัสนักศึกษาตามด้วย space ตามด้วยคะแนนนักศึกษา ให้checkว่าคะแนนนักศึกษาคนใดที่มีคะแนนมากกว่าหรือเท่ากับค่าเฉลี่ย ให้ output รหัสนักศึกษาออกมาโดยเรียงจากน้อยไปมาก แต่ถ้าคะแนน > 100 ให้ output ว่า "Error"

รูปเเบบ Input
บรรทัดที่ 1 รับค่านักศึกษาทั้งหมด(n)
บรรทัดที่ n รับค่ารหัสนักศึกษา คะแนนนักศึกษา (คั่นด้วย space)

รูปเเบบ Output
n บรรทัด แต่ละบรรทัดแสดงรหัสนักศึกษาที่เข้าเงื่อนไขข้างบนโดยเรียงจากน้อยไปมาก
ถ้า คะแนน > 100 ให้ output ว่า "Error"

ข้อจำกัด
n > 0 , คะแนน <= 100

ตัวอย่างที่1
Input:
3
65070160 96.5
65070168 56.2
65070164 46.8

Output:
65070160

ตัวอย่างที่2
Input:
5
65070154 99.1
65070684 62
65070912 85.4
65070166 37.9
65070184 55.3

Output:
65070154
65070912

ตัวอย่างที่3
Input:
2
65070149 100.1
65070881 65.8

Output:
Error
'''
num = int(input())
student = [input() for i in range(num)]

st_p = {}
for i in student:
  id_s, point = i.split(" ")
  st_p[id_s] = float(point)
  
avg = sum([i for i in st_p.values()])/num
st_p = dict(sorted(st_p.items(), key = lambda item: item[1]))

result_list = []
for i,j in st_p.items():
  if j >= avg:
    result_list.append(i)

def check_lower_100():
  for i in st_p.values():
    if i > 100:
      return True
  return False

result_list = sorted(result_list)

for i in result_list:
  if check_lower_100():
    print("Error")
  else:
    print(i)

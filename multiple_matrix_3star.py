'''
คำอธิบาย
ให้ทำการคูณเมทริกซ์ 2 เมทริกซ์ มิติ m × n ตามที่โจทย์ระบุให้

รูปเเบบ Input
บรรทัดที่ 1 รับจำนวนเต็มบวก 2 จำนวน แสดงมิติของเมทริกซ์ A
บรรทัดที่ 2 รับจำนวนเต็มบวก 2 จำนวน แสดงมิติของเมทริกซ์ B
บรรทัดที่ 3 ถึง mA+2 รับจำนวนเต็มบวก nA จำนวนในแต่ละบรรทัด
บรรทัดที่ mA+3 ถึง mA+(mB+2) รับจำนวนเต็มบวก nB จำนวนในแต่ละบรรทัด

รูปเเบบ Output
แต่ละบรรทัดแสดงสมาชิกของเมทริกซ์ผลลัพธ์ AB
ถ้าเมทริกซ์ทั้ง 2 ไม่สามารถคูณกันได้ให้แสดง output เป็น "Cant calculate !"
ข้อจำกัด

ตัวอย่างที่1
Input:
3 3
3 2
1 3 4
3 2 2
1 2 3
1 2
3 4
5 6

Output:
[30 38]
[19 26]
[22 28]

ตัวอย่างที่2
Input:
2 2
2 3
1 2
3 4
5 6 7
8 9 10

Output:
[21 24 27]
[47 54 61]

ตัวอย่างที่3
Input:
4 4
3 3
1 1 1 1
2 2 2 2
3 3 3 3
4 4 4 4
5 5 5
6 6 6
7 7 7

Output:
Cant calculate !
'''
dimentions_a = input()
dimentions_b = input()

row_a = int(dimentions_a.split(" ")[0])
row_b = int(dimentions_b.split(" ")[0])

matrix_a = []
for i in range(row_a):
  ele = input()
  ele = [int(item) for item in ele.split(" ")]
  matrix_a.append(ele)
  
matrix_b = []
for j in range(row_a):
  ele2 = input()
  ele2 = [int(item2) for item2 in ele2.split(" ")]
  matrix_b.append(ele2)

dimention_a = len(matrix_a[0]) 
dimention_b = len(matrix_b[0])
  
def cal_matrix():
  result = []
  for row in matrix_a:
    for column_b in range(dimention_b) : 
      for idx, ele in enumerate(row):
        re_each = ele * matrix_b[idx][column_b]
        result.append(re_each)
  
  result_sum = []
  round_sum = len(result[::dimention_a])
  for i in range(round_sum):
    sum_ele = sum(result[i*dimention_a:i*dimention_a+dimention_a])
    result_sum.append(sum_ele)
    
  last_re = []
  for i in range(dimention_a):
    sub_list = result_sum[i*dimention_b:(i*dimention_b)+dimention_b]
    last_re.append(sub_list)

  for i in last_re:
    i_new = [str(item) for item in i]
    print("[" + " ".join(i_new) + "]")

if int(dimentions_a.split(" ")[1]) == int(dimentions_b.split(" ")[0]):
  cal_matrix()
else:
  print("Cant calculate !")

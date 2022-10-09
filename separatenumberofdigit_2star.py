'''
คำอธิบาย
จงแยกหลักของตัวเลขที่ป้อนเข้ามาให้เป็น หลักหน่วย, หลักสิบ, หลักร้อย, หลักพัน หรือ หลักที่มากกว่านั้น

รูปเเบบ Input
บรรทัดเดียว: รับค่าตัวเลขจำนวนเต็มบวก

input :
1234

รูปเเบบ Output
แสดงผลเป็นจำนวนเต็ม โดยให้เรียงจากหลักที่มากที่สุดลงมาถึงหลักที่น้อยที่สุด

output :
1000
200
30
4

ข้อจำกัด
input ที่ป้อน มีค่าตั้งแต่ 0-1,000,000 หากค่าเกินกว่านั้นให้แสดง 'OVER' หรือ ค่าต่ำกว่านั้นให้แสดง 'UNDER' ถ้าหากป้อนข้อมูลเป็นชนิดอื่นให้แสดง 'Invalid'

ตัวอย่างที่1
Input:
1234567

Output:
OVER

ตัวอย่างที่2
Input:
abc

Output:
Invalid

ตัวอย่างที่3
Input:
12034

Output:
10000
2000
0
30
4
'''
try:
  get = int(input())
  if get > 1000000:
    print("OVER")
  elif get < 0:
    print("UNDER")
  else:
    get_str = str(get)
    digit = len(get_str)
    list_re = []
    while digit >0:
      a = get%(10**(digit))
      b = get%(10**(digit-1))
      c = a - b
      list_re.append(c)
      digit -= 1
    for i in list_re:
      print(i)
except:
  print("Invalid")



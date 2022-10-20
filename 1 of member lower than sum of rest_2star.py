'''
คำอธิบาย
คล้ายการตรวจสอบว่าเป็นสามเหลี่ยมไหม แต่มีสมาชิกlist n ตัว

เช่น
input: [2,3,4,5]

output: true

นั้นคือ
2<3+4+5
3<2+4+5
4<2+3+5
5<2+3+4
(ต้องเป็นจริงทุกกรณี)

รูปเเบบ Input
รับข้อมูลlist เป็นstring

รูปเเบบ Output
true
false

ข้อจำกัด
ความยาวของstring < 100
จำนวนสมาชิกในlist < 20
0 < ค่าสมาชิกในlist < 500

ตัวอย่างที่1
Input:
[5,4,50]

Output:
false

ตัวอย่างที่2
Input:
[1,1,2,1]

Output:
true
'''
get = input()
get = get.rstrip("]")
get = get.lstrip("[")
get = get.split(",")
get = [int(i) for i in get]

def check(get):
  for idx,i in enumerate(get):
    num = get.pop(idx)
    if num < sum(get):
      get.insert(0,num)
      continue
    else:
      return False
  return True

if __name__ == "__main__":
  [print("true") if check(get) else print("false")]

'''
คำอธิบาย
การเปลี่ยนคำเอกพจน์ เป็นพหูพจน์ ในภาษาอังกฤษนั้น มีกฏอยู่
1.คำนามเอกพจน์ที่ลงท้ายด้วย s, x, z, sh, ch ให้เติม es
Ex. bus -> buses

2.คำนามเอกพจน์ที่ลงท้ายด้วย y และด้านหน้า y เป็นพยัญชนะ (ที่ไม่ใช่ a, e, i, o, u เพราะว่าเป็นตัวสระ) ให้ตัด y แล้วเติม ies
Ex. baby -> babies

3.หากไม่ตรงตามที่กล่าวมา เติม s ได้เลย
Ex.boat -> boats

ในโจทย์จะยกแค่ 3 ข้อนี้
รูปเเบบ Input
คำนามเอกพจน์

รูปเเบบ Output
คำนามเอกพจน์ -> คำนามพหูพจน์

ตัวอย่างที่1
Input:
bus

Output:
bus -> buses

ตัวอย่างที่2
Input:
baby

Output:
baby -> babies

ตัวอย่างที่3
Input:
boat

Output:

boat -> boats
'''

get = input()

s = ["a", "e", "i", "o", "u"]
last = ["s", "x", "z", "sh", "ch"]

result = ""
if get[-1] in last:
  result = get + "es"
elif get[-2:] in last:
  result = get + "es"
elif get[-1] == "y" and get[-2] not in s:
  result = get.replace("y", "ies")
else:
  result = get + "s"

  
print(f"{get} -> {result}")

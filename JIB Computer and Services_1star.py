'''
คำอธิบาย
เมื่อวันหนึ่งคุณได้เข้าไปทำงานที่ JIB เป็นแคชเชียร์คอยคิดเงินให้กับลูกค้าที่เข้ามาซื้อของ เช่นซื้อ การ์ดจอ เมนบอร์ด ฯลฯ และหัวหน้าคุณสั่งให้เก็บรวบรวมข้อมูลการเงินโดยการเขียนไว้ ถ้ามีคนมาซื้อของ 2500บาท ให้เขียน 2500 แล้วต่อไปเรื่อยๆ และหัวหน้าจะให้คิดสรุปการเงินของวันนั้นว่าวันนั้นมีคนซื้อไปทั้งหมดกี่บาท (Sum) หรือ เรียงลำดับว่าคนซื้อสูงสุดราคาเท่าไหร่ลงไปน้อยสุด (Max) หรือเรียงลำดับว่าคนซื้อน้อยสุดราคาเท่าไหร่ขึ้นไปมาก (Min) ซึ่งคุณจะไม่ทำตามที่หัวหน้าสั่งแน่นอน !!! เพราะเป็นโปรแกรมเมอร์สุดเก่ง ที่สุดในร้านนั้นก็ว่าได้ คุณเลยคิดว่าจะต้องเขียนโปรแกรมออกมายังไงก็ได้ตามที่หัวหน้าต้องการ ;-;

รูปเเบบ Input
บรรทัดแรกใส่จำนวนเต็ม N; 1 <= N <= 10000 แทนจำนวนราคา
N บรรทัดต่อมา ใส่ข้อมูลเป็นจำนวนเต็ม N; 1 <= N <= 10000 และไม่ซ้ำกัน แทนรหัสข้อมูล
ใส่ 0 หากข้อมูลครบแล้ว และหลังจากใส่ 0 พิมพ์คำสั่ง เรียงจากมากไปน้อย (Max) , เรียงจากน้อยไปมาก (Min) , หาค่าผลรวมของตัวเลขที่พิมพ์ (Sum) หรือถ้าใส่คำสั่งไม่ถูกจะแสดง 0

รูปเเบบ Output
แสดงค่าที่ได้มาตามคำสั่ง เรียงจากมากไปน้อย (Max) , เรียงจากน้อยไปมาก (Min) , หาค่าผลรวมของตัวเลขที่พิมพ์ (Sum) หรือถ้าใส่คำสั่งไม่ถูกจะแสดง 0

ข้อจำกัด
1 <= N <= 10000 

ตัวอย่างที่1
Input:
6
1
4
9
0
Max

Output:
9 6 4 1

ตัวอย่างที่2
Input:
6
1
4
7
0
Sum

Output:
18

ตัวอย่างที่3
Input:
6
1
4
7
0
Summssmax

Output:
0
'''

store_v = []
order = ""

while True:
  v = input()
  if v.isdigit():
    store_v.append(v)
  else:
    order = v
    break


store_v = list(map(int, store_v))
store_v.remove(0)  if 0 in store_v else store_v

total_order = {"Max": sorted(store_v, reverse = True), "Min": sorted(store_v), "Sum": sum(store_v)}

result = total_order.get(order, 0)

result = " ".join([str(i) for i in result]) if isinstance(result, list) else result
print(result)
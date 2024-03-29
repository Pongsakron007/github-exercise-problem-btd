'''
คำอธิบาย
ระดับความยาก 1 ดาว
พลเมืองประเทศหนึ่งต้องการประกาศอิสรภาพจากการโดน DEVLAB ครอบงำ จึงได้รวบรวมแรงงานมาสร้างสัญลักษณ์เป็นพีระมิดยอดตัดฐานสี่เหลี่ยมจัตุรัสที่ฐานด้านล่างมีความยาวด้าน a หน่วย ฐานด้านบนมีความยาวด้าน b หน่วย (a>b) และมีความสูง h หน่วย
แรงงานเหล่านี้ต้องใช้ทรายจากทะเลทราย ขนมายังสถานที่ก่อสร้างเป็นระยะทาง 2566 กิโลเมตร ทั้งนี้ แรงงานของประเทศนี้ไม่อยากขนทรายหลายรอบ เลยขนรอบเดียวเลย (แข็งแกร่ง) แต่ต้องขนมาโดยที่ปริมาตรพอดีกับขนาดที่จะสร้าง
งานของคุณ จงเขียนโปรแกรมคำนวณปริมาตรของพีระมิดยอดตัด

รูปเเบบ Input
มีบรรทัดเดียว รับจำนวนเต็ม a,b,h แทน ความยาวด้านฐานล่าง ความยาวด้านฐานบน และความสูง ตามลำดับ

รูปเเบบ Output
มีบรรทัดเดียว แสดงผลเป็นทศนิยม 6 ตำแหน่ง เป็นปริมาตรของพีระมิดยอดตัด

ข้อจำกัด
2<=a,b,h<=10^3 และ a>b

ความรู้เพิ่มเติม
พีระมิดยอดตัดที่มีความยาวด้าน a หน่วย ฐานด้านบนมีความยาวด้าน b หน่วย (a>b) และมีความสูง h หน่วย เกิดจาก
พีระมิดที่มีฐานความยาวด้าน a หน่วย สูง x หน่วย (ยังไม่ทราบค่า) และต้องการตัดยอดให้ฐานด้านบนมีความยาว b หน่วย และสูง h หน่วย จะสามารถใช้สามเหลี่ยมคล้ายในการหาค่า x ได้

จากรูปจะใช้สามเหลี่ยมคล้ายในการหาค่า x
และปริมาตรพีระมิดยอดตัด = ปริมาตรพีระมิดเต็ม - ปริมาตรพีระมิดฐานบน
และนั่นคือปริมาตรของพีระมิดยอดตัด

ตัวอย่างที่1
Input:
3 2 4

Output:
25.333333

ตัวอย่างที่2
Input:
4 3 2

Output:
24.666667

ตัวอย่างที่3
Input:
5 2 5

Output:
65.000000
'''
a, b, h = [int(i) for i in input().split()]

def cal(a, b, h):
  result = (a**2 + a*b + b**2) * (h/3)
  print(f"{result:.6f}")

cal(a, b, h)

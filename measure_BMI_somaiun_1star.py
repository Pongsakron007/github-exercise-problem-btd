'''
คำอธิบาย
-- เนื้อเรื่อง (สาระสำคัญอยู่ด้านล่าง) --
ในช่วงโรคระบาดทำให้ลุงสมหมายขายของได้ไม่ดี ช่วงไม่มีลูกค้าเขาก็กินมากขึ้น
และขี้เกียจออกกำลังกาย เด็กหญิงสมจริง ลูกสาวลุงสมหมายจึงให้ลุงสมหมาย
วัดค่า BMI ทุกๆเดือน ในฐานะนักพัฒนาโปรแกรมของเราจึงได้เข้าไปเสนอตัว
ในการรับพัฒนาโปรแกรมวัดค่า BMI ให้ลุงสมหมาย

-- คำอธิบาย --
ให้ทำเครื่องคำนวณค่า BMI ให้ลุงสมหมาย
Body Mass Index - BMI
BMI หมายถึง การประเมินเรื่องความสมดุลของน้ำหนักตัวต่อส่วนสูง
โดยคำนวณเป็นทศนิยม 2 ตำแหน่งและคำนวณด้วยสูตรการคำนวณดังนี้
น้ำหนักตัว [กิโลกรัม] หารด้วย ส่วนสูง [เมตร] ยกกำลังสอง

รูปเเบบ Input
ให้รับ Input 2 ตัวแปรดังนี้
ค่าน้ำหนัก ในหน่วยกิโลกรัม
ค่าส่วนสูง ในหน่วยเซนติเมตร

รูปเเบบ Output
ให้แสดงข้อความค่า BMI โดยประมาณเป็นตัวเลขทศนิยม 2 ตำแหน่ง

ตัวอย่างที่1
Input:
63
173

Output:
BMI: 21.05

ตัวอย่างที่2
Input:
52
162

Output:
BMI: 19.81

ตัวอย่างที่3
Input:
50
170

Output:
BMI: 17.3
'''

weight = int(input())
height = int(input())/100

result = round(weight/height**2, 2)
print(f"BMI: {result}")
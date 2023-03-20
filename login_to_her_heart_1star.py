'''
คำอธิบาย
คุณตกหลุมรักกับโปรแกรมเมอร์สาว(หรือชาย)คนหนึ่ง วันหนึ่งเธออยากจะเก็บข้อมูลส่วนตัวของเธอแต่วันนั้นดันรู้สึกขี้เกียจ เธอจึงขอให้คุณเขียนโค้ดให้เธอหน่อย เธออธิบายว่า "ไม่ยากหรอกหน่า แค่ทำระบบ login ที่ต้องใส่ Username และ Password เอง ถ้าอย่างใดอย่างนึงผิดก็ไม่ให้เข้า ถ้าถูกทั้งคู่ค่อยให้เข้า จิ๊บๆ ถ้าทำได้เดี๋ยวไปดูหนังกัน" 
﻿เธอยื่นกระดาษใบให้คุณ บนกระดาษเขียนไว้ว่า "Username : 5572417765736F6D65 Password : 494C6F766555 #สู้ๆ!~"
ด้วยความ S I M P ของคุณ คุณจึงตอบตกลง แล้วสัญญากับตัวเองว่าจะ Login เข้าหัวใจเธอ ให้ได้
tldr : จงทำระบบ Login โดยกำหนดให้ Username เป็น 5572417765736F6D65 และ Password เป็น 494C6F766555

รูปเเบบ Input
รับค่า Username และ Password เป็น "String"

รูปเเบบ Output
หากเข้าสำเร็จ Output : Access Granted
หากเข้าไม่สำเร็จ Output : Access Denied

ข้อจำกัด
(Optional) ยิ่งเขียนโค้ดนี้สั้นเท่าไหร่ ยิ่งทำให้เธอประทับใจมากขึ้น

ตัวอย่างที่1
Input:
5572417765736F6D65
494C6F766555

Output:
Access Granted

ตัวอย่างที่2
Input:
5671328855934E6D12
848C16F55745

Output:
Access Denied

ตัวอย่างที่3
Input:
Pleaseletmeintoyourheart
Idontknowthepasswordbutiminlovewithyou

Output:
Access Denied
'''
u, p = [input() for i in range(2)]
if u == "5572417765736F6D65" and p == "494C6F766555":
  print("Access Granted")
else:
  print("Access Denied")

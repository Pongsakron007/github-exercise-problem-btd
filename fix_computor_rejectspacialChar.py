'''
คำอธิบาย
คอมพิวเตอร์เป็นอะไรไม่รู้อ่ะ เปิดไม่ติดเลยอยากจะให้เขียนโปรแกรมเข้าไปเช็คไวรัสว่ามีชื่อไฟล์ใดบ้าง โดยคอมที่จะให้เข้าไปเช็คไวรัสชื่อ "GUITAR" ถ้าเจอเครื่องอื่นจะไม่ถูก 
ไวรัสจะมีอักศรพิเศษในชื่อแปลกๆเช่น f@i#l$e^%, soft@#%!@ ถ้าปกติจะไม่มีอักษรพิเศษ เช่น file, soft ช่วยลบไฟล์ไวรัสพวกนี้ให้หน่อยนะ ^^

รูปเเบบ Input
ชื่อคอม, ชื่อไฟล์

รูปเเบบ Output
ชื่อไฟล์ที่ไม่มีอักษรพิเศษ

ข้อจำกัด
ต้องเป็นคอมที่ชื่อ GUITAR
ต้องแสดงผลชื่อไฟล์ที่ไม่มีอักษรพิเศษ

ตัวอย่างที่1
Input:
GUITAR:[#$@fsdw, fil@#^!, Me, WERT]
HUITAR:[wert, test, hello_file]
pitch:[ok, dam, wert]

Output:
GUITAR:[Me, WERT]

'''
get_str = [input() for i in range(3)]

List_re =""
for i in get_str:
  if i[0:6] == "GUITAR":
    List_re += i
    
List_re = List_re[8:-1]  
List_start = List_re.split(",")

Str_pass = ""
for i in List_start:
  if "*" not in i:
    if "@" not in i:
      if "#" not in i:
        if "^" not in i :
          if "(" not in i:
            if "'" not in i:
              Str_pass += ","+i
Str_pass = Str_pass.lstrip(",")              

print(f"GUITAR:[{Str_pass}]")

'''
คำอธิบาย
ให้ใส่เลขนาที (เป็นจำนวนเต็ม) เช่น 431 นาที แล้วคิดออกมาเป็นจำนวนชั่วโมง : นาที
เช่น 60 นาทีจะได้ผลลัพธ์เป็น 1:0 (1ชั่วโมง 0 นาที)
หรือ 435 นาทีจะได้ผลลัพธ์เป็น 7:15 (7ชั่วโมง 15 นาที)

รูปเเบบ Input
เลขจำนวนเต็ม (นาที)

รูปเเบบ Output
แสดงค่าชั่วโมง:นาที

ข้อจำกัด
0-30,000

ตัวอย่างที่1
Input:
65

Output:
1:5

ตัวอย่างที่2
Input:
176

Output:
2:56

ตัวอย่างที่3
Input:
317

Output:
3:17
'''
time_m = int(input())

time_h = time_m//60
time_r_m = time_m%60

print(f"{time_h}:{time_r_m}")

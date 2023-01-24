'''
คำอธิบาย
โรงเรียนหนึ่งพานักเรียนไปเข้าค่าย นักเรียนกลุ่มหนึ่งจำนวน N คนแข่งขันกันว่าใครจะหลับเป็นคนสุดท้าย คนที่นอนหลับเป็นคนแรกเป็นผู้แพ้ คนที่นอนหลับเป็นคนสุดท้ายเป็นผู้ชนะ ทุกคนเชื่อว่าถ้านับแกะแล้วจะทำให้หลับได้ช้าลง
ผู้ชนะและผู้แพ้ใช้เวลาในการนับแกะไปคนละกี่ชั่วโมง กี่นาที กี่วินาที และเวลาที่ทุกคนในกลุ่มใช้ในการนับแกะเฉลี่ยกันเท่ากับกี่ชั่วโมง กี่นาที กี่วินาที

รูปเเบบ Input
บรรทัดที่ 1 - รับ ค่า N เป็นจำนวนเต็ม
บรรทัด 2 ถึง N+1 - รับ จำนวนแกะ ที่แต่ละคนนับได้ เป็นจำนวนเต็ม

รูปเเบบ Output
บรรทัดที่ 1 - เวลาที่ใช้ในการนับแกะของผู้ชนะ
บรรทัดที่ 2 - เวลาที่ใช้ในการนับแกะของผู้แพ้
บรรทัดที่ 3 - เวลาเฉลี่ยที่ใช้ในการนับแกะของทุกคน

ข้อจำกัด
การนับแกะ 1 ตัว ใช้เวลา 1 วินาที
N > 0
0 < จำนวนแกะ < 10000
กำหนดให้ การเฉลี่ยในโจทย์นี้ หารลงตัว

ตัวอย่างที่1
Input:
3
610
580
700

Output:
Winner : 0 hr 10 min 10 sec
Loser : 0 hr 9 min 40 sec
Average : 0 hr 10 min 30 sec

ตัวอย่างที่2
Input:
5
3600
3600
3600
3600
3600

Output:
Winner : 1 hr 0 min 0 sec
Loser : 1 hr 0 min 0 sec
Average : 1 hr 0 min 0 sec

ตัวอย่างที่3
Input:
6
3560
4790
2890
3745
1985
4780

Output:
Winner : 1 hr 19 min 50 sec
Loser : 0 hr 33 min 5 sec
Average : 1 hr 0 min 25 sec
'''
num = int(input())
time = [int(input() )for i in range(num)]
max_time = max(time)
min_time  = min (time)
avg_time = sum(time)/len(time)

def cal(time_item):
  sec = 0
  minute = 0
  hr = 0
  while time_item >0:
    time_item -=1
    sec+= 1
    if sec == 60:
      sec = 0
      minute += 1
    if minute == 60:
      minute = 0
      hr +=1
  return [hr, minute, sec]

winner = cal(max_time)
loser = cal(min_time)
avg = cal(avg_time)

print(f"Winner : {winner[0]} hr {winner[1]} min {winner[2]} sec")
print(f"Loser : {loser[0]} hr {loser[1]} min {loser[2]} sec")
print(f"Average : {avg[0]} hr {avg[1]} min {avg[2]} sec")

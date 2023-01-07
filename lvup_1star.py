'''
คำอธิบาย
สู้กับมอนเตอร์เพื่อจะได้Exp และไปอัพLv กันเถอะ
โดยมีแนวทางดังนี้อย่างแรกต้องแยกเอาตัวเลขออกมาเพื่อทำการคำนวณต่อไปเช่น Received 100 EXP from battle ก็ให้นำเอาเลข100ออกมาเพื่อ นำไปคิดต่อโดยที่มีสูตรการคิดของแต่ละเลเวลอยู่ว่า

maxexp = lv*100
ATK = lv*10
HP = lv*100

รูปเเบบ Input
รับExp ที่ได้จากการสู้กับมอนเอตร์

รูปเเบบ Output
แสดงเลเวลปัจจุบัน พร้อมทั้งความสามารถของตัวละครในเลเวลนั้นๆ

ตัวอย่างที่1
Input:
Received 0 EXP from battle

Output:
Lv : 1
Exp : 0/100
ATK : 10
HP : 100

ตัวอย่างที่2
Input:
Received 100 EXP from battle

Output:
Lv : 2
Exp : 0/200
ATK : 20
HP : 200

ตัวอย่างที่3
Input:
Received 350 EXP from battle

Output:
Lv : 3
Exp : 50/300
ATK : 30
HP : 300
'''
import re

get = input()

exp_list = re.findall("[0-9]+",get)
exp_list_int = list(map(int, exp_list))
exp_f = exp_list_int[0]

exp = exp_f
lv = 1
comute = 0
rest = 0
scrap = 0
while exp >=0:
  exp -= 100
  comute += 100
  if exp ==0:
    lv +=1
    break    
  elif exp < 100:
    rest = exp_f - scrap
    break 
  elif comute ==100*(lv):
    scrap += comute
    comute = 0
    lv += 1      
#print(lv)
#print(scrap)

print(f'Lv : {lv}')
print(f'Exp : {rest}/{lv*100}')
print(f'ATK : {lv*10}')
print(f'HP : {lv*100}')

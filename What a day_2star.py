'''
คำอธิบาย
ให้รับค่ามา 2 บรรทัด
บรรทัดแรกคือ วันใน 1 สัปดาห์(วันไหนก็ได้)
บรรทัดที่สองคือ จำนวนเต็ม n ที่มากกว่าหรือเท่ากับ 0
โปรแกรมจะคำนวณว่า จากวันในบรรทัดแรกไปอีก n วันจะเป็นวันอะไร

รูปเเบบ Input
บรรทัดแรก รับค่าวันเป็นภาษาอังกฤษตัวอักษรพิมพ์เล็กทั้งหมด

รูปเเบบ Output
แสดงผลวันที่ถัดจากบรรทัดแรก n วัน(เป็นตัวอักษรพิมพ์เล็กทั้งหมด)

Input:
monday
6

Output:
sunday

'''

day = input()
num = int(input())

dic1 ={'monday':1,'tuesday':2,'wednesday':3,
       'thursday':4, 'friday':5, 'saturday':6, 'sunday':7}
dic2 ={1:'monday', 2:'tuesday', 3:'wednesday',4:'thursday',
       5:'friday', 6:'saturday', 7:'sunday'}

a = num%7
b = dic1[day] + a

if b <=7:
  print(dic2[b])
elif b>=7:
  c = b-7
  print(dic2[c])

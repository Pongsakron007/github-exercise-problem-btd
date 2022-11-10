'''
คำอธิบาย
นาย A ได้เดินทางไปทำงานที่สถานที่หนึ่งซึ่งสถานที่นั้นมีแต่เลขโรมันแต่นาย A ไม่สามารถอ่านเลขโรมันได้จึงได้ทำการจ้างเราซึ่งเป็นโปรแกรมเมอร์ให้เขียนโค้ดที่แปลงจากเลขโรมันเป็นเลขอารบิกเพื่อช่วยเขา
จงทำการเขียนโปรแกรม ที่รับinputเป็นเลขโรมันและแสดงoutpuเป็นเลขอารบิก

รูปเเบบ Input
รับ input เป็น string ตัวพิมพ์ใหญ่ทั้งหมด

รูปเเบบ Output
แสดง output เป็น integer

ตัวอย่างที่1
Input:
IV

Output:
4
2

ตัวอย่างที่2
Input:
MD

Output:
1500

ตัวอย่างที่3
Input:
LX

Output:
60
'''
roman = input()
dic_r = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

list_result = []

for i in roman:
  list_result.append(dic_r[i])

  
if sorted(list_result, reverse=True) == list_result :
  print(sum(list_result))
else:
  result = 0
  accu = 0
  i = 0
  while i < len(list_result)-1:
    if list_result[i] == list_result[i+1]:
      accu += list_result[i]
      i += 1 
    elif list_result[i] < list_result[i+1]:
      if accu ==0:
        result += list_result[i+1]  - list_result[i]
      elif accu >0:
        result += list_result[i+1]  - accu
      accu = 0
      i += 1
  print(result)
      

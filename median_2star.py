'''
คำอธิบาย
ให้หาค่ามัธยฐาน(ค่ากึ่งกลาง) โดยรับค่า input มาตัวเดียวที่คั้นด้วยจุลภาค

รูปเเบบ Input
รับค่าตัวเลขมาโดยคั้นด้วย

รูปเเบบ Output
แสดงผลเป็นรูปแบบตัวเลข

ตัวอย่างที่1
Input:
2,3,5,7,8,11,12

Output:
7

ตัวอย่างที่2
Input:
1,1,3,4,2,5

Output:
2.5

ตัวอย่างที่3
Input:
23,24,24,25,26,27,29,30

Output:
25.5
'''
num = sorted(list(map(int, input().split(","))))

if len(num)%2 !=0:
  print(num[len(num)//2])
else:
  print((num[len(num)//2 - 1] + num[len(num)//2])/2)

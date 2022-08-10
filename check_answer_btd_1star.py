'''
คำอธิบาย
ในการตรวจข้อสอบมีกติกาในการตรวจอีกมากมาย
เราจึงเชิญชวนให้มีการตรวจข้อสอบชุดหนึ่ง สมมติว่าข้อสอบนี้มี n ข้อและซึ่งแต่ละข้อมีทั้งหมด 2 ตัวเลือกเท่านั้น
นั่นก็คือ A และ B นั่นเอง ซึ่งมีด้วยกัน 2 ชุดคำตอบที่จะตรวจ นั่นก็คือชุดคำตอบของผู้ทำข้อสอบและชุดคำตอบของเฉลย ซึ่งสมมติว่าเฉลยทุกอันจะต้องมี A และ B ให้ครบ n ข้อ ถ้าหากในการตรวจคนไหนทำข้อใดถูกจะต้องได้คะแนนข้อละ k คะแนน หากคนไหนทำข้อใดผิดจะต้องหักคะแนนข้อละ m คะแนน ข้อไหนไม่ได้ทำให้คะแนนข้อละ p คะแนน ซึ่งถ้าหากจะต้องการระบุว่าหักคะแนนแล้ว p<0 ซึ่งสัญลักษณ์ไม่ได้ทำให้แสดงเป็น X นั่นเอง ซึ่ง k,m,n>0 และ k,m,n,p เป็นจำนวนเต็ม

รูปเเบบ Input
บรรทัดแรกเป็นการนำเข้าค่า n,k,m,p โดยแสดงโดยคั่นด้วยช่องว่างตามลำดับ
บรรทัดที่สองเป็นการนำเข้าสตริงของชุดคำตอบของเฉลย
บรรทัดที่สามเป็นการนำเข้าสตริงของชุดคำตอบของผู้ทำข้อสอบ

รูปเเบบ Output
ให้แสดงผลคะแนนที่ได้แบบตัวอย่าง

Input:
5 3 2 1
ABABB
AXXBA

Output:
Your score:6
'''

n, k, m, p= list(map(int, input().split()))
corect = input()
ex = input()

score = 0

for i,j in zip(corect, ex):
  if i ==j :
    score += k
  elif j =="X":
    score += p
  elif i !=j :
    score -= m

print(f"Your score:{score}")  
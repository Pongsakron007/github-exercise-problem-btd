'''
คำอธิบาย
ในการแข่งขันเกมประเภททีมเกมหนึ่ง ผู้เล่นจะถูกแบ่งออกเป็นสองทีม ทีมละ N คน คนที่ 1 ของทีมแรกจะแข่งกับคน ที่ 1 ของทีมที่สอง ในทำานองเดียวกัน คนที่ 2 ของแต่ละทีมก็จะมาแข่งกัน และเป็นเช่นนี้จนครบทั้งหมด N คู่ กติกามี อยู่ว่าผู้เข้าแข่งขันแต่ละคนจะทำาแต้มตั้งแต่ 0 ถึง 10 คะแนน ถ้าใครทำาคะแนนมากกว่าคู่แข่งขันของตัวเองจะถือว่า ชนะในเกมนั้น ถ้าทำาได้น้อยกว่าถือว่าแพ้ และถ้าทำาได้เท่ากันถือว่าเสมอ
การชนะในแต่ละเกมจะทำาคะแนนให้กับทีมของผู้ชนะ 2 คะแนน การเสมอได้ 1 คะแนน และการแพ้จะไม่ได้ คะแนน ทีมที่มีคะแนนรวมมากกว่าเป็นฝเายชนะ ทีมที่มีคะแนนรวมน้อยกว่าแพ้ และ หากทั้งสองทีมได้คะแนนรวม เท่ากันถือว่าเป็นผลเสมอ

จงเขียนโปรแกรมที่รับแต้มของผู้เข้าแข่งขันแต่ละคนและสรุปผลการแข่งขันประเภททีมออกมาให้ได้ตามข้อ กำาหนดเรื่องข้อมูลเข้าและผลลัพธ์ต่อไปนี้

รูปเเบบ Input
เอาล่ะมาเริ่มกัน!!
1. บรรทัดแรกเป็นตัวเลขจำานวนเต็ม N ซูึ่งระบุจำานวนผู้เข้าแข่งขันของแต่ละทีม ( N≤1000 )
2. บรรทัดที่สองคือแต้มที่ผู้เข้าแข่งขันในทีมที่หนึ่งทำาได้ เรียงจากคนที่ 1 ไปคนที่ 2, 3, …, N โดยแต้มเป็นจำานวนเต็ม แต้มของแต่ละคนถูกคั่นด้วยช่องว่าง
3. บรรทัดที่สามคือแต้มที่ผู้เข้าแข่งขันทีมที่สองทำาได้ เรียงจากคนแรกไปคนสุดท้ายในลักษณะเดียวกับคะแนนของทีม ที่หนึ่ง

รูปเเบบ Output
1. บรรทัดแรกระบุทีมที่ชนะ [ดูรูปแบบผลลัพธ์ในตัวอย่างทางด้านใต้]
2. บรรทัดที่สองระบุคะแนนของทั้งสองทีม โดยนำาคะแนนของทีมที่ชนะขึ้นก่อน ในกรณีที่เสมอให้แสดงคะแนนของ ทีมไหนก่อนก็ได้ (เพราะคะแนนเท่ากันลำาดับจึงไม่มีผล)

ตัวอย่างที่1
Input:
5
1 2 3 1 4
3 9 3 5 6

Output:
Team 2 wins
Score 9 to 1

ตัวอย่างที่2
Input:
5
7 9 3 5 6
3 8 7 8 5

Output:
Team 1 wins
Score 6 to 4

ตัวอย่างที่3
Input:
7
7 8 7 8 5 5 9
9 9 7 4 4 6 6

Output:
Draw game
Score 7 to 7
'''
num = int(input())
team_1 = [int(i) for i in (input().split(" "))]
team_2 = [int(i) for i in (input().split(" "))]

score_a = 0
score_b = 0

for i, j in zip(team_1, team_2):
  if i > j:
    score_a += 2
  elif i < j:
    score_b += 2
  elif i == j:
    score_a += 1
    score_b += 1
    
total_s = [score_a, score_b]
if score_a > score_b:
  print("Team 1 wins")
elif score_a == score_b:
  print("Draw game")
elif score_a < score_b:
  print("Team 2 wins")
print(f"Score {max(total_s)} to {min(total_s)}")

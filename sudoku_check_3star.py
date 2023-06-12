'''
คำอธิบาย
ตรวจเช็คว่า ตาราง Sudoku ที่ให้มามีเลขซ้ำในแต่ละแถว คอลัมน์ และสี่เหลี่ยม3*3 หรือไม่

รูปเเบบ Input
9 บรรทัด แทนแต่ละแถวในตาราง
ตัวเลขแต่ละตัวจะคั่นด้วย เว้นวรรค 1 ช่อง

รูปเเบบ Output
หากไม่มีเลขซ้ำ = True
หากมีเลขซ้ำ = False

ข้อจำกัด
ตารางที่ให้มา มีทั้งแบบ ทำเสร็จแล้ว และยังไม่เสร็จ โดย 0=ช่องว่าง

ตัวอย่างที่1

Input:
0 0 3 0 0 0 0 0 9
0 0 0 0 7 0 0 0 0
2 0 0 5 8 0 3 0 0
0 8 0 1 5 0 0 0 4
0 0 0 0 0 7 5 0 0
1 0 0 0 0 0 0 0 0
0 4 0 0 0 0 0 6 0
0 0 0 0 0 1 0 0 0
8 0 0 2 3 0 9 0 0

Output:
True

ตัวอย่างที่2
Input:
0 0 3 0 0 0 0 0 9
0 0 0 0 7 0 0 0 0
2 0 0 5 8 0 3 0 0
0 8 0 1 5 0 0 0 4
0 0 0 0 0 7 5 0 0
1 0 0 0 0 0 0 0 0
0 4 0 0 0 0 0 6 0
0 0 0 0 0 1 0 0 0
8 0 0 2 3 0 9 0 6

Output:
False

ตัวอย่างที่3
Input:
4 5 3 6 1 2 7 8 9
9 6 8 4 7 3 1 2 5
2 1 7 5 8 9 3 4 6
7 8 9 1 5 6 2 3 4
6 3 4 9 2 7 5 1 8
1 2 5 3 4 8 6 9 7
3 4 1 7 9 5 8 6 2
5 9 2 8 6 1 4 7 3
8 7 6 2 3 4 9 5 1

Output:
True
'''
sudoku = [list(map(int, input().split())) for i in range(9)]

def check_row():
  mem = {}
  for row in sudoku:
    for column in row:
      if column == 0:
        pass
      else:
        if column not in mem:
          mem[column] = 1
        else:
          return False
    mem.clear()
  return True

def check_column():
  mem2 = {}
  for i in range(9):
    for row in range(9):
      if sudoku[row][i] == 0:
        pass
      else:
        if sudoku[row][i] not in mem2:
          mem2[sudoku[row][i]] =1
        else:
          return False
    mem2.clear()
  return True

def get_9_path():
  last_item = []
  for k in range(3):
    for i in range(3):
      mem_item = []
      for j in range(3):
        #mem_item = []
        item = sudoku[j + (i*3)][k*3:(k*3)+3]
        mem_item+= item
      last_item.append(mem_item)
  return last_item

def check_9_path():
  items = get_9_path()
  mem = {}
  for row in items:
    for column in row:
      if column == 0:
        pass
      else:
        if column not in mem:
          mem[column] = 1
        else:
          return False
    mem.clear()
  return True

print(check_row() and check_column() and check_9_path())

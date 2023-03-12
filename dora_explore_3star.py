'''
คำอธิบาย
โดร่าและผองเพื่อนของเธอได้ทำการสำรวจเกาะต่างๆ จากแผนที่ของเธอ ซึ่งเธอต้องการให้คุณช่วยนับเกาะในแผนที่ว่ามีจำนวนเกาะทั้งหมดกี่เกาะในแผนที่ ซึ่งในแผนที่นั้น จะใช้ # แทนสัญลักษณ์ของพื้นดิน และ . แทนสัญลักษณ์ของน้ำ ซึ่งถ้าพื้นดินอยู่ติดกัน(ทิศเหนือ ทิศใต้ ทิศตะวันออกและทิศตะวันตก)จะถือว่าเป็นเกาะเดียวกัน

รูปเเบบ Input
บรรทัดแรก รับค่าจำนวนเต็มบวก n และ m หมายถึง ขนาดของแถวและคอลลัมของแผนที่ตามลำดับ
อีก n บรรทัดต่อมา รับค่า # หรือ . หมายถึง สัญลักษณ์ของแผนที่ จำนวน m ตัว
n,m <= 100

รูปเเบบ Output
จำนวนเกาะทั้งหมด

ข้อจำกัด
n,m <= 100

ตัวอย่างที่1
Input:
4 4
###.
##..
#.##
.###

Output:
2

ตัวอย่างที่2
Input:
5 5
...##
...#.
.##..
...#.
#.##.

Output:
4

ตัวอย่างที่3
Input:
5 6
..#.##
###...
.#...#
#####.
#...#.

Output:
3
'''
from collections import deque

x, y = input().split(" ")
x, y = int(x), int(y)

grid = [input() for i in range(x)]

def numberisland(grid):
  if not grid:
    return 0
  
  rows, cols = len(grid), len(grid[0])
  visit = set()
  island = 0
  
  def bfs(r, c):
    q = deque()
    visit.add((r, c))
    q.append((r, c))
    while q:
      row, col = q.pop()
      directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
      for dr, dc in directions:
        r, c = row + dr, col + dc
        if (r in range(rows) and c in range(cols) and grid[r][c] == "#" and (r, c) not in visit):
          q.append((r, c))
          visit.add((r, c))
          
  for r in range(rows):
    for c in range(cols):
      if grid[r][c] == "#" and (r, c) not in visit:
        bfs(r, c)
        island +=1
  return island
  
print(numberisland(grid))

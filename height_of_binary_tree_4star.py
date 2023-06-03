'''
คำอธิบาย
เขียนโปรแกรมเพื่อหาความสูง (Height) ของต้นไม้ (Binary Search Tree) จากชุดข้อมูลที่ได้รับ
Height of Binary Tree in C/C++ - JournalDev
แผนภาพแสดงการค่าความสูง (Height) ของต้นไม้

รูปเเบบ Input
บรรทัดที่ 1 จำนวนชุดข้อมูล (n)
บรรทัดที่ 2 - (n + 1) รับค่าข้อมูล (x1, x2, x3,..., xn)

รูปเเบบ Output
จำนวนความสูงของต้นไม้จากชุดข้อมูลที่ได้รับ

ข้อจำกัด
กำหนดให้จำนวนชุดข้อมูลมีค่าไม่เกิน 100 (n <= 100)
กำหนดให้ข้อมูลที่ได้รับตัวแรก (x1) เป็นรากของต้นไม้ (Root)

ตัวอย่างที่1
Input:
3
4
1
6

Output:
2

ตัวอย่างที่2
Input:
7
5
3
2
9
11
4
8

Output:
3
3
ตัวอย่างที่3
Input:
9
6
5
4
8
3
7
9
2
11

Output:
5
'''
class Node:
  def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data
    
  def insert(self, data):
    if data < self.data:
      if self.left:
        self.left.insert(data)
      else:
        self.left = Node(data)
    elif data > self.data:
      if self.right:
        self.right.insert(data)
      else:
        self.right = Node(data)

def get_tree_height(root):
    if root is None:
        return 0
    else:
        left_height = get_tree_height(root.left)
        right_height = get_tree_height(root.right)
        return max(left_height, right_height) + 1


nums = int(input())
tree = [int(input()) for i in range(nums)]

root = Node(tree.pop(0))

while tree:
  root.insert(tree.pop(0))
  
tree_height = get_tree_height(root)
print(tree_height)

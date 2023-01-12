'''
คำอธิบาย
Given a list of integers, return a new list with all even numbers doubled.

รูปเเบบ Input
The input for this problem is a list of integers. For example, [1, 2, 3, 4].

รูปเเบบ Output
The output for this problem is a new list of integers, where all even numbers from the original list are doubled. For example, given the input [1, 2, 3, 4], the function would return [1, 4, 3, 8].

ข้อจำกัด

1
ตัวอย่างที่1
Input:
1 2 3 4

Output:
1 4 3 8

ตัวอย่างที่2
Input:
5 6 7 8

Output:
5 12 7 16

ตัวอย่างที่3
Input:
9 10 11 12

Output:
9 20 11 24
'''
list_num = list(map(int, input().split(" ")))

new_list = [str(i) if idx%2==0 else str(i*2) for idx, i in enumerate(list_num)]
result = " ".join(new_list) 
print(result)

'''
คำอธิบาย
พี่โดมเป็นโปรแกรมเมอร์ได้รับโจทย์จากการสมัครงาน โดยโจทย์มีอยู่ว่า ให้เขียนโปรแกรมในการตรวจสอบ Palindrome เช่น 'asoi' ไม่เป็น Palindrome เพราะว่าหลังจาก reverse แล้วได้ iosa ไม่ตรงกับ asoi ที่ยังไม่ revrse เป็นต้น

รูปเเบบ Input
รับค่าจาก argument ใน function checkPalindrome(str)

รูปเเบบ Output
return ข้อความ str is a Palindrome หรือ str is not palindrome

ตัวอย่างที่1
Input:
abba

Output:
abba is a palindrome.

ตัวอย่างที่2
Input:
asdf

Output:
asdf is not a palindrome.
'''

string = input()

def palindrome(string):
  if string==string[::-1]:
    print(f"{string} is a palindrome.")
  else:
    print(f"{string} is not a palindrome.")
    
palindrome(string)

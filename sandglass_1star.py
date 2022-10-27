'''
คำอธิบาย
นาฬิกาทรายรูปแบบ Star Pattern

รูปเเบบ Input
for

รูปเเบบ Output

* * * * * * * 
 * * * * * * 
  * * * * * 
   * * * * 
    * * * 
     * * 
      * 
      * 
     * * 
    * * * 
   * * * * 
  * * * * * 
 * * * * * * 
* * * * * * * 

ตัวอย่างที่1
Input:
7

Output:

* * * * * * * 
 * * * * * * 
  * * * * * 
   * * * * 
    * * * 
     * * 
      * 
      * 
     * * 
    * * * 
   * * * * 
  * * * * * 
 * * * * * * 
* * * * * * * 
'''
num = int(input())

def sandglass(num):
  for i in range(num,0,-1):
    print(" "*(num-i) +"* "*i)
  for row in range(1,num+1):
    print(" "*(num-row) +"* "*row)
    
sandglass(num)

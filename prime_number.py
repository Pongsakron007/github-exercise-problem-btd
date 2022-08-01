get = int(input())

def prime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

count = 0
for i in range(2,get+1):
    if prime(i) == True:
        count +=1

print(f"จำนวนเฉพาะในช่วง 0 ถึง {get}")
print(f"มีอยู่ {count} จำนวน")


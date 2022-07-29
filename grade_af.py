'''
คำอธิบาย
โดยการคำนวณเกรดนั้นจะมีการให้คะแนนตามเกรดแต่ละช่วงเป็น
80- 100 ได้เกรด A ,
70 - 79 ได้เกรด B ,
60 - 69 ได้เกรด C ,
50 - 59 ได้เกรด D และ ต่ำกว่า 50 จะได้เกรด F โดยผู้ใช้จะต้องกรอกเป็นตัวเลขจำนวนเต็มเท่านั้น


'''
point = int(input())

if point >=80 and point <=100:
    print("A")
elif point >=70 and point <=79:
    print("B")
elif point >=60 and point <=69:
    print("C")
elif point >=50 and point <=59:
    print("D")
else:
    print("F")

'''
คำอธิบาย
โจทย์นี้นายเซฟรู้ว่าเขาต้องรอเพื่อนเป็นเวลาหนึ่ง ซึ่งเพื่อนของเขาบอกมาเป็นหน่วยวินาที แต่นายเซฟอยากรู้ว่านั่นเป็นกี่ชั่วโมง เราจึงต้องเขียนโปรแกรมเพื่อแปลงเวลาจาก วินาที เป็น ชั่วโมง ให้นายเซฟ

รูปเเบบ Input
เวลา (วินาที)

รูปเเบบ Output
เวลา (ชั่วโมง)

Input: 12345

Output: 3:25:45
'''

second = int(input())


def convert(seconds):
  seconds = seconds % (24 * 3600)
  hour = seconds // 3600
  seconds %= 3600
  minutes = seconds // 60
  seconds %= 60
      
  return "%d:%02d:%02d" % (hour, minutes, seconds)

print(convert(second))

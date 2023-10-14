s = '7' * 104
s = s[(104 // 14) * 14:]
s = s.replace('777', '3')
print(s)

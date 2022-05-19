selfish = 'me me me'
        # 01234567
print(selfish[0]) #m

selfish = '01234567'
# [start:stop:stepover]
print(selfish[0:2]) #01
print(selfish[0:8]) #01234567
print(selfish[1:]) #1234567
print(selfish[:5] #01234)
print(selfish[::1]) #01234567
print(selfish[-1]) #76543210 (negative index means start at the end of the string)
print(selfish[::-1] #76543210 (negative two will skip by two in reverse)
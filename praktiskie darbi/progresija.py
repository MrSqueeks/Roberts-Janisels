print('Aritmētiskas progresijas elementu aprēķins')
print('Ievadiet pirmo locekli!')
a = int(input())
print('Ievadiet diferenci!')
b = int(input())
print('Ievadiet elementu skaitu!')
c = int(input())
print('')
print('1 . loceklis: ',float(a))
for i in range(2,c+1):  
    while i <=c:
        if True:
            print(i,'. loceklis: ',float(a+b*(i-1)))
            i += 1
        break
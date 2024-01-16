print("Ievadiet 3 skaitļus:")
a = int(input())
b = int(input())
c = int(input())

#loģiskais and
""""
if a>0 and b>0 and c>0:
    print('Visi skaitļi ir lielāki par 0')
else:
    print('Vismaz viens skaitlis nav lielāks par 0!')
"""
#loģiskais and
if a>0 or b>0 or c>0:
    print('Vismaz 1 skaitlis ir lieāks par 0')
else:
    print('Neviens skaitlis nav lielāks par 0!')

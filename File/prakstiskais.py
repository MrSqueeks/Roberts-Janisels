reiz = 7
for i in range(1,13):
    print('Cik ir ',i,'x',reiz,'?')
    minejums = input()
    if minejums == 'stop':
        break #Ar break programma beidzas

    if minejums == 'izlaist':
        print('Tiek izlaists')
        continue 
    atb = i*reiz #glabā pareizās abildes
    if int(minejums) == atb:
        print('Pareizi')
    else:
        print('Nē, tas ir',atb)
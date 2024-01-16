import math
while True:
    linolejacena = float(input('Ievadiet linoleja cena kvadrātmetrā:'))
    rullaplatums = int(input('Ievadiet rulla platumu metros:'))
    telpasgarums = float(input('Ievadiet telpas garumu metros:'))
    telpasplatums = float(input('Ievadiet telpas platumu metros:'))
    telpasplatiba = telpasgarums*telpasplatums
    print('telpas platība', telpasplatiba, 'm2')
    print('Jums vajadzēs:', telpasplatiba, 'kvadrātmetru linoleja')

    print('-----------Veikals "Depo"-----------------')
    linolejadaudzums = math.ceil(telpasgarums*telpasplatums)/rullaplatums
    print('Jums nepieciešams:', round(linolejadaudzums),  ' m2 linoleja')

    izmaksas = linolejadaudzums*linolejacena
    print('Izmaksas par linoleju ir:', round(izmaksas,2),'Eiro')

    apaksklaju_ieklasana = input('Vai jūs vēlaties ieklāt apakšklāju?(ja/ne)')
    if apaksklaju_ieklasana == 'ja':
        ievadietapaksklajucenu = float(input('Lūdzu ievadiet apakšklāju cenu:'))
        apaksklajukopejacena = round(linolejadaudzums*ievadietapaksklajucenu,2)
        print('Apaksklāju cena ir:', apaksklajukopejacena,'$')
    if apaksklaju_ieklasana == 'ne':
        apaksklajukopejacena = 0
        print()
    
    Turpinatprogrammu = input('Vai jūs vēlaties sākt programmu no jauna?(ja/ne)')
    if Turpinatprogrammu.upper() == 'ja':
        continue
    if Turpinatprogrammu == 'ne':
        break

def ceks():
    print('Jums nepieciešams:', round(linolejadaudzums),  'm2 linoleja')
    print('Izmaksas par linoleju ir:', round(izmaksas,2),'Eiro')
    kopejacena = round(izmaksas + apaksklajukopejacena,2)
    print('Kopējā cena ir:',kopejacena, '$')

ceks()

while True:
    kontakti = {'vards':[], 'numurs':[]}
    kontakti['vards'] = ['Anna','Zane','Jānis','Gustavs']
    kontakti['numurs'] = ['12547865', '45697456','26588965','12365445']

    drukatkontaktus = input('Vai jūs vēlaties drukāt kontaktus uz ekrāna?(ja/ne)')
    if drukatkontaktus == 'ja':
        print(kontakti)
    if drukatkontaktus == 'ne':
        print()

    pievienotkontaktus = input('Vai jūs vēlatis pievienot kontaktus?(ja/ne)')
    jaunakontaktavards = input('Ievadiet jaunā kontakta vārdu:')
    jaunakontaktanumurs = int(input('Ievadiet jaunā kontakta numuru:'))
    kontakti.update({'vards': ['Anna','Zane','Jānis','Gustavs', jaunakontaktavards], 'numurs': ['12547865', '45697456','26588965','12365445',jaunakontaktanumurs]})
    print(kontakti)


    izdzestkontaktus = input('Vai jūs vēlaties izdzēst kontaktus? (ja/ne)')
    if izdzestkontaktus == 'ja':
        vards = input('Ievadi kontakta vārdu kuru vēlaties dzēst:')
        index = kontakti['vards'].index(vards)
        kontakti['vards'].pop(index)
        kontakti['numurs'].pop(index)
        print(kontakti)
    if izdzestkontaktus == 'ne':
        print()

    iziesana = input('Vai jūs velaties iziet no programmas?(ja/ne)')
    if iziesana == 'ja':
        print('Uzredzēšanos!')
        break
    if iziesana == 'ne':
        print('Programma turpinās!')
        continue

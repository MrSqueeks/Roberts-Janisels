def fun():
    p = input('Ievadiet preces nosaukumu:')
    a = float(input('Ievadiet preces cenu:'))
    b = int(input('Ievadiet preču daudzumu:'))
    
    if b<0:
        print('Preču daudzums nevar būt mazāks nekā 0')
        exit()
    
    s = (a*b)*0.3


    print(p,',preces cena ar 30% atlaidi ir:',round((a*b)*0.3),'$')
    jautajums1 = input('Vai jums ir atlaižu karte (j/n)')
    if jautajums1 == 'j':
        print(p,',preces cena ar karti, 40% atlaidi ir:',round((a*b)*0.4),'$')
        print(p,',preces cena ar karti, 50% atlaidi ir:',round((a*b)*0.5),'$')
    if jautajums1 == 'n':
        print(p,',preces cena bez kartes ar 20% atlaidi ir:',round((a*b)*0.2),'$')
    if b >= 3:
        print(p,',preces cena pērkot 3 un vairāk, ar 30% atlaidi ir:',round((a*b)*0.3),'$')      
    jautajums3 = input('Vai ir nopirkts viss, kas sarakstā (j/n)')
    if jautajums3 == 'n':
        return(fun)

    if jautajums3 == 'j':
        print('-------------čeks----------------')
    


""" print('30% atlaide ir',round(atlaide1),'$')
print('40% atlaide, ja ir karte ir',round(atlaide2),'$')
print('20%, ja nav karte ir',round(atlaide4),'$')
print('50% atlaide, ja ir karte ir',round(atlaide3),'$')
print('30% atlaide, ja pērk 3 preces un vairāk ir:',round(atlaide5),'$')
print('Kopā viss maksā',round(atlaide1 + atlaide2 + atlaide3 + atlaide4 + atlaide5),'$') """
while True: 
    p = input('Ievadiet preces nosaukumu:')
    a = float(input('Ievadiet preces cenu:'))
    b = int(input('Ievadiet preču daudzumu:'))
    if b<0:
        print('Preču daudzums nevar būt mazāks nekā 0')
        exit()
    atlaide1 = (a*b)*0.3
    atlaide2 = (a*b)*0.4
    atlaide3 = (a*b)*0.5
    atlaide4 = (a*b)*0.2
    atlaide5 = (a*b)*0.3

    def fun():

    print(p,',preces cena ar 30% atlaidi ir:',atlaide1,'$')
    jautajums1 = input('Vai jums ir atlaižu karte (j/n)')
    if jautajums1 == 'j':
        atlaide2 = (a*b)*0.4
        print(p,',preces cena ar karti, 40% atlaidi ir:',atlaide2,'$')
        atlaide3 = (a*b)*0.5
        print(p,',preces cena ar karti, 50% atlaidi ir:',atlaide3,'$')
        
    if jautajums1 == 'n':
        atlaide4 = (a*b)*0.2
        
        print(p,',preces cena bez kartes ar 20% atlaidi ir:',atlaide4,'$')

    if b >= 3:
        atlaide5 = (a*b)*0.3
        print(p,',preces cena pērkot 3 un vairāk, ar 30% atlaidi ir:',atlaide5,'$')
        


    jautajums3 = input("Vai ir nopirkts viss, kas sarakstā (j/n): ")
    if jautajums3.upper() == "n": #go back to the top
      continue    
    
    if jautajums3 == "j":
        break
print('______čeks__________-')
print(p,',preces cena ar 30% atlaidi ir:',atlaide1,'$')
print(p,',preces cena ar karti, 40% atlaidi ir:',(a*b)*0.4,'$')
print(p,',preces cena ar karti, 50% atlaidi ir:',(a*b)*0.5,'$')
print(p,',preces cena bez kartes ar 20% atlaidi ir:',(a*b)*0.2,'$')
print(p,',preces cena pērkot 3 un vairāk, ar 30% atlaidi ir:',(a*b)*0.3,'$')
def sum():
    skaitli = atlaide1 + atlaide2 + atlaide3 + atlaide4 + atlaide5
    print(skaitli)

sum()
#Uzrakstīt programmu, kurā ir 2 saraksti. Ar + abus apvienot
mans_saraksts = ['svece',2,'sāls'] #pirmais elements ir ar indeksu 0
otrs_saraksts = ['karstmaizes','brauniji','kafija']

liels_saraksts = mans_saraksts + otrs_saraksts
print(liels_saraksts)

#nokopēt saraksta vērtības un ieliktā tās jaunajā sarakstā
milzis = ['zupa','dzervene','tastatūra']
jauns = list(milzis)
print(milzis)
print(jauns)

#izveidot sarakstu ar 4 krāsu nosaukumiem. Atrast katra elementa garumu
krasas = ['zils','zaļš','dzeltens','balts']
jauns_saraksts = [] #tukšs saraksts
for krasa in krasas:
    burti = 0 #katru reizi palaižot sarakstu, atgriežas uz 0
    for burts in krasa:
        burti +=1 #katru reizi pieskaita 1
    pagaidu_saraksts = [krasa, burti]
    jauns_saraksts.append(pagaidu_saraksts)

print(jauns_saraksts)

#Kā šo kodu var uzrakstīt ar mazāk rindiņām? Vai ir vienkāršāks veids kā atrast katra vārda garumu?
krasas = ['zils','zaļš','dzeltens','balts']
for krasa in krasas:
    print(len(krasa))


#variants 3
krasas = ['zils','zaļš','dzeltens','balts']
jauns_saraksts = []
for krasa in krasas:
    jauns_saraksts.append([krasa, len(krasa)])
print(jauns_saraksts)
valstis = {
    'Latvija': 1884000,
    'Igaunija': 1331000,
    'Lietuva': 2801000,
    'Vācija': 83200000,
    'Polija': 37750000,
    'Nīderlande':17530000,
    'Rumānija':19120000,
    'Ungārija':9710000,
    'Bulgārija':6878000,
    'Beļģija':11590000,
}   #valstis un to iedzīvotāju skaits

while True:   
    izvelne= input("""Ko vēlaties darīt?
                   1-drukāt sakārtotas valstis pēc nosaukuma augošā secībā
                   2-drukāt sakārtotas valstis pēc to nosaukuma dilstošā secībā
                   3-drukāt sakārtotas valstis pēc to iedzīvotāju skaita augošā secībā
                   4-drukāt sakārtotas valstis pēc to iedzīvotāju skaita dilstošā secībā
                   5-pievienot jaunu valsti un iedzīvotāju skaitu
                   6-drukāt visas valstis
                   7- iziet no programmas \n """) #programma darbojas līdz lietotājs uzspiež 7 jeb exit
    izvelnes_atbilde = int(izvelne)  #Lietotājam iespēja ievadīt skaitli, kas kodā tālāk ļaus veikt darbības

    if izvelnes_atbilde == 1:
        valstis_pec_nosaukuma2 = dict(sorted(valstis.items()))  #sakārto valstis pec to nosaukuma augušā secībā
        print('Valstu nosaukumi augošā secībā:', valstis_pec_nosaukuma2)

    if izvelnes_atbilde == 2:
        valstis_pec_nosaukuma2 = dict(sorted(valstis.items(),  reverse = True))  #sakārto valstis pec to nosaukuma dilstošā secībā
        print('Valstu nosaukumi dilstošā secībā:',valstis_pec_nosaukuma2)

    if izvelnes_atbilde == 3:
        valtis_pec_skaita1 = sorted(valstis.items(), key=lambda x:x[1])    #sakārto valstis pec to iedzīvotāju skaita augošā secībā
        print('Valstu iedzīvotāju skaits augošā secībā:', valtis_pec_skaita1)

    if izvelnes_atbilde == 4:
        valstis_pec_skaita2 = sorted(valstis.items(), key=lambda x:x[1], reverse=True)  #sakārto valstis pec to iedzīvotāju skaita dilstošā secībā ar reverse=True
        print('Valstu iedzīvotāju skaits dilstošā secībā:', valstis_pec_skaita2)
       

    if izvelnes_atbilde == 5:     #Lietotājs ievada jaunās valsts nosaukumu un tās iedzīvotāju skaitu, kā arī kods atjaunina "veco" vārdnīcu ar jaunajiem parametriem
            jaunavalsts = input('Ievadiet jaunās valsts nosaukumu:')
            if jaunavalsts == 'stop': #ja lietotājs ievada 'stop', programma beidzas
                print("Uzredzēšanos, programma beigusies!")
                exit()
            jaunasvalstsiedzivotajuskaits = int(input('Ievadiet jaunās valsts iedzīvotāju skaits:'))
            valstis.update({jaunavalsts:jaunasvalstsiedzivotajuskaits})
            print('Pievienotās valsts nosaukums un iedzīvotāju skaits:')
            for i, j in valstis.items():
                print(i, ' : ', j)
    if izvelnes_atbilde == 6:  #Izprintēs visu valstu nosaukumus un iedzīvotāju skaitu ar for ciklu (tehniski so jau varēja saprast pēc koda) 
        print('Visu valstu nosaukumi un iedzīvotāju skaiti:')
        for x, y in valstis.items():
            print(x, y)

    if izvelnes_atbilde == 7:  #Iziet no programmas
        print('Uzredzēšanos, programma beigusies!')  
        exit()          



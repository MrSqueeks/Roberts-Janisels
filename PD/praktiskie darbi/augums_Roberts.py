augumspreksdzesanas = {'vards':[], 'augums':[]} #
augumspreksdzesanas['vards'] = ['Anna','Zane','Jānis','Gustavs','Roberts','Reinis','Arturs','Laura','Iveta','Gerda','Markuss','Valters']#
augumspreksdzesanas['augums'] = ['172', '185','164','184','162','164','165','167','177','184','165','180']#
#mainīgie lai varetētu izdzēst (nesanāca savādāk)
augums = {
    'Anna': '172',
    'Zane': '185',
    'Jānis':'164',
    'Gustavs':'184',
    'Roberts':'162',
    'Reinis':'164',
    'Arturs':'165',
    'Laura':'167',
    'Iveta':'177',
    'Gerda':'184',
    'Markuss':'165',
    'Valters':'180'
}   #augumi, prekš skolēniem


while True:   
    izvelne= input("""Ko vēlaties darīt?
                   1-drukāt skolēnu vārdus un to augumus
                   2-pievienot skolēnu un to augumu 
                   3-izdzēst skolēnu(automatiski tiek izdzēst tā skolēna numurs)
                   4-iziet no programmas 
                   5- Videjais augums \n """) #programma darbojas līdz lietotājs uzspiež 4 jeb exit
    izvelnes_atbilde = int(izvelne)  #Lietotājam iespēja ievadīt skaitli, kas kodā tālāk ļaus veikt darbības

    if izvelnes_atbilde == 1:   #Izprintēs skolēnus un to augumus stabiņāa uz leju
        for x, y in augums.items():
            print(x, y)
    elif izvelnes_atbilde == 2:
            jaunaskolenavards = input('Ievadiet jaunā skolēna vārdu:')
            jaunaskolenaaugums = int(input('Ievadiet jaunā skolēna augumu:'))
            augums.update({'vards':['Anna','Zane','Jānis','Gustavs','Roberts','Reinis','Arturs','Laura','Iveta','Gerda','Markuss','Valters', jaunaskolenavards], 'augums':['172', '185','164','184','162','164','165','167','177','184','165','180', jaunaskolenaaugums]})
            print(augums)
    elif izvelnes_atbilde == 3:   #Izdzēsīs skolēna vārdu un to augumu
        vards = input('Ievadi skolēna vārdu kuru vēlaties dzēst:')
        index = augumspreksdzesanas['vards'].index(vards)
        augumspreksdzesanas['vards'].pop(index)
        augumspreksdzesanas['augums'].pop(index)
        print(augumspreksdzesanas)
    elif izvelnes_atbilde == 4:   #Izies no programmas
        print('Programmas beigas!')
        exit()
    elif izvelnes_atbilde == 5:   #Aprēķinās vidējo augsumu skolēniem
        videjaisaugums = (172 + 185 + 164 + 184 + 162 + 164 + 165 + 167 + 177 + 184 + 165 + 180)/12 
        print('videjais augums ir:', round(videjaisaugums), "cm")


        valstis_pec_nosaukuma1 = sorted(valstis)
    sorted_valstis1 = {key:valstis[key] for key in valstis_pec_nosaukuma1}
    print(sorted_valstis1)
dati = ('viens','divi','trīs')
vertiba = input('Vērtība:')
vardnica = dict.fromkeys(dati, vertiba)
print(vardnica)
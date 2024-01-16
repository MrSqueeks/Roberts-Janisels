def virsraksts():  #Funkcija kuras mērķis ir uz ekrāna parādīt ko viņa dara un 55 zvaigznītes
    print('Faktoriāla aprēķināšana')
    i = 55
    for i in range(0,i):
        print("*", end="")
virsraksts()
def atstarpes(): #Funkcija, kas ieliks 2 atstarpes jeb 2 jaunas līnijas
   print()
   print()


while True:    
    def faktorials(): #Funkcija, kas aprēķina skaitļa faktoriālu
     num = int(input("\nIevadiet veselu pozitīvu skaitli(mazāku par 13): "))    #Lietotājs ievada skaitli ar kuru vēlas faktoriālu          
     if num > 13: #Ja ievadītais skaitlis ir lielāks par 13, tad parādīs print funkcijā ierakstītu tekstu
       print("Īevadītais skaitlis ir pārāk liels!")

     factorial = 1  
     if num < 13:    #Ja ievadītais skaitlis ir mazāks par 13, tad izrēķinās tā skaitļa faktoriālu
       for i in range(1,num + 1):    
        factorial = factorial*i    
       print("Faktoriāls",factorial)

    faktorials()

    turpinatdarbu = input('Vai vēlies turpināt darbu(j-jā, citi taustiņi-nē)')

    if turpinatdarbu == 'j': #Ja lietotājs ievada "j" tad while cikls atkārtojās
        atstarpes()
    else:  #Ja ievada citu taustiņu, kas nav "j" tad programma beidzas
        atstarpes()
        print('Paldies!')
        exit()  
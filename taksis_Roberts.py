n = int (input ("Enter a number: "))

factorial = 1

if n >= 1:

              for i in range (1, n+1):

                             factorial = factorial *i

print ("Factorial of the given number is: ", factorial)

















def lol():
    num = int(input("Enter a number: "))    
    factorial = 1

        
    if num < 0:    
        print(" Factorial does not exist for negative numbers")
    elif num == 0:    
     print("The factorial of 0 is 1")     
  
    if num < 13:    
     for i in range(1,num + 1):    
        factorial = factorial*i    
    print("The factorial of",num,"is",factorial)
    if num > 13:
       print('Parak liels skaitlis')
             
lol()














"""def faktorials():
    num = 7
    factorial = 1
    num = int(input("Enter a number: "))
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1,num + 1):
            factorial = factorial*i
            print("The factorial of",num,"is",factorial)

faktorials():"""




pasažieri = int(input("Ievadiet pasažieru skaitu?")) #Pārbaudam pasažieru skaitu
if pasažieri <=0:    #Pārbaudu vai pasažieri nav mazāks vai vienāds ar 0, jo savādāk tas būtu aplami
    print("Ievadi pareizus datus")
    exit()
elif pasažieri<=4: #Pārbaudu vai pasažieri ir lielāka vai vienāds ar 4
    print(pasažieri, "pasažieri/s")
else:
    print("Pasažieru ir pārāk daudz") 
    exit()
laiks = int(input("Ievadiet laiku")) #Lietotājs ievada laiku
if laiks>=24 or laiks<0:   #Pārbaudu vai laiks nav lielāks par 24
    print("Ievadiet pareizus datus") 
    exit()
elif laiks<22 and laiks>=6: #Pārbaudu vai laiks ir mazāks kā 22 un lielāks vai vienāds ar 6
    print("1km cena ir 0.57$")
    x = 0.57  #Piešķīru vērtību 1km braucot pa dienu
else:
    print("1km cena ir 0.67$")
    x = 0.67  #Piešķīru vērtību 1km braucot pa nakti
nolīgšana = str(input("Vai firmai pie dzelzceļa stacijas atrodas taksometrs(j/n)"))   #Pārbaudu vai pie firmas atrodas kāds taksis
if nolīgšana == 'j':
    print("Par nolīgšanu jāmaksā 2,20$")
    y = 2.20    #Piešķiru vērtību par nolīgšanu, ja taksis atrodas
elif nolīgšana == 'n':
    print("Par nolīgšanu jāmaksā 3,45$")
    y= 3.45      #Piešķiru vērtību par nolīgšanu, ja taksis neatrodas
else:     #Ja tiek ievadūīti nepareizi dati:
    print("Ievadi pareizus datus")
    exit()
gaidisana = input("Vai jūs braukšanas laikā vēlēsieties piestāt?(j/n)")  #Pārbaudu, vai lietotājs vēlesies piestāt, un taksistam japagaida
if gaidisana == 'j':    #Ja pasažierim vajadzēs piestāt
    maksa = int(input("Cik minūtes jums ir plānot piestāt?"))  #Pārbaudu, cik ilgi pasažierim vajadzēs piestāt
    print("Par gaidīšanu/piestāšanu jāmaksā", maksa*0.13, "$")
    z = (maksa*0.13)  #Pievienoju mainīgo, lai pēc tam čekā būtu šī maksa par gaidšanu
elif gaidisana == 'n':    #Ja pasažierim nevajadzēs piestāt, tad iet tālāk un par gaidīšanu jamakšair 0 (jo pasažieris nepiestāja)
    print()
    z = 0   #Piešķiru vērtību, lai vēlāk tas parādītos čekā
    maksa = 0 #Piešķiru vērtību, lai vēlāk tas parādītos čekā
else:    #Ja tiekievadīti nepareizi dati:
    print("Ievadi pareizus datus")
    exit()
cels = int(input("Cik km brauksiet?"))  #Pārbaudu cik tālu(km) pasažierim būs jābrauc
if cels<=0:    #Pasažieris nevar nobraukt negatīvus km, tapat arī 0km
    print("Ievadi pareizus datus")
    exit()
elif cels<=20:        #Papildnosacījums, ja jūs vēlaties braukt tālāk par 20km, taksists atteiksies jūs vest, ja mazāk, tad vedīs
    print("Par braukšanu jums jāmaksā", cels*x, "$")
else:
    print("Taksista vadītājs atsakās tik tālu braukt")
    exit()

print("Čeks:")
print("...........................")
print("Jūs nobraucāt", cels, "km")
print("Jūs piestājāt", maksa, "minūtes")
print("Par nolīgšanu jums jāmaksā", y, "$")
print("Par gaidīšanu/piestāšanu jums jāmaksā", z, "$")
print("Par braukšanas attālumu jums jāmaksā", cels*x, "$")
print("Kopēja cena par braucienu ir", cels*x + y + z, "$")
print("...........................")
print("Paldies, ka veicāt braucienus, ar Roberta taksi, gaidīsim jūs vēlāk :^)")



def virsraksts():
    print('Faktoriāla aprēķināšana')
    i = 55
    for i in range(0,i):
        print("*", end="")
virsraksts()
def atstarpes():
   print()
   print()

while True:   
    def faktorials():
     num = int(input("\nIevadiet veselu pozitīvu skaitli(mazāku par 13): "))    
     factorial = 1    
     if num < 0:    
        print(" Faktoriāls skatlis nevar būt negatīvs")
     elif num > 13:
        print("Īevadītais skaitlis ir pārāk liels!")        
        exit()
        

     if num < 13:    
         for i in range(1,num + 1):    
            factorial = factorial*i    
     print("Faktoriāls",factorial)
    faktorials()
    turpinatdarbu = input('Vai vēlies turpināt darbu(j-jā, citi taustiņi-nē)')

    if turpinatdarbu == 'j':
        atstarpes()
    else:
        atstarpes()
        print('Paldies!')
        exit()  






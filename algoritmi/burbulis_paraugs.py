#Programma ļauj lietotājam ievadīt skaitļus, pēc tam tos sakārtot ar burbuļkārtošanu.
#izaicinājums- tajā pašā programmā uztaisīt f-ju quickSort un selectionSort
#papildināt, noformēt pēc saviem ieskatiem

def burbulis(saraksts):
    elementi = len(saraksts) #kopējais elementu saraksts
    for i in range(elementi):
        for j in range(0,elementi-i-1): #elements peld uz augšu, nonākot pareizajā vietā
            #izlaiž pēdējo(sakārtoto) elementu
            if saraksts[j]>saraksts[j+1]: #ja patiess, tad notiek swap
                saraksts[j],saraksts[j+1] = saraksts[j+1], saraksts[j]

def sakartot():
    elementi = int(input("Ievadiet skaitļu skaitu sarakstā: "))
    saraksts = []

    for i in range(elementi):
        skaitlis = int(input(f"Ievadiet {i+1}. skaitli: "))
        saraksts.append(skaitlis)

    burbulis(saraksts)
    print('Sakārtotais saraksts:')
    for skaitlis in saraksts:
        print(skaitlis, end= " ")

sakartot()
def burbulis(saraksts):
    for key,value in saraksts.items():
        if(saraksts[key]<saraksts[key+1]):
            temp=saraksts[key]
            saraksts[key]=saraksts[key+1]
            saraksts[key+1]=temp
   

def sakartot():
    elementi = int(input("Ievadiet studentu skaitu sarakstā: "))
    saraksts = {}

    for i in range(elementi):
        vards = input(f"Ievadiet {i+1}. skolēna vārdu: ")
        atzime = int(input(f"Ievadiet {i+1}. atzīmi: "))
    saraksts[vards] = atzime
    marklist=list(saraksts.items())
    l=len(saraksts)
    for i in range(l-1):
        for j in range(i+1,l):
            if marklist[i][1]>marklist[j][1]:
                t=marklist[i]
                marklist[i]=marklist[j]
                marklist[j]=t
    sortdict=dict(marklist)
    print(sortdict)

sakartot()

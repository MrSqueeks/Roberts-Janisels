def selectionSort(array, size):
   
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
         
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
         
        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])



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
    
    uz_augsu_vai_leju = input("Kā jūs vēlaties printēt sarakstu? (up/down)")
    if uz_augsu_vai_leju == 'up':
        print("\n".join("{}\t{}".format(k, v) for k, v in sortdict.items()))
    elif uz_augsu_vai_leju == 'down':
        uz_leju_sakaroti_dati = sorted(saraksts.items(), key=lambda x:x[1], reverse=True)
        converted_dict = dict(uz_leju_sakaroti_dati)
        print(converted_dict)
    else:
        print('Nepareizi ievadīti dati')
sakartot()

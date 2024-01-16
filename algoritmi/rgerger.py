
"""def Sort_Tuple(saraksts):
 
    # getting length of list of tuples
    lst = len(saraksts)
    for i in range(0, lst):
 
        for j in range(0, lst-i-1):
            if (saraksts[j][1] > saraksts[j + 1][1]):
                temp = saraksts[j]
                saraksts[j] = saraksts[j + 1]
                saraksts[j + 1] = temp
    return saraksts
 
 
# Driver Code
elementi = int(input("Ievadiet studentu skaitu sarakstā: "))
saraksts = {
    'vards': [],
    'atzime': [],
}

for i in range(elementi):
    vards = input(f"Ievadiet {i+1}. skolēna vārdu: ")
    atzime = int(input(f"Ievadiet {i+1}. atzīmi: "))
    saraksts['vards'].append(vards)
    saraksts['atzime'].append(atzime)
 
print(Sort_Tuple(saraksts))"""

markdict={"Tom":67, "Tina": 54, "Akbar": 87, "Kane": 43, "Divya":73}
marklist=list(markdict.items())
l=len(marklist)
for i in range(l-1):
    for j in range(i+1,l):
        if marklist[i][1]>marklist[j][1]:
            t=marklist[i]
            marklist[i]=marklist[j]
            marklist[j]=t
sortdict=dict(marklist)
print(sortdict)
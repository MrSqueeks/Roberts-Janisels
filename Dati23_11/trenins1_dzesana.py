file_name = 'Dzest.txt'
delete_me = 'Drīz būs Ziemassvētku brīvdienas!'

try:
    with open(file_name, 'r',encoding='UTF=8') as data:
        #r atver failu lasīšanai saglabā mainīgajā data
    #readline ielasa visas rindas no faila un saglabā sarakstā
        rows = data.readlines()

    with open(file_name, 'w', encoding='UTF=8') as data: #atver rakstīšanai(pārraksta)
        for row in rows: #iterē cauri visām sarkasta rindām
            if delete_me not in row:
                data.write(row)
            #ja neatrod vārdu, tad ši rinda ieraksta šo rindu atpakaļ failā
            #ignorējot vai izdzēšot rindas, kuras atbilst
        print(f'Rindas ar vārdu "{delete_me}" ir veiksmīgi dzēst no faila "{file_name}".')

except FileNotFoundError:
    print(f"Kļūda: Fails '{file_name}' nav atrasts.")
except Exception as e:
    print(f"Kļūda: Neparedzēta kļūda - {e}")

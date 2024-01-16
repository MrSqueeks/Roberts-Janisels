telefoni = {
    "zimols": "Apple",
    "modelis": "14",
    "gads": 2021
}
telefoni.update({'gads': '2022'})
print(telefoni)

skolas = {
    "nosaukums": "Gimnazija",
    "novads": "Sigulda",
    "skolenu_skaits": 569,
    "gads": 2019
}
skolas.clear()
print(skolas)

augli = {1:'banani',2:'aboli',3:'bumbieri',4:'mango'}
augli.pop(1, 'banani')
print(augli)

skaitli = {'a': 100, 'b': 200, 'c': 300, 'd': 400}

if 200 in skaitli.values():
    print('Skaitlis 200 ir vārdnīcā!')

augums = {'vards':[], 'augums':[]}
augums['vards'] = ['Anna','Zane','Jānis','Gustavs','Roberts','Reinis','Arturs','Laura','Iveta','Gerda','Markuss','Valters']
augums['augums'] = ['172', '185','164','184','162','164','165','167','177','184','165','180']
import json
#izveidot txt failu ar nosaukumu dati2.txt
fails = open('dati2.txt','a',encoding='utf-8')

#ierakstīt failā sarakstu ar 3 pilsētām
saraksts = ['Rīga\n','Sigulda\n','Jaunpiebalga\n']
fails.writelines(saraksts)
fails.write('Hello, World!') #ieraksta vienu virkni
#pārrakstiet faila saturu uz 3 valstīm
valstis = {
    'Somija':'Fazer',
    'Latvija':'Laima',
    'Lietuva':'Ruta'
}

"""fails.write(str(valstis))"""
"""with open('dati2.txt','w')as f:
    for key, value in valstis.items():
        f.write('%s:%s\n'%(key, value))"""
with open('dati2.txt', 'w') as file:
    file.write(json.dumps(valstis)) # use json.loads to do the revers
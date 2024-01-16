fails = open('dati.txt','a',encoding='utf-8') #izveidos failu
fails.write('Ingvera sula garšo pēc suši!!\n')
#katru reizi palaižot programmu, teksts tiek pievienots klāt 

fails = open('dati.txt','r',encoding='utf-8') #izveidos failu
print(fails.read())

fails = open('dati.txt','w',encoding='utf-8')
#w pārraksta datus
fails.write('Mācos rakstīt failā')


fails = open('dati.txt','a',encoding='utf-8') #a pievieno klāt datus esošajiem
fails.write('\nlolololololol')

fails.close()
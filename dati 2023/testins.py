fails = open("ziema.txt",'w',encoding='UTF-8')
#w arī izveido neeksistējošu failu no jauns
#ieraksta failā datus
saraksts = ["Alūksne\n", "Valmiera\n","Balvi\n"]
fails.writelines(saraksts) #ieraksta vairākas rindiņas
fails.write('Es te braukšu ar telti gulēt')
fails.close()


#pārrakstīt kopētā faila saturu
fails = open("ziema_copy.txt",'w+',encoding='UTF-8')
fails.write('Varētu drīz iet pusdienās!')
fails = open("ziema_copy.txt",'w+',encoding='UTF-8')
print(fails.read()) #parāda faila saturu uz ekrāna
fails.close()

fails = open("ziema_copy.txt",'a+',encoding='UTF-8')
fails.write('\nCerams pusdienas šodien būs garšīgas!')
fails.close()
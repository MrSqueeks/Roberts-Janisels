parole='kruts'
lietotaja_v='Roberts'
meginajumi = 5 

while meginajumi > 0:             #While loop kurs sakas ar 5 mēģinājumiem
    ievaditas_lietotaja_v=input('Ievadiet lietotāja vārdu:')
    if ievaditas_lietotaja_v == lietotaja_v:       #Parbauda vai sakrīt ar īsto paroli
        break
    elif ievaditas_lietotaja_v == 'stop': #ieavadot stop quit() arā no programmas
        quit('Programmas beigas!')
    else: #katru mēģinājumu kad nav pareizi tad tas no 5 mēģinājumiem atņem 1 nost
        print('Mēģini vēlreiz. Ir palikuši',meginajumi,'mēģinājumi!')
        meginajumi -=1
if meginajumi==0: 
    quit('Atļauts mēģināt pieslēgties 5 reizes')
    
while meginajumi > 0:    #While loop kurs sakas ar 5 mēģinājumiem         
    ievadita_parole=input('Ievadiet paroli:')
    if ievadita_parole == parole:   #Parbauda vai sakrīt ar īsto paroli    
        break
    elif ievadita_parole == 'stop':
        quit('Programmas beigas!')
    else: #katru mēģinājumu kad nav pareizi tad tas no 5 mēģinājumiem atņem 1 nost
        print('Mēģini vēlreiz. Ir palikuši',meginajumi,'mēģinājumi!')
        meginajumi -=1
if meginajumi==0:
    quit('Atļauts mēģināt pieslēgties 5 reizes')

if len(parole) == 5:#šeit pārbauda vai parole ir 5 rakstzīmes gara 
    print('Tā ir 5 rakstzīmes gara') 
else:
    print('Parole nav 5 rakstzīmes gara')

print('\nPieslēgšanās veiksmīga!\n')
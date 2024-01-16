import math
import random
print('Ievadiet riņķa līnijas rādiusu:')
rl = int(input())   #Lietotājs ievada riņķa līnijas rādiusu
print("{:.1f}".format(rl))
rlg = (2*math.pi)*rl #Aprēķins riņķa līnijas garumam
print('Riņķa līnijas garums:'"{:.2f}".format(rlg))
rll = math.pi*(math.pow(rl,2))    #Aprēķins riņķa līnijas laukumam
print('Riņķa līnijas laukums:'"{:.2f}".format(rll))
print('Ievadiet taisnleņķa trijstūra pirmās katetes garumu:')
katete1 = int(input())   #Lietotājs ievada kateti
print('Ievadiet taisnleņķa trijstūra otrās katetes garumu:')
katete2 = int(input())   #Lietotājs ievada kateti
h = math.sqrt(math.pow(katete1,2)+(math.pow(katete2,2)))    #Aprēķina taisnleņķa hipotenūzas garumu
print('Taisnleņķa trijstūra hipotenūzas garums:'"{:.2f}".format(h))
cipars = random.random()   #Tiek izvēlēt "random" jeb nejaušs skaitlis no 0-1
print('Gadījuma skaitlis no 0-1:', cipars)
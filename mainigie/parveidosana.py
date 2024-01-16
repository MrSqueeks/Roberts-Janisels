#int pārveidošana par str(a un b saskaita)
#a un b kā teksts tiek konkatenēti(concat)
from re import S


a = 5
b = 7
print('skaitlis',a + b) #int tipa mainīgie tiek saskaitīti
print('teksts',str(a)+str(b)) #kā teksts tiek konatenēti
a = str(a)
b = str(b)
print('teksts',a + b) 

#str pārveidošana par int
s = '123'
t = '456'
print(s+t, type(s+t))
a = int(S) #virkni s pārveido par int tipa mainīgo
b = int(t) #virkni t pārveido par int tipa mainīgo
print(a+b,type(a+b))

#pārveido no par float un atpakaļ
a = 5
print(a,type(a))

a=float(a)
a=int(a)
print(a,type(a))

a=123.56
a=int(a)
print(a,type(a))
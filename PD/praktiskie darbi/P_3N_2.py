import math
import random
print('Matemātisko funkciju lietosana')
print('-------------------------------------')
a = int(input('Ievadiet veselu skaitli a:'))
print(a)
b = float(input('Ievadiet veselu skaitli b:'))
print(b)
print('Skaitļa ',a,' absolūtā vērtība ir', float(abs(a)))
print('Skaitļa ',b,' noapalota vertiba ir',float(round(b)))
print('Skaitlis ',a,' pakāpē 2 ir',math.pow(a,2))
print('Skaitla ',b,' kvadrātsakne ir ',math.sqrt(b))
gad2 = random.random()
gad1 = random.random()
print('Pirmais gadijuma skaitlis ir', gad1)
print('Otrais gadijuma skaitlis ir',"{:.6f}".format(gad2))
ran = random.randint(10,11)
print('Gadījuma skaitlis intervala 10 līdz 11 ir', ran)
print('PI vērtība ir', math.pi)
print('PI vērtība ir '"{:.2f}".format(math.pi))
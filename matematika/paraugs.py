import math #raksta programmas sākumā tikai 1 reizi
skaitlis = 21.6
print('Noapaļots uz leju:',math.floor(skaitlis)) #Noapaļo uz leju
print('Noapaļots uz augšu:',math.ceil(skaitlis)) #Noapaļots uz augšu

print('PI vērtība:',math.pi) #atgriež PI vērtību
print(math.pow(skaitlis,3)) #kāpina skaitli 3.pakāpē

#skaitļu formatēšana
x = 252463/213
print('Bez formatēšanas:',x)
print('Ar formatēšanu:', "%.4f"%x)
print('Ar formatēšanu:'"{:.2f}".format(x))

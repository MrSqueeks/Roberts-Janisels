""" def summa(skaitli):
    kopsumma = 0
    for i in skaitli:
        kopsumma +=i
    return kopsumma
    
print(summa((1,2,3,4,5))) """

#Programmā ir f-ja, kas celsija grādus pārveido par fārenheita grādiem
a = int(input("Ievadiet celsija grādus:"))
def grādi():
    b = (a * 9/5) + 32
    print(b)
grādi()

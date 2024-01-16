def gcd(x, y): 
    if x == 0 : 
        return y 
     
    return gcd(y%x, x) 

skaitlis1 = int(input("Ievadiet pirmo skaitli: "))
skaitlis2 = int(input("Ievadiet otro skaitli: "))
if skaitlis1 > skaitlis2:
    x = skaitlis1
    y = skaitlis2
else:
    x = skaitlis2
    y = skaitlis1

print("Lielākais dalītājs (", x , "," , y, ") ir = ", gcd(x, y)) 
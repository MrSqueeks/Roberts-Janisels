#atrastu skaitļus 2 un 4 dalītājus
for i in range(41):       #i ir saitlis kas ies līdz 40
    if i%2==0 and i%4==0:
        print(i, ":dalos ar 2 un 4")
    elif i%2==0:
        print(i, ":dalos ar 2")
    elif i%4==0:
        print(i, ":dalos ar 4")
    else:
        print(i)

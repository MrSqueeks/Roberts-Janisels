#izveidot sarakstu 'atzime' ar punktiem (testā iegūtajiem)(10 rezultāti no 60 - 99)
#ar for ciklu 'iziet cauri' visiem sarakstiem
#ar elif nosacījumu uz erānu parādīt punktus ar atzīmi
# >=90 - A, >=80 - B, starp 70 un 80 - C, no 60 - 70 -D, ja krīt zem 60 - F
#grūtāk - var pielikt datu ievadi atkarībā no ievadītā skaitļa, parādīt punktu

[78, 'C'], [93, 'A'], [81, 'B'], [87,'B']
atzimes = [int(input('punkti = '))]
#atzimes = [60, 65, 70, 75, 80, 85, 90, 95, 99]
rez = []
for punkti in atzimes:
    if punkti >=90:
        atzime = 'A'
    elif punkti >=80:
         atzime = 'B'
    elif punkti >=70:
         atzime = 'C'
    elif punkti >=60:
         atzime = 'D'
    else:
        atzime = 'F'
    rez.append([punkti,atzime])
print(rez)

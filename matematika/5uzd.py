print('Ievadiet malas A garumu:')
Amala = int(input())
print('Malas A garums:'"{:.1f}".format(Amala))
print('Ievadiet malas B garumu:')
Bmala = int(input())
print('Malas B garums:'"{:.1f}".format(Bmala))
print('Ievadiet augstumu:')
augstums = int(input())
print('Augstums:'"{:.1f}".format(augstums))
ltrij = (Amala*augstums)/2
print('Laukums trijstūrim:'"{:.1f}".format(ltrij))
ltrap = Amala*augstums
print('Laukums trapecei:'"{:.1f}".format(ltrap))
lpar = ((Amala+Bmala)/2)*augstums
print('Laukuma paralelograms:'"{:.1f}".format(lpar))
print('Paldies!')

print('ieveadiet savu vārdu')
vards = input()
print("Jūsu vards ir:,",vards)

print('')
print("ievadiet decimālskaitli:")
x = float(input()) #javeic kovertēšama, jo input() f-ja datus atgreiž teksta veidā
print('Ievadītais skaitlis:',x)

print("ievadiet decimālskaitli:")
y = float(input()) #javeic kovertēšama, jo input() f-ja datus atgreiž teksta veidā
print('Ievadītais skaitlis:', y)

rezultats = (x+y)*(x-y)//(y-x)
print('rezultats:', rezultats)

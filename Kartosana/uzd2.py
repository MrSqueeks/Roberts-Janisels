vecums = {
    'Anna': '31',
    'Zane': '10',
    'Jānis':'11',
    'Gustavs':'84',
    'Roberts':'62',
    'Reinis':'54',
    'Arturs':'62',
    'Laura':'40',
    'Iveta':'20',
    'Gerda':'15',
    'Markuss':'16',
    'Valters':'18'
} #Tēma: vecums. Atslēga- cilvēku vārdi, vērtība - cilvēku vecums
for i in range(1):
    vards = input("Ievadiet atslēgu(jeb clivēku vārdu): ")
    cilvekuvecums = input("Ievadiet vērtību(jeb clivēku vecumu): ")

    vecums[vards] = cilvekuvecums

print(vecums)

dilstosi = dict(sorted(vecums.items(),  reverse = True)) 
print(dilstosi)

vecums_vertiba = sorted(vecums,key=vecums.get)
kartota_vardnica = {}

for key in vecums_vertiba:
    kartota_vardnica[key] = vecums[key]
print("Vārdnīca kārtota pēc vērtībām:",kartota_vardnica)
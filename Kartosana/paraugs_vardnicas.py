krasas = {'red':'#FF0000',
          'green':'#008000',
          'black':'#000000',
          'white':'#FFFFFF'}

for atslega in sorted(krasas):
    print((atslega, krasas[atslega])) #sakārtots pēc atslēgas augošā secībā

veikals = {
    'banāni':12,
    'apelsīni':32,
    'arbūzi':21,
    'mandarīni':17,
    'vīnogas':15
}

'''izveidot sarakstu ar sorted() funkciju, kas atgriež vērtības
augošā secībā. Ar for ciklu iziet cauri key:value pārim jaunajā vārdnīcā'''
kartots = sorted(veikals, key=veikals.get)

for vertiba in kartots:
    print(vertiba,veikals[vertiba])

kartota_vardnica = {}
for key in kartots:
    kartota_vardnica[key] = veikals[key]
print(kartota_vardnica)
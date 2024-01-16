"""darzeni = ['zirņi','burkāni','kartupeļi','batātes','gurķi']
print('Orģinālais saraksts:',darzeni)
darzeni.sort()
print('Sakārtots ar sort:', darzeni)

viens = [5,4,6,1,8,2]
print(sorted(viens)) #atgriež jaunu sarakstu, nemainot orģinālo
print(sorted(viens, reverse=True))
print('Orģinālais:', viens)

darzeni_kartots = sorted(darzeni, reverse=True)
print('Apgriezts:', darzeni_kartots)"""

'''saraksts = ['viens','divi','trīs','pieci','septiņi','deviņi']
saraksts_augosi = print(sorted(saraksts,key=len)) #pēc garuma augoši
saraksts_dilstoši = print(sorted(saraksts,key=len, reverse=True)) #pēc garuma dilstoši'''

strs = ['rīts', 'Vakars', 'pusdienas', 'KOMPLEKSIŅŠ','ZEMENES']
strs.sort() # nevar likt printā, tad neiet
print('Kārtots:', strs)
print('Kārtots ar str.lower:',sorted(strs, key=str.lower)) #ignorē uppercase
print('Kārtots ar str.lower:',sorted(strs, key=str.upper)) #ignorē lowercase
print('Kārtots ar str.lower:',sorted(strs, key=str.lower, reverse=True)) #ignorē uppercase, samaina vārdu secību
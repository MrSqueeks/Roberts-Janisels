skaitli= [100,200,45,2,0.5,77,100,55,400]
zoo = ['zebra','lūsis','lama','kamielis','briedis']
saraksts_augosi = print(sorted(zoo,key=len)) 
saraksts_dilstoši = print(sorted(zoo,key=len, reverse=True))
print(sorted(skaitli))
print(sorted(skaitli, reverse=True))
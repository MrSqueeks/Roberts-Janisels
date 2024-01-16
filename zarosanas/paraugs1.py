atbilde = input('Vai tev ir laba diena?(j/n)')
if atbilde == 'j': #salīdzināšana veicama ar 2 vienādības zīmēm
    print('Apsveicu')

teksts = input('Vai sodien ir Jaungada diena?(j/n)')
if teksts == 'j':
    print('Laiks salūtam!')
else: #pie else nosacījumu nebbūs(tas it tas, kas paliek pāri)
    print('Bēdīgi..') #šis tiek palaists tikai tad, 
    #ja lietotājs neieraksta 'j'
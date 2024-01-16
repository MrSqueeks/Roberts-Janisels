file_name = 'Dzest.txt'
putnew_me = 'Drīz būs Ziemassvētku brīvdienas!'

try:
    with open('dzest.txt', 'a', encoding='utf-8') as fails:
        fails.write('\n' + putnew_me)
    print(f'Jauna informācija ir veiksmīgi pievienota failam "{file_name}".')


except FileNotFoundError:
    print(f"Kļūda: Fails '{file_name}' nav atrasts.")
except Exception as e:
    print(f"Kļūda: Neparedzēta kļūda - {e}")

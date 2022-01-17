data_base = [
    {'id': 1, 'imie': 'Jan', 'nazwisko': 'Kowalski', 'konto1': {'id': 1, 'bank': 'NBP', 'srodki': 1800}},

    {'id': 2, 'imie': 'Filip', 'nazwisko': 'Meger', 'konto1': {'id': 1, 'bank': 'PKO', 'srodki': 13300},
     'konto2': {'id': 2, 'bank': 'PKK', 'srodki': 3850}},

    {'id': 3, 'imie': 'Daria', 'nazwisko': 'Gajdamowicz', 'konto1': {'id': 1, 'bank': 'PKO', 'srodki': 420}},

    {'id': 4, 'imie': 'Kuba', 'nazwisko': 'Paszke', 'konto1': {'id': 1, 'bank': 'PKK', 'srodki': 420},
     'konto2': {'id': 2, 'bank': 'NBP', 'srodki': 120}, 'konto3': {'id': 3, 'bank': 'PKO', 'srodki': 4990}}
]

searched_bank = 'PKO'
money_sum = 0

for person in data_base:
    count = 0
    for id_name in person:
        if count > 2:
            if person[id_name]['bank'] == searched_bank:
                money_sum += person[id_name]['srodki']
        count += 1

print(money_sum)

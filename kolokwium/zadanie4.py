data_base = [
    {'id': 1, 'imię': 'Jan', 'Nazwisko': 'Kowalski',
     'konto 1': {'id': 1, 'nazwa banku': 'PKO', 'suma środków': 2200},
     'konto 2': {'id': 2, 'nazwa banku': 'NBP', 'suma środków': 1300}},
    {'id': 2, 'imię': 'Mirosław', 'Nazwisko': 'Debko',
     'konto 1': {'id': 3, 'nazwa banku': 'NBP', 'suma środków': 420},
     'konto 2': {'id': 1, 'nazwa banku': 'ING', 'suma środków': 12200}, },
    {'id': 3, 'imię': 'Filip', 'Nazwisko': 'Jażdżewski',
     'konto 1': {'id': 1, 'nazwa banku': 'PKO', 'suma środków': 10000}},
    {'id': 4, 'imię': 'Agata', 'Nazwisko': 'Paczkowska',
     'konto 1': {'id': 1, 'nazwa banku': 'NBP', 'suma środków': 7700},
     'konto 2': {'id': 2, 'nazwa banku': 'PKO', 'suma środków': 4111}
     }
]


def sum_of_funds(data, bank):
    my_sum = 0
    for person in data_base:
        print(person)




import csv

def extract():
    data = []
    with open('input.csv',mode = 'r') as file:
        csv_reader = csv.DictReader(file)
        for line in csv_reader:
            data.append(line)
        return data


def transform(donnee_a_transformer):
    donnee_a_charger = []
    for data in donnee_a_transformer:
        donnee_transformee = {}
        donnee_transformee['nom'] = data['nom']
        data['heures_travaillees'] = int(data['heures_travaillees'])*15
        donnee_transformee['salaire'] = str(data['heures_travaillees'])
        donnee_a_charger.append(donnee_transformee)
    return donnee_a_charger
    
def load(donnee_a_charger):
    with open('output.csv',mode = 'w') as file:
        titre_champs = ['nom','salaire']
        writer = csv.DictWriter(file, fieldnames=titre_champs)
        writer.writeheader()
        for data in donnee_a_charger:
            writer.writerow(data)


donnee_non_traitee = extract()
donnee_a_charger = transform(donnee_non_traitee)
print(transform(donnee_non_traitee))
load(donnee_a_charger)
import csv

with open('data.csv', mode='r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
    for row in reader:
        print(row)

headers = ['Nom', 'Age']
data =  [
    {'Nom': 'Ferdinant', 'Age': '65'},
    {'Nom': 'Gerard', 'Age': '23'},
    {'Nom': 'Harry', 'Age': '18'},
    {'Nom': 'Ivon', 'Age': '15'},
    {'Nom': 'Jessica', 'Age': '32'},
]
with open('data.csv', mode='a', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=headers)
    csvfile.write('\n')
    writer.writerows(data)
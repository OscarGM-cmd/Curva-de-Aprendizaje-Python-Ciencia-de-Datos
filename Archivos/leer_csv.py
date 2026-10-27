import csv

with open("Archivos\\datos.csv") as archivos:
    reader = csv.reader(archivos)
    for row in reader:
        print(row)

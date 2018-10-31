import csv

print("Comecou")

with open('DadosGeodrone.csv', mode='w') as DadosGeoDrone:


    DadosGeodrone_writer = csv.writer(DadosGeoDrone, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    DadosGeodrone_writer.writerow(['DJI', 'Numero', 'Data'])
    DadosGeodrone_writer.writerow(['Matrice', '200', 'Setembro'])
    DadosGeodrone_writer.writerow(['Matrice', '600', 'Outubro'])

print("Terminou")

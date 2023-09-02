import csv

#crear una funcion con persisos solo de lectura 'r'
def read_csv(path):
    with open (path, 'r') as csvfile:
        #creando el lector, 
        #el delimitador es  la forma en la que vienen separados los datos, siempre verificar
        reader = csv.reader(csvfile, delimiter=',')
        #leer fila a fila
        for row in reader:
            print('***' * 5)
            print(row)

#para ejecutar como script desde la terminal:
#la siguiente linea verifica si el archivo se está ejecutando directamente o si se está importando como un módulo
if __name__ == '__main__':
    read_csv(./'friends_episodes.csv')
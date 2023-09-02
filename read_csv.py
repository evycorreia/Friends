import csv

#crear una funcion con persisos solo de lectura 'r'
def read_csv(path):

#para evitar el error UnicodeDecodeError try...
    try:

        with open (path, 'r', encoding='ISO-8859-1') as csvfile:
            #creando el lector, 
            #el delimitador es  la forma en la que vienen separados los datos, siempre verificar
            reader = csv.reader(csvfile, delimiter=',')
            #leer fila a fila
            for row in reader:
                print('***' * 5)
                print(row)

    except UnicodeDecodeError:
        print('No se puso abrir el archivo con la codificación ISO-8859-1')       

#para ejecutar como script desde la terminal:
#la siguiente linea verifica si el archivo se está ejecutando directamente o si se está importando como un módulo
if __name__ == '__main__':
    read_csv('friends_episodes.csv')
limite = int(input("Inserte el valor máx de la serie ") )
anterior = 0
inicial = 1
fibonacci = str(0)
suma = 0
while inicial <= limite:
   
    fibonacci = fibonacci + ","  + str(suma)
   
    suma = anterior + inicial
    anterior = inicial
    inicial = suma
   
    print(fibonacci)
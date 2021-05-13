limite = int(input("Inserte el limite de la serie  ") )
anterior = 0
inicial = 1
fibonacci = str(0)
while inicial <= limite:
  
    suma = anterior + inicial
    fibonacci = fibonacci + ","  + str(suma)
    #print(fibonacci)
    anterior = inicial
    inicial = suma
    print(fibonacci)
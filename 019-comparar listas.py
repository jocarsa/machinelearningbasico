from PIL import Image,ImageFilter

imagen = Image.open("prueba/tepongoaprueba.png")
escalado = imagen.resize((512,512))
grises = escalado.convert("L")
bordes = grises.filter(ImageFilter.FIND_EDGES)
blancoynegro = bordes.point(lambda x:0 if x < 50 else 255,'1')
pixeles = blancoynegro.load()
anchurabloque = 2
longitud = pow(2,pow(anchurabloque,2))
lista = []
for i in range(0,longitud):
    lista.append(0)
for xi in range(0,512-anchurabloque):
    for yi in range(0,512-anchurabloque):
        cadena = ""
        for x in range(0,anchurabloque):
            for y in range(0,anchurabloque):
                if pixeles[xi+x,yi+y] == 255:
                    cadena += "1"
                else:
                    cadena += "0"
        lista[int(cadena,2)] += 1
print(lista)

memoria = open("memoria.txt",'r')
for linea in memoria:
    tipo = linea.split("|")[0]
    valores = linea.split("|")[1]
    milista = [int(value) for value in valores.split(',')]
    suma = 0
    for i in range(0,len(lista)):
        suma += abs(lista[i] - milista[i])
    print(tipo+": "+str(suma))
memoria.close()







    

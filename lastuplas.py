arcoiris=("Azul","Verde","Rojo","Amarillo")
print(arcoiris)
print("-longtud arcoiris-")
print(len(arcoiris))
animales=("Pantera",20,"estatura",1.7)
print(animales)
print("elemento de la tupla")
print(animales[2])
rateros =("Juan","Ana","Pedro")
y=list(rateros)
y[0]="Polainas"
x=tuple(y)
print(x)
print("Agregando elementos")
Nanimal=("body","cheto",)
y=list(Nanimal)
print(y)
y.append("tontolin")
otratupla=tuple(y)
print(otratupla)
print("Uso de for en tuplas")
for elcolor in arcoiris:
    print(elcolor)
    
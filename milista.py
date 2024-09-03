# ejemplo de uso de lista
Misnovias=["Agripina","Anastacia","Maria"]
misNumeros=[666, 77, 10]
# Mostrando mis novias
print(Misnovias)
# Mostrando mis numeros raros
print(misNumeros)
print("--- accediento a los elementos de la lista ---")
print(Misnovias[-2])
if "Ana" in Misnovias:
    print("si, 'Agripina' esta en la lista de mis novias")
else:
    print("Chale no eres mi novia")
    print("Numeros de novias")
    Nnovias=len(Misnovias)
    print(f"Numero de novias = {Nnovias}")

    print("ciclo for en listas")
    posicion=0
    for medianaranja in Misnovias:
        print(posicion," ",medianaranja)
        posicion=posicion+1
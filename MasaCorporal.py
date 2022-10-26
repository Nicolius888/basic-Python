peso = int(input("ingresa tu peso: "))
estatura = float(input("ingresa tu altura: "))

indice = int(peso // (estatura**2))

print(f"Tu indice de masa corporal es:  {indice}")



#Ejemplo: Peso = 68 kg, Estatura = 165 cm (1.65 m)
#Cálculo: 68 ÷ (1.65)2 = 24.98


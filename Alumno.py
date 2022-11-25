#En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno 
# que tenga como atributos su nombre y su nota.
# Deberéis de definir los métodos para inicializar sus atributos, 
#imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class Alumno():
    nombre = None
    note = None

    def nombre(self, nombre):
        self.nombre = nombre
        print(self.nombre)
    
    def nota(self, nota):
        self.nota = nota
        print(self.nota)
        if (nota > 4):
            print("Alumno aprobado!")
        else: print("Alumno desaprobado.")

newAlumno = Alumno()
newAlumno2 = Alumno()

newAlumno.nombre("Paco")
newAlumno.nota(8)

newAlumno2.nombre("Juan")
newAlumno2.nota(1)

#Ouptut:
#Paco
#8
#Alumno aprobado!
#Juan
#1
#Alumno desaprobado.

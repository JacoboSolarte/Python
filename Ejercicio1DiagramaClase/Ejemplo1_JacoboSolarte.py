class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo_bruto):
        super().__init__(nombre, edad)
        self.sueldo_bruto = sueldo_bruto

class Directivo(Empleado):
    def __init__(self, nombre, edad, sueldo_bruto, categoria, subordinados=[]):
        super().__init__(nombre, edad, sueldo_bruto)
        self.categoria = categoria
        self.subordinados = subordinados

class Cliente(Persona):
    def __init__(self, nombre, edad, telefono_contacto):
        super().__init__(nombre, edad)
        self.telefono_contacto = telefono_contacto

# Ejemplo de uso
if __name__ == "__main__":
    empleado1 = Empleado("Juan", 35, 850000)
    empleado2 = Empleado("Oscar", 28, 450000)

    directivo1 = Directivo("Luis", 45, 2000000, "Gerente", [empleado1, empleado2])

    cliente1 = Cliente("Carlos", 30, "123-456-7890")
    cliente2 = Cliente("Samuel", 22, "987-654-3210")

    # Mostrar los datos de empleados
    print("Datos de Empleados:")
    print(f"Nombre: {empleado1.nombre}, Edad: {empleado1.edad}, Sueldo Bruto: {empleado1.sueldo_bruto}")
    print(f"Nombre: {empleado2.nombre}, Edad: {empleado2.edad}, Sueldo Bruto: {empleado2.sueldo_bruto}")

    # Mostrar los datos de clientes
    print("\nDatos de Clientes:")
    print(f"Nombre: {cliente1.nombre}, Edad: {cliente1.edad}, Teléfono de Contacto: {cliente1.telefono_contacto}")
    print(f"Nombre: {cliente2.nombre}, Edad: {cliente2.edad}, Teléfono de Contacto: {cliente2.telefono_contacto}")

    #Mostrar Datos Directivo
    print("\nDatos del directivo:")
    print(f"Nombre : {directivo1.nombre}, Edad : {directivo1.edad}, Sueldo : {directivo1.sueldo_bruto}, Cargo : {directivo1.categoria}")

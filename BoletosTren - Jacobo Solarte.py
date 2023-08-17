class BilleteDeTren:
    def __init__(self, destino, precio):
        self.destino = destino
        self.precio = precio

class SistemaExpedicion:
    def __init__(self):
        self.destinos = {
            "A": BilleteDeTren("Destino A", 150),
            "B": BilleteDeTren("Destino B", 75),
            "C": BilleteDeTren("Destino C", 120)
        }

    def mostrar_menu(self):
        print("Bienvenido al sistema de expedición de billetes de tren")
        print("Seleccione su destino:")
        for codigo, billete in self.destinos.items():
            print(f"{codigo}: {billete.destino} - ${billete.precio}")

    def expedir_billete(self, destino, tarjeta_credito, pin):
        if destino in self.destinos:
            billete = self.destinos[destino]
            print(f"Billete expedido para {billete.destino}.")
            print(f"Se ha cargado ${billete.precio} en su tarjeta de crédito.")
        else:
            print("Destino inválido.")

def main():
    sistema = SistemaExpedicion()

    while True:
        sistema.mostrar_menu()
        seleccion = input("Seleccione el destino (A/B/C): ")
        tarjeta_credito = input("Ingrese el número de tarjeta de crédito: ")
        pin = input("Ingrese su número de identificación personal (PIN): ")

        sistema.expedir_billete(seleccion.upper(), tarjeta_credito, pin)

        continuar = input("¿Desea comprar otro billete? (si/no): ")
        if continuar.lower() != "si":
            print("Gracias por utilizar nuestro sistema.")
            break

if __name__ == "__main__":
    main()

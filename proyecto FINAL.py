#proyecto final
import json
import os

class Reserva:
    ReservaID = 1

    def __init__(self, nombre_cliente, numero_personas, fecha, hora):
        self.id = Reserva.ReservaID
        self.nombre_cliente = nombre_cliente
        self.numero_personas = numero_personas
        self.fecha = fecha
        self.hora = hora
        Reserva.ReservaID += 1
    
    def __str__(self):
        string = f"ID: {self.id} - Cliente: {self.nombre_cliente} - Personas: {self.numero_personas} - Fecha: {self.fecha} - Hora: {self.hora}"
        return string

    def to_dict(self):
        diccionario = {"id": self.id, "nombre_cliente": self.nombre_cliente, 
                       "numero_personas": self.numero_personas, "fecha": self.fecha, "hora": self.hora}
        return diccionario




class Restaurante:
    def __init__(self):
        self.reservas = []

    def guardar_reservas(self):
        with open('reservas.json', 'w') as file: 
            data = [reserva.to_dict() for reserva in self.reservas]
            json.dump(data, file)

    def cargar_reservas(self):
        with open('reservas.json', 'r') as file:
            data = json.load(file)
            for reserva_data in data:
                reserva = Reserva(reserva_data['nombre_cliente'], reserva_data['numero_personas'],
                                    reserva_data['fecha'], reserva_data['hora']) 
                self.reservas.append(reserva)

    def agregar_reserva(self, reserva):
        for elemento in self.reservas:
            self.reservas.append(reserva)
            self.guardar_reservas()

    def listar_reservas(self):
        for reserva in self.reservas:
            print(reserva)

def menu():
    restaurante = Restaurante()
    while True:
        os.system("cls")
        print("----- Menú -----")
        print("1. Agregar reserva")
        print("2. Listar reservas")
        print("3. Cancelar reserva")
        print("4. Salir")
        opcion = input("Ingrese el número de la opción que desea: ")

        if opcion == "1":
            nombre_cliente = input("Ingrese el nombre del cliente: ")
            numero_personas = int(input("Ingrese el número de personas para la reserva: "))
            fecha = input("Ingrese la fecha de la reserva (DD/MM/YYYY): ")
            hora = input("Ingrese la hora de la reserva (HH): ")
            reserva_nueva = Reserva(nombre_cliente, numero_personas, fecha, hora)
            restaurante.agregar_reserva(reserva_nueva)
            input("\nReserva agregada correctamente. Presione ENTER para continuar.")

        elif opcion == "2":
            print("\n----- Listado de Reservas -----")
            restaurante.listar_reservas()
            input("\nPresione ENTER para continuar.")

        elif opcion == "3":
            reserva_id = int(input("Ingrese el ID de la reserva que desea cancelar: "))
            input("\nPresione ENTER para continuar.")

        elif opcion == "4":
            print("Programa finalizado.")
            break

menu()
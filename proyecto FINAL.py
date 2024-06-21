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




        

class Restaurante:
    def __init__(self):
        self.reservas = []




def menu():
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

        elif opcion == "2":
            print("\n----- Listado de Reservas -----")

        elif opcion == "4":
            print("Programa finalizado.")
            break

menu()
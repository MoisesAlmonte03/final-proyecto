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

def menu():
    while True:
        print("----- Menú -----")
        print("1. Agregar reserva")
        print("2. Listar reservas")
        print("3. Cancelar reserva")
        print("4. Salir")
        opcion = input("Ingrese el número de la opción que desea: ")
        if opcion == "4":
            print("Programa finalizado.")
            break

menu()
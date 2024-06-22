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
        self.cargar_reservas()

    def guardar_reservas(self):
        with open('reservas.json', 'w') as file: 
            data = [reserva.to_dict() for reserva in self.reservas]
            json.dump(data, file)

    def cargar_reservas(self):
        try:
            with open('reservas.json', 'r') as file:
                data = json.load(file)
                for reserva_data in data:
                    reserva = Reserva(reserva_data['nombre_cliente'], reserva_data['numero_personas'],
                                        reserva_data['fecha'], reserva_data['hora']) 
                    self.reservas.append(reserva)
        except FileNotFoundError:
            self.guardar_reservas()

    def agregar_reserva(self, reserva):
        for elemento in self.reservas:
            if elemento.fecha == reserva.fecha and elemento.hora == reserva.hora:
                raise ValueError("Esta reserva está en conflicto con una con esta fecha y hora. Favor elegir datos diferentes.")
        self.reservas.append(reserva)
        self.guardar_reservas()

    def listar_reservas(self):
        for reserva in self.reservas:
            print(reserva)

    def cancelar_reserva(self, reserva_id):
        for reserva in self.reservas:
            if reserva.id == reserva_id:
                self.reservas.remove(reserva)
                self.guardar_reservas()
                print(f"\nReserva ID {reserva_id} ha sido exitosamente cancelada.")
                return
        print(f"No hay ninguna reserva con ID {reserva_id}.")

def validar_fecha(fecha):
    try:
        dia, mes, anio = fecha.split('/')
        dia = int(dia)
        mes = int(mes)
        anio = int(anio)
        if not (1 <= dia <= 31 and 1 <= mes <= 12):
            raise ValueError("Día debe ser entre 1 y 31 y mes entre 1 y 12.")
    except ValueError:
        raise ValueError("Formato de fecha inválido. Debe ser DD/MM/YYYY.")

def validar_hora(hora):
    try:
        hora = int(hora)
        if not (0 <= hora <= 23):
            raise ValueError("Hora fuera de rango.")
    except ValueError:
        raise ValueError("Formato de hora inválido. Debe ser un número entero de 0 a 23.")

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
            try:
                nombre_cliente = input("Ingrese el nombre del cliente: ")
                numero_personas = int(input("Ingrese el número de personas para la reserva: "))
                fecha = input("Ingrese la fecha de la reserva (DD/MM/YYYY): ")
                validar_fecha(fecha)
                hora = input("Ingrese la hora de la reserva (HH): ")
                validar_hora(hora)
                reserva_nueva = Reserva(nombre_cliente, numero_personas, fecha, hora)
                restaurante.agregar_reserva(reserva_nueva)
                input("\nReserva agregada correctamente. Presione ENTER para continuar.")
            except ValueError as error_uno:
                print(f"Error: {error_uno}")
                input("\nPresione ENTER para continuar.")
            except Exception as error_random:
                print(f"Error inesperado: {error_random}")
                input("\nPresione ENTER para continuar.")

        elif opcion == "2":
            print("\n----- Listado de Reservas -----")
            restaurante.listar_reservas()
            input("\nPresione ENTER para continuar.")

        elif opcion == "3":
            try:
                reserva_id = int(input("Ingrese el ID de la reserva que desea cancelar: "))
                restaurante.cancelar_reserva(reserva_id)
                input("\nPresione ENTER para continuar.")
            except ValueError:
                print("Debe ingresar un ID válido (número entero).")
                input("\nPresione ENTER para continuar.")

        elif opcion == "4":
            print("Programa finalizado.")
            break

        else:
            print("Opción inválida. Por favor, ingrese un número válido.")
            input("\nPresione ENTER para continuar.")

menu()
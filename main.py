"""
Um software em Python que implementa uma Fila de carros e uma Fila de drones.
"""

from Drone import Drone
from Carro import Carro
from FilaCarros import FilaCarros
from FilaDrones import FilaDrones

c1 = Carro("Chevrolet", "Camaro", "2")
c2 = Carro("Fiat", "Uno", "4")
c3 = Carro("Toyota", "Corolla", "4")

d1 = Drone("NaoSei", "Modelo1", "8")
d2 = Drone("SeiNao", "RTX", "6")
d3 = Drone("Drone111", "XLS", "12")

filaCarros = FilaCarros()
filaDrones = FilaDrones()

while True:
    menu = int(input("""
        MENU
        1. Adicionar Carro
        2. Remover Carro
        3. Adicionar Drone
        4. Remover Drone
        5. Imprimir fila de carros
        6. Imprimir fila de drones
        """))
    if menu == 1:
        marca = input("Marca do carro: ")
        modelo = input("Qual o modelo do carro: ")
        portas = input("Quantidade de portas: ")
        carro = Carro(marca, modelo, portas)
        filaCarros.add(carro)
    elif menu == 2:
        remCarro = ("Qual carro você deseja remover: ")
        filaCarros.remover()
    elif menu == 3:
        marca = input("Marca do drone: ")
        modelo = input("Qual o modelo do drone: ")
        qtdH = input("Quantidade de helices: ")
        drone = Carro(marca, modelo, qtdH)
        filaDrones.add(drone)
    elif menu == 4:
        remDrone = ("Qual drone você deseja remover: ")
        filaCarros.remover()
    elif menu == 5:
        filaCarros.imprimir()
    elif menu == 6:
        filaDrones.imprimir()
    SimNao = input("Você deseja continuar S/N: ")
    if SimNao == "S" or "s":
        continue
    else:
        break
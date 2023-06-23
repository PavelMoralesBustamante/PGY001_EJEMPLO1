from colorama import Style, Fore, Back
import numpy
import os
import msvcrt
import random

##############################
#DISEÑO
def printr(texto : str):
    print(f"{Fore.RED}{Style.BRIGHT}{texto}{Style.RESET_ALL}{Fore.RESET}")

def printv(texto : str):
    print(f"{Fore.GREEN}{Style.BRIGHT}{texto}{Style.RESET_ALL}{Fore.RESET}")

def printa(texto : str):
    print(f"{Fore.YELLOW}{Style.BRIGHT}{texto}{Style.RESET_ALL}{Fore.RESET}")

def limpiarpantalla():
    printa("<<Press any key to continue>>")
    msvcrt.getch()
    os.system("cls")

##############################
#OPERACIONES
def validarCodigo(codigo):
    pass

def guardar(codigo,titulo,autor,precio):
    pass

def buscar(codigo):
    pass

def certificadoCriticas(codigo):
    pass

def certificadoDetalles(codigo):
    pass
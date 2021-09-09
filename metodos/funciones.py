import sys
from math import *
from sympy import *
import numpy as np

def hello():
    print('hello world')
    
# ============================ REPLACE CHARACTERS ON STRING INI ===================
# reemplazar simbolos en la cadena de caracteres para poderse utilizar en el metodo simpson 1/3
def string_replace(string):
    replacements = {
        '^': '**',
    }

    for old, new in replacements.items():
        string = string.replace(old, new)

    return string
# ============================ REPLACE CHARACTERS ON STRING FIN ===================    

# ============================ SIMPSON 1/3 INI ===================
#SIMPSON 1/3
#@ n: numero de x
#@ a y b los intervalos de la integral
#@ f: La funcion a integrar
def simpson_13(a, b, n, f):
    # evaluar una funcion en x
    def fx(x, f):
        return eval(f)
    
    f = string_replace(f)
    # print(f)
    #calculamos h
    h = (b - a) / n
    #Inicializamos nuestra varible donde se almacenara las sumas
    suma = 0.0
    #hacemos un ciclo para ir sumando las areas
    for i in range(1, n):
        #calculamos la x
        #x = a - h + (2 * h * i)
        x = a + i * h
        # si es par se multiplica por 4
        if(i % 2 == 0):
            suma = suma + 2 * fx(x, f)
        #en caso contrario se multiplica por 2
        else:
            suma = suma + 4 * fx(x, f)
    #sumamos los el primer elemento y el ultimo
    suma = suma + fx(a, f) + fx(b, f)
    #Multiplicamos por h/3
    rest = suma * (h / 3)
    #Retornamos el resultado
    return rest
# ============================ SIMPSON 1/3 FIN ===================


# ============================ TRAPECIOS INI ===================
#TRAPECIOS

#Ingrese su parametro inicial
# a = 1
# #Ingrese su parametro final
# b = 2
# #Ingrese el numero de particiones
# m = 4
# f= "sin(2*pi*x)+x^2"
# funcion = 


def trapecios(func, a, b, m):
    func = sympify(func)
    h = (b-a)/float(m)
    s = 0
    n = 0
    a_evaluado = 0
    b_evaluado = 0

    for i in range(1,m):
        n = a + (i*h)
        n_evaluado = func.evalf(subs = {"x" : n}) #evalua n en la funcion descrita
        s = s + n_evaluado

    a_evaluado = func.evalf(subs = {"x" : a}) #evalua a en la funcion descrita, lo mismo con b en la siguiente linea
    b_evaluado = func.evalf(subs = {"x" : b})
    result = h/2 * (a_evaluado + 2*s + b_evaluado)

    return result


# print(trapecios(funcion,a,b,m) )  #el primer parametro debe ser la funcion en expresion literal
# ============================ TRAPECIOS 3/8 FIN ===================
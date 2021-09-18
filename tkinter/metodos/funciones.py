import sys
from math import *
import numpy as np
from numpy import log as ln


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
    print(rest)
    return rest
# ============================ SIMPSON 1/3 FIN ===================


# ============================ TRAPECIOS INI ===================
# metodo trapecios
def trapecios(func, a, b, m):

    def funcx(x, f):
          return eval(f)

    func = string_replace(func)

    print(func)
    h = (b-a)/float(m)
    s = 0
    n = 0
    a_evaluado = 0
    b_evaluado = 0

    for i in range(1,m):
        n = a + (i*h)
        n_evaluado = funcx(n, func) #evalua n en la funcion descrita
        s = s + n_evaluado

    a_evaluado = funcx(a, func) #evalua a en la funcion descrita, lo mismo con b en la siguiente linea
    b_evaluado = funcx(b, func)
    result = h/2 * (a_evaluado + 2*s + b_evaluado)

    return result
# ============================ TRAPECIOS FIN ===================


# ============================ BISECCION  INI ===================
def bisection(f,a,b,N):
  def fx(x,f):
    return eval(f)

  f = string_replace(f)

  if fx(a,f)*fx(b,f) >= 0:
      print("Bisection method fails.")      
      return None
  a_n = a
  b_n = b
  for n in range(1,N+1):
      m_n = (a_n + b_n)/2
      f_m_n = fx(m_n,f)
      if fx(a_n,f)*f_m_n < 0:
          a_n = a_n
          b_n = m_n
      elif fx(b_n, f)*f_m_n < 0:
          a_n = m_n
          b_n = b_n
      elif f_m_n == 0:
          print("Found exact solution.")
          print(m_n)
          return m_n
      else:
          print("Bisection method fails.")
          return None
  return (a_n + b_n)/2
# ============================ BISECCION  FIN ===================


# ============================ SIMPSON 3/8  INI ===================
def simpson_38(f,x0,xf,n):
  def fx(x,f):
    return eval(f)

  f = string_replace(f)

  # Integracion mediante Simpson 3/8
  n = n - n%3 # truncar al multiplo de 3 mas cercano
  if n<=0:
    n = 1
  h = (xf-x0)/n
  x = x0
  suma = 0
  for j in range(n//3):
    suma += fx(x, f) + 3.*fx(x+h, f) + 3.*fx(x+2*h, f) + fx(x+3*h, f)
    x += 3*h
    r=(3.*h/8)*suma
  return r
# ============================ SIMPSON 3/8  FIN ===================


# ============================ FALSA POSICION INI ===================
def falsa_posicion(f,a,b,tolera):
  def fx(x,f):
    return eval(f)

  f = string_replace(f)

  tramo = abs(b-a)
  while not(tramo<=tolera):
      fa = fx(a,f)
      fb = fx(b,f)
      c = b - fb*(a-b)/(fa-fb)
      fc = fx(c,f)
      cambia = np.sign(fa)*np.sign(fc)
      if (cambia > 0):
          tramo = abs(c-a)
          a = c
      else:
          tramo = abs(b-c)
          b = c
  raiz = c
  return raiz
# ============================ FALSA POSICIOM FIN ===================


# ============================ NEWTON-RAPHSON INI ===================
def newton_raphson(f,df,x0,tolera):
  def fx(x, f):
    return eval(f)

  def dfx(x, df):
    return eval(df)
  
  f = string_replace(f)
  df = string_replace(df)

  tabla = []
  tramo = abs(2*tolera)
  xi = x0
  while (tramo>=tolera):
      fxi =  fx(xi, f)
      dfxi = dfx(xi,df)
      xnuevo = xi - fxi/dfxi
      tramo  = abs(xnuevo-xi)
      tabla.append([xi,xnuevo,tramo])
      xi = xnuevo

  # convierte la lista a un arreglo.
  tabla = np.array(tabla)
  n = len(tabla)

  return ("raiz",xi,"con error de", tramo)
# ============================ NEWTON-RAPHSON FIN ===================


# ================================ SECANTE INI =========================
def secante(f, xa, tolera):
  # evaluar funcion en x
  def fx(x, f):
    return eval(f)

  # tabla secante
  def secante_tabla(f,xa,tolera):
    dx = 4*tolera
    xb = xa + dx
    tramo = dx
    tabla = []
    while (tramo>=tolera):
        fa = fx(xa, f)
        fb = fx(xb, f)
        xc = xa - fa*(xb-xa)/(fb-fa)
        tramo = abs(xc-xa)
        
        tabla.append([xa,xb,xc,tramo])
        xb = xa
        xa = xc

    tabla = np.array(tabla)
    return (tabla)

  # reemplazar caracteres en la funcion...
  f = string_replace(f)

  tabla = secante_tabla(f,xa,tolera)
  n = len(tabla)
  raiz = tabla[n-1,2]

  np.set_printoptions(precision=4)
  # print('[xa ,\t xb , \t xc , \t tramo]')
  # for i in range(0,n,1):
  #     print(tabla[i])

  return ("raiz en: ", raiz)
# ================================ SECANTE FIN =========================


# ================================ PUNTO FIJO INI =========================
def punto_fijo(func,  approx, tol, n):
  def fx(x, f):
    return eval(f)

  func = string_replace(func)

  for i in range(0, n):
      p = fx(approx, func)
      if abs(p-approx) < tol:
          return p
      approx = p
  return "Method failed after {} iterations".format(n)
# ================================ PUNTO FIJO FIN =========================


# ================================ TIPOS DE ERRORES INI =========================
def error_verdadero(valor_verdadero,valor_aproximado):
  return ("El error verdadero es : ",valor_verdadero-valor_aproximado )

def error_relativo(valor_real,valor_aproximado):
  valor_absoluto= valor_real-valor_aproximado
  return ("El error relativo es : ",valor_absoluto/valor_real)

def error_aproximado(aproxi_anterior,aproxi):
  return ("El error de aproximación es : ",((aproxi-aproxi_anterior)/aproxi)*100)
# ================================ TIPOS DE ERRORES FIN =========================
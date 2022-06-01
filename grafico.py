from matplotlib.pyplot import plot_date, title
import sympy as sym
from sympy import symbols, plot_implicit, And
from sympy.plotting import plot

#VARIABLES
x, y = symbols('x, y') #Declaramos las variables X,Y
diccionario = {} #Este diccionario lo utilizaremos para guardar los maximos o Minimos (Depende el caso)
lista = [] #La lista nos ayudara a organizar los maximos y minimos para los ejercicios 6 en adelante


#VARIABLES CON FUNCIONES
primer_ejercicio = y < (5-2*x)
segundo_ejercicio = y <= 5

tercer_ejercicio = 2*(2*x-y)<2*(x+y)-4 


#Funciones Para ejercicios de MAXIMOS Y MINIMOS
#Funcion del Ejercicio 6
def primerFuncionMaximos(x,y):
    p = 4*x+6*y     #Evaluamos los puntos en la funcion P(x,y)
    diccionario[p]= (x,y) #Guardamos el resultado y los valores x,y
    text = "x: "+str(x)+" y: "+str(y) #realizamos un texto para el usuario
    return text #retornamos el texto

#Funciones Para ejercicios de MAXIMOS Y MINIMOS
#Funcion del Ejercicio 6
def segundaFuncionMaximos(x,y):
    z = 200*x+100*y     #Evaluamos los puntos en la funcion Z(x,y)
    diccionario[z]= (x,y) #Guardamos el resultado y los valores x,y
    text = "x: "+str(x)+" y: "+str(y) #realizamos un texto para el usuario
    return text #retornamos el texto

def terceraFuncionMaximos(x,y):
    z =  45000*x + 56000*y    #Evaluamos los puntos en la funcion Z(x,y)
    
    diccionario[z]= (x,y) #Guardamos el resultado y los valores x,y
    text = "x: "+str(x)+" y: "+str(y) #realizamos un texto para el usuario
    return text #retornamos el texto

def cuartaFuncionMaximos(x,y):
    z =  80*x + 60*y    #Evaluamos los puntos en la funcion Z(x,y)
    
    diccionario[z]= (x,y) #Guardamos el resultado y los valores x,y
    text = "x: "+str(x)+" y: "+str(y) #realizamos un texto para el usuario
    return text #retornamos el texto

#Ejercicio de graficar Sistemas de Ecuaciones
print("EJERCICIO 1.\nGrafica y < 5-2x")
plot_implicit(primer_ejercicio, (x,-10,10), (y,-10,10),title = 'Grafica y < 5-2x')#Obtenemos la region a estudiar plot_implicit(function,(range))

print("\n\nEJERCICIO 2.\nGrafica y <= 5")
plot_implicit(segundo_ejercicio, (x,-30,30), (y,-30,30),title = 'Grafica y <= 5')#Obtenemos la region a estudiar plot_implicit(function,(range))

print("\n\nEJERCICIO 3.\nGrafica 2(2x-y)<2(x+y)-4")
plot_implicit(tercer_ejercicio, (x,-8,8), (y,-8,8),title = 'Grafica 2(2x-y)<2(x+y)-4') #Obtenemos la region a estudiar plot_implicit(function,(range))

print("\n\nEJERCICIO 4.\nGrafica: \n  2x+y > 3\n  2y-1 > 0\n  x>=y")
plot_implicit(And(2*x+y > 3, 2*y - 1 > 0, x>=y), (x,-10,10), (y,-10,10),title = 'Grafica: \n  2x+y > 3\n  2y-1 > 0\n  x>=y')#Obtenemos la region a estudiar plot_implicit(And(function,function,...),(range))

print("\n\nEJERCICIO 5.\nGrafica: \n  2x+3y <= 60\n  x >= 0\n  y >= 0")
plot_implicit(And((2*x+3*y)<=60, x >= 0, y >= 0), (x,-40,40), (y,-40,40),title='Grafica: \n  2x+3y <= 60\n  x >= 0\n  y >= 0')#Obtenemos la region a estudiar plot_implicit(And(function,function,...),(range))



#MAXIMIZAR Y MINIMIZAR UNA FUNCION SUJETA A RESTRICCIONES
#EJERCICIO 6
print("\n\nEJERCICIO 6.\nMaximizar La Funcion sujeta a Las siguientes Restricciones:")
print("Max. P = 4x + 6y\n     S.A : 2X+Y<=180\n           x+2y<=160\n           x+y<=100\n           x>=0\n           y>=0")
print("Primero Dibujamos las rectas de las Restricciones:\n   2x+y-180=0\n   x+2y-160=0\n   x+y-100=0\n   x=0\n   y=0")
plot(180-2*x,(160-x)/2,100-x,0,(x,-100,100),title ='Max. P = 4x + 6y' ) #Graficamos todas las rectas igualadas a Y plot(function,function,...,(range))
print("Ahora solo escojemos la zona de estudio que es la siguiente:\n")

#el sym.solve nos ayuda a resolver ecuaciones igualadas a 0
inter_1 = sym.solve([2*x+y-180, x+y-100], dict=True)
inter_2 = sym.solve([x+2*y-160, x+y-100], dict=True)
inter_3 = sym.solve([2*x+y-180, y+0], dict=True)
inter_4 = sym.solve([x+0, y+0], dict=True)
inter_5 = sym.solve([x+2*y-160, x+0], dict=True)
print("Los puntos extremos son los siguientes:\n")
print("1:"+primerFuncionMaximos(inter_1[0][x],inter_1[0][y])+"\n2:"+primerFuncionMaximos(inter_2[0][x],inter_2[0][y])+"\n3:"+primerFuncionMaximos(inter_3[0][x],inter_3[0][y])+"\n4:"+primerFuncionMaximos(inter_4[0][x],inter_4[0][y])+"\n5:"+primerFuncionMaximos(inter_5[0][x],inter_5[0][y]))
for i in diccionario.keys(): #añadimos las llaves de los diccionarios a la lista
    lista.append(i)
lista.sort()    #organizamos la lista de menor a mayor
valores = diccionario[lista[-1]]    #obtenemos la tupla del Maximo en el diccionario
print("El maximo absoluto es el punto (x: "+str(valores[0])+" y: "+str(valores[1])+")\n ya que evaluados en la funcion P da como valor maximo : "+str(lista[-1]))

#MAXIMIZAR  UNA FUNCION APLICATIVA SUJETA A RESTRICCIONES
#EJERCICIO 7

print("\n\nEJERCICIO 7.\nMaximizar La Funcion sujeta a Las siguientes Restricciones:")
print("Max. P = 200x + 100y\n     S.A : 5x+3y<=105\n           2x+4y<=70\n           x>=0\n           y>=0")
print("Primero Dibujamos las rectas de las Restricciones:\n   5x+3y-105=0\n   2x+4y-70=0\n     x=0\n   y=0")
plot((105-5*x)/3,(70-2*x)/4,0,(x,-100,100),title = 'Max. P = 200x + 100y') #Graficamos todas las rectas igualadas a Y plot(function,function,...,(range))
print("Ahora solo escojemos la zona de estudio que es la siguiente:\n")

#el sym.solve nos ayuda a resolver ecuaciones igualadas a 0
inter_1 = sym.solve([5*x+3*y-105, 2*x+4*y-70], dict=True)

inter_2 = sym.solve([5*x+3*y-105, y+0], dict=True)
inter_3 = sym.solve([x+0, y+0], dict=True)
inter_4 = sym.solve([2*x+4*y-70, x+0], dict=True)
print("Los puntos extremos son los siguientes:\n")
print("1:"+segundaFuncionMaximos(inter_1[0][x],inter_1[0][y])+"\n2:"+segundaFuncionMaximos(inter_2[0][x],inter_2[0][y])+"\n3:"+segundaFuncionMaximos(inter_3[0][x],inter_3[0][y])+"\n4:"+segundaFuncionMaximos(inter_4[0][x],inter_4[0][y]))
for i in diccionario.keys(): #añadimos las llaves de los diccionarios a la lista
    lista.append(i)
lista.sort()    #organizamos la lista de menor a mayor
valores = diccionario[lista[-1]]    #obtenemos la tupla del Maximo en el diccionario
print("El maximo absoluto es el punto (x: "+str(valores[0])+" y: "+str(valores[1])+")\n Es decir que el numero de articulos X que se deben fabricar es de "+str(valores[0])+" y el numero de articulos que Y que se deben fabricar es de "+str(valores[1])+"  \n Teniendo en cuenta que al evaluar el maximo en los puntos descritos tenemos una utilidad maximizada de: "+str(lista[-1]))

#EJERCICIO 8 
# EJEMPLO CREADO "MAXIMIZAR LA FUNCION SUJETA A LAS RESTRICCIONES"
print("\n\nEJERCICIO 8.\nMaximizar La Funcion sujeta a Las siguientes Restricciones:")
print("Max. P = 45000x + 56000y\n     S.A : 4x+2y<=70\n           2x+4y<=58\n          x,y>=0 ")
print("Primero Dibujamos las rectas de las Restricciones:\n   4x+2y-70=0\n    2x+4y-58=0\n  ")
plot((70-4*x)/2, (58-2*x)/4, (x,-100,100),title='Max. P = 45000x + 56000y')#Graficamos todas las rectas igualadas a Y plot(function,function,...,(range))

print("Ahora solo escojemos la zona de estudio que es la siguiente:\n")


diccionario={}
lista=[]
#el sym.solve nos ayuda a resolver ecuaciones igualadas a 0
inter_1 = sym.solve([4*x+2*y-70, 2*x+4*y-58], dict=True)
inter_2 = sym.solve([x+0, y+0], dict=True)
inter_3 = sym.solve([4*x+2*y-70, y+0], dict=True)
inter_4 = sym.solve([ 2*x+4*y-58, x+0], dict=True)
print("Los puntos extremos son los siguientes:\n")
print("1:"+terceraFuncionMaximos(inter_1[0][x],inter_1[0][y])+"\n2:"+terceraFuncionMaximos(inter_2[0][x],inter_2[0][y])+"\n3:"+terceraFuncionMaximos(inter_3[0][x],inter_3[0][y])+"\n4:"+terceraFuncionMaximos(inter_4[0][x],inter_4[0][y]))
for i in diccionario.keys(): #añadimos las llaves de los diccionarios a la lista
    lista.append(i)
lista.sort()    #organizamos la lista de menor a mayor
valores = diccionario[lista[-1]]    #obtenemos la tupla del Maximo en el diccionario
print("El maximo absoluto es el punto (x: "+str(valores[0])+" y: "+str(valores[1])+")\n ya que evaluados en la funcion P da como valor maximo : "+str(lista[-1]))



#EJERCICIO 9 
# EJEMPLO CREADO "MINIMIZAR LA FUNCION SUJETA A LAS RESTRICCIONES"
print("\n\nEJERCICIO 8.\nMinimizar La Funcion sujeta a Las siguientes Restricciones:")
print("Min. P = 80*x +60y\n     S.A : 20x+32y<=25\n           x+y=1\n           x,y>=0")
print("Primero Dibujamos las rectas de las Restricciones:\n   20x+32y-25=0\n   x+y-1=0\n   ")
plot((25-20*x)/32, 1-x,  (x,-3,3),title='Min. P = 80*x +60y') #Graficamos todas las rectas igualadas a Y plot(function,function,...,(range))
print("Ahora solo escojemos la zona de estudio que es la siguiente:\n")


diccionario={}
lista=[]
#el sym.solve nos ayuda a resolver ecuaciones igualadas a 0
inter_1 = sym.solve([20*x+32*y-25, x+y-1], dict=True)
inter_2 = sym.solve([20*x+32*y-25, y+0], dict=True)
inter_3 = sym.solve([x+y-1, x+0], dict=True)
print("Los puntos extremos son los siguientes:\n")
print("1:"+cuartaFuncionMaximos(inter_1[0][x],inter_1[0][y])+"\n2:"+cuartaFuncionMaximos(inter_2[0][x],inter_2[0][y])+"\n3:"+cuartaFuncionMaximos(inter_3[0][x],inter_3[0][y]))
for i in diccionario.keys(): #añadimos las llaves de los diccionarios a la lista
    lista.append(i)
lista.sort()    #organizamos la lista de menor a mayor
valores = diccionario[lista[1]]    #obtenemos la tupla del minimo en el diccionario
print("El minimo absoluto es el punto (x: "+str(valores[0])+" y: "+str(valores[1])+")\n ya que evaluados en la funcion P da como valor minimo : "+str(lista[1]))

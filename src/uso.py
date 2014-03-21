#!/src/bin/python
import modulo  

def mostrar(lista):
  print 'i   PI35DT   lista   i   PI35DT - lista i'
  for l in lista:
    diff= modulo.PI - l
    print '%d   %.10f   %.10f   %.10f' %(u, modulo.PI, l, abs(diff))

t_upla_valores=(1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7)
lista=[]

for i in t_upla_valores:
  y=modulo.aproximacion(i)
  lista=lista+[y]
  
mostrar(lista)

# Al ejecutar el programa vemos que el numero maximo de elementos de la t_upla es 7.
# Se producen errores de memoria en el elemento 100000000.
#Hemos probado a definir los elementos con notacion cientifica y el programa se ejecuta.
# La expresion .pyc es el acronimo de "Compiled Python script file".
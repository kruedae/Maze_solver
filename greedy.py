import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl


def read_matrix(path):
  file = open(path)
  # type(file)
  csv_reader = csv.reader(file) 
  
  # header = next(csv_reader) 
  # print(header)
  
  nr = 0
  nc = 0
  
  rows = []
   
  for row in csv_reader:
    w = len(row)
    if w > 0: 
      rows.append(row) 
      if w > nc:
        nc = w
  
  nr = len(rows)
  
  dims = (nr, nc) 
  
  print('dims:')
  print(dims) 
    
  file.close()
  
  binM = np.zeros(dims)
  
  
  for i in range(nr):
    for j in range(nc):
      if rows[i][j]=='c':
      	binM[i][j]=1

  return binM
#Finaliza read_matrix

def encontrarInicio(maze):
  posJ=1
  while(maze[0][posJ]==0):
    posJ+=1
  return posJ

def encontrarFinal(maze):
  (nFilas,nColumnas)=np.shape(M)
  posJ=nColumnas-1
  while(maze[0][posJ]==0):
    posJ-=1
  return posJ

def heuristica(finalI,finalJ,posicion):
  return abs(finalI-posicion[0])+abs(finalJ-posicion[1])

"""
def agregarPorHeuristica(finalI,finalJ,lista,nuevo):
  print(lista[lista.size//2-1])
  if heuristica(finalI,finalJ,lista[lista.size//2-1])<=heuristica(finalI,finalJ,nuevo):
    nueva_lista=np.append(lista,[nuevo],0)
  else:
    i=0
    search=True
    while(search):
      if heuristica(finalI,finalJ,nuevo)<heuristica(finalI,finalJ,lista[i]):
        nueva_lista=np.insert(lista,i,[nuevo],0)
        search=False
      else:
        print(i)
        i+=1
  return nueva_lista
"""

def calcular_vecinos(maze,posI,posJ):
  parejas=[]  
  (nFilas,nColumnas)=np.shape(maze)
  finalJ=encontrarFinal(maze)

  if(maze[posI][posJ-1]==1):
      parejas.append(np.array([posI,posJ-1]))
  
  if(maze[posI][posJ+1]==1):
    if finalJ<posJ:   
      # izquierda mejor que derecha      
      parejas.append(np.array([posI,posJ+1]))    
    else:
      # derecha mejor que izquierda   
      parejas.insert(0,np.array([posI,posJ+1]))
  if(maze[posI-1][posJ]==1):
    # abajo lo ultimo  
    parejas.append(np.array([posI-1,posJ]))
  if(maze[posI+1][posJ]==1):
    # arriba lo primero
    parejas.insert(0,np.array([posI+1,posJ]))
  return(parejas)
  


def agregarPorHeuristicaCaminos(finalI,finalJ,caminos,nuevo_camino):
    
  nuevo=nuevo_camino[0]
  
  camino=caminos[len(caminos)-1]
  
  #print(nuevo)
  #print(camino)

  
  if heuristica(finalI,finalJ,camino[0])<=heuristica(finalI,finalJ,nuevo):
    caminos.append(nuevo_camino)
  else:
    i=0
    search=True
    while(search):
      camino=caminos[i]
      if heuristica(finalI,finalJ,nuevo)<heuristica(finalI,finalJ,camino[0]):
        caminos.insert(i,nuevo_camino)
        search=False
      else:
        print(i)
        i+=1
  return caminos

# Finaliza agregarPorHeuristicaCaminos
  
def algoritmoGreedy(M):
  maze = M.copy()
  
  posiblesCaminos=[np.array([[0,encontrarInicio(maze)]])]
  
  agregarPorHeuristicaCaminos(finalI,finalJ,caminos,nuevo_camino)
  
  buscando=True
  
  while(buscando):
    mejor_camino=posiblesCaminos[0]
    ultimo_paso=mejor_camino.pop(0)
    #Actualizar los caminos
      vecinos=calcular_vecinos(maze,ultimo_paso[0],ultimo_paso[1])
      if vecinos!=[]:
        for v in vecinos:
          nuevo_camino=mejor_camino.insert(0,v)
        
  


def fmain():

  #print("Ingresar nombre del archivo csv:")
  #string = input()
  
  #ruta = "maze-examples/" + string + ".csv"
   
  #M = read_matrix(ruta)

  #(nFilas,nColumnas)=np.shape(M)
   
  #print(heuristica(5,4,np.array([1,2])))
   
  #print("agregarPorHeuristica")
  
  #print(agregarPorHeuristica(5,4,lista,np.array([5,3])))
  
  listaCaminos=[np.array([[1,4],[1,3]]),np.array([[1,4],[1,4],[1,4]]),np.array([[1,4],[2,3],[1,2],[0,1]])]
  
  #print("Caminos")
  #print(listaCaminos)
  #print(len(listaCaminos))
  
  print("Prueba caminos")
  
  print(agregarPorHeuristicaCaminos(5,4,listaCaminos,np.array([[2,2],[1,3]])))
  
  

# end fmain


# run program

fmain()


import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from funciones import *
import time

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
  
  #print('dims:')
  #print(dims) 
  
  #print(rows) 
  
  
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

def posiblesMovimientos(maze,posI,posJ):
  return np.array([  maze[posI+1][posJ]  , maze[posI][posJ+1] , maze[posI-1][posJ]  , maze[posI][posJ-1] ])
#Finaliza posiblesMovimientos

def realizarMovimientoI(opcion,posI):
  newposI=posI
  if(opcion==0):
    newposI+=1
  elif(opcion==2):
    newposI-=1
  return newposI
#Finaliza realizarMovimientoI(Y)

def realizarMovimientoJ(opcion,posJ):  
  newposJ=posJ
  if(opcion==1):
    newposJ+=1
  elif(opcion==3):
    newposJ-=1
  return newposJ
#Finaliza realizarMovimientoJ(X)

def no_regresar(opcion):
  if(opcion==0):
    lista=np.array([0,1,3])
  elif(opcion==1):
    lista=np.array([0,1,2])
  elif(opcion==2):
    lista=np.array([1,2,3])
  elif(opcion==3):
    lista=np.array([0,2,3])
  return lista
 #Finaliza no_regresar


def algoritmoProfundidad(M):
  maze = M.copy()
  (nFilas,nColumnas)=np.shape(maze)
  
  posI=0
  posJ=encontrarInicio(maze)
 
  if(maze[1][posJ]==1):
    opcion=0    
  elif(maze[0][posJ+1]==1):
    opcion=1
  else:
    opcion=3
  posI=realizarMovimientoI(opcion,posI)
  posJ=realizarMovimientoJ(opcion,posJ)
   
  pasos=[opcion]
  #print(pasos)
  
  posibles=posiblesMovimientos(maze,posI,posJ)
  
  opciones=no_regresar(opcion)
  
  while(not(posI==nFilas-1)):
    #print(pasos)
    posibles=posiblesMovimientos(maze,posI,posJ)
    
    trys=0
    
    opcion=opciones[0]
    search=(posibles[opcion]==0)
    while(trys+1<3 and search):     
      if(search):              
        trys+=1        
        opcion=opciones[trys]
        search=(posibles[opcion]==0)
    if(search):
      maze[posI][posJ]=0
      opcion=pasos[-1]
      regresar=(opcion+2)%4
      posI=realizarMovimientoI(regresar,posI)
      posJ=realizarMovimientoJ(regresar,posJ)
      pasos=pasos[np.arange(pasos.size - 1)]
    else:
      posI=realizarMovimientoI(opcion,posI)
      posJ=realizarMovimientoJ(opcion,posJ)
      pasos=np.append(pasos,opcion)
    opciones=no_regresar(pasos[-1])   
  return pasos
    
  #Finaliza algoritmo Profundidad
  
def profundidad_pasos_01(pasos):
  pasos01=[]
  for paso in pasos:
    if paso==0:
      pasos01.append([1,0])
    elif paso==1:
      pasos01.append([0,1])
    elif paso==2:
      pasos01.append([-1,0])
    elif paso==3:
      pasos01.append([0,-1])  
  return pasos01
  
def posiciones_camino_profundidad(pasos,inicioJ):
  posI=0
  posJ=inicioJ
  posiciones=np.array([[0,inicioJ]])
  for paso in pasos:
    posI=realizarMovimientoI(paso,posI)
    posJ=realizarMovimientoJ(paso,posJ)
    posiciones=np.append(posiciones,[[posI,posJ]],0)
  return posiciones
  #Finaliza posiciones_camino_profundidad


  
def colorear_pasos(maze,pasos):
  (nFilas,nColumnas)=np.shape(maze)
  camino = np.zeros((3*nFilas,3*nColumnas))
  
  for posI in range(0,nFilas):
    for posJ in range(0,nColumnas):
      if maze[posI][posJ]==1:
        for i in range(0,3):
          for j in range(0,3):
            camino[3*posI+i][3*posJ+j]=1  
            
  posI=0
  posJ=encontrarInicio(maze)
  camino[0][3*posJ+1]=0.5
  camino[1][3*posJ+1]=0.5
  for paso in pasos:
    if paso<1.5:
      s=-1
    else:
      s=1
 
    posI=realizarMovimientoI(paso,posI)
    posJ=realizarMovimientoJ(paso,posJ)
    
    if paso%2==0:
      for k in range(0,3):
          camino[3*posI+s+k][3*posJ+1]=0.5        
    else:
      for k in range(0,3):
          camino[3*posI+1][3*posJ+s+k]=0.5  
                 
  camino[3*posI+2][3*posJ+1]=0.5
      
  return camino  
#Finaliza colorear_pasos

def main_profundidad(filename):

  #string = input()
  
  #ruta = "./" + string + ".csv"
 
  M = read_matrix(filename)
  maze = np.genfromtxt(filename, delimiter=',', dtype=str)

  #get the start time
  st = time.time()
  pasos=algoritmoProfundidad(M)
  # get the end time
  et = time.time()
  # get the execution time
  elapsed_time = et - st 
  
  
  animate_solution(maze, profundidad_pasos_01(pasos), 'profundidad')
  
  return elapsed_time 
  #print(posiciones_camino_profundidad(pasos,encontrarInicio(M)))
  #cmap = mpl.colors.ListedColormap(['#000000', '#ff2200', '#00ff00'])
  
  #plot1 = plt.figure("laberinto")
  #plt.imshow(M, cmap)

  #plot2 = plt.figure("recorrido")
  #plt.imshow(colorear_pasos(M,pasos), cmap)
  
  #plt.show()

  #plt.imshow(C)
  #plt.show()

# end fmain


# run program







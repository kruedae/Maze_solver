import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
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
  (nFilas,nColumnas)=np.shape(maze)
  posJ=nColumnas-1
  while(maze[nFilas-1][posJ]==0):
    posJ-=1
  return posJ

def heuristica(finalI,finalJ,posicion):
  return abs(finalI-posicion[0])+abs(finalJ-posicion[1])
  
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

def calcular_vecinos(finalJ,maze,posI,posJ):
  parejas=[]

  if(maze[posI][posJ-1]==1):
      parejas.append(np.array([posI,posJ-1]))
  
  if(maze[posI][posJ+1]==1):
    if finalJ<posJ:   
      # izquierda mejor que derecha      
      parejas.append(np.array([posI,posJ+1]))    
    else:
      # derecha mejor que izquierda   
      parejas.insert(0,np.array([posI,posJ+1]))
  
  if(posI!=0):
    if(maze[posI-1][posJ]==1):
      # abajo lo ultimo  
      parejas.append(np.array([posI-1,posJ]))
    
  if(maze[posI+1][posJ]==1):
    # arriba lo primero
    parejas.insert(0,np.array([posI+1,posJ]))
  return(parejas)
  


def agregarPorHeuristicaCaminos(finalI,finalJ,caminos,nuevo_camino):
  if(len(caminos)==0):
	  caminos.append(nuevo_camino)
  else:   
    #print("agregarPorHeuristicaCaminos")
    
    nuevo=nuevo_camino[0]
    
    #print(caminos)
    
    camino=caminos[len(caminos)-1]
    
    #print(camino)
    
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
          #print(i)
          i+=1
  return caminos

# Finaliza agregarPorHeuristicaCaminos
  
def algoritmoGreedy(M):
  maze = M.copy()
  (nFilas,nColumnas)=np.shape(maze)
  finalI=nFilas-1
  finalJ=encontrarFinal(maze)
  #print("finalJ")
  #print(finalJ)
  
  caminos=[np.array([[0,encontrarInicio(maze)]])]
  
  #agregarPorHeuristicaCaminos(finalI,finalJ,caminos,nuevo_camino)
  
  buscando=True
  
  #etapas=0
  while(buscando):
    #etapas+=1
    mejor_camino=caminos.pop(0)
    #print("mejor_camino")    
    #print(mejor_camino)
    ultimo_paso=mejor_camino[0]
    #print("ultimo_paso")    
    #print(ultimo_paso)
    #print("maze ult paso")
    #print(maze[ultimo_paso[0]][ultimo_paso[1]])
    maze[ultimo_paso[0]][ultimo_paso[1]]=0
    #Actualizar los caminos
    vecinos=calcular_vecinos(finalJ,maze,ultimo_paso[0],ultimo_paso[1])
    #print("vecinos")
    #print(vecinos)    
    if vecinos!=[]:
      for v in vecinos:
        if buscando:
          nuevo_camino=np.insert(mejor_camino,0,v,0)
          agregarPorHeuristicaCaminos(finalI,finalJ,caminos,nuevo_camino)
          if (v[0]==finalI and v[1]==finalJ):
            buscando=False
    maze[ultimo_paso[0]][ultimo_paso[1]]=0
    
    
  #print("Mejor camino Greedy:")
  #print(nuevo_camino)                      
  return nuevo_camino
          
  
def colorearGredy(camino_gredy,M):
  maze = M.copy()
  for cuadro in camino_gredy:
    maze[cuadro[0]][cuadro[1]]=0.5
  return maze

def caminoReverso_a_pasos(camino_reverso):
  pasos=[] 
  l=len(camino_reverso)-1
  for i in range(0,l):
    paso=camino_reverso[i]-camino_reverso[i+1]
    if(paso[0]==1 and paso[1]==0):
      pasos.insert(0,0)
    elif(paso[0]==-1 and paso[1]==0):
      pasos.insert(0,2)
    elif(paso[0]==0 and paso[1]==1):
      pasos.insert(0,1) 
    elif(paso[0]==0 and paso[1]==-1):
      pasos.insert(0,3)
  return pasos


def greedy_pasos_01(camino_reverso):
  pasos=[] 
  l=len(camino_reverso)-1
  for i in range(0,l):
    paso=camino_reverso[i]-camino_reverso[i+1]
    pasos.insert(0,[paso[0],paso[1]])
  return pasos


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


def greedy():

  print("Ingresar nombre del archivo csv:")
  string = input()
  
  ruta = "maze-examples/" + string + ".csv"
   
  M = read_matrix(ruta)

  #(nFilas,nColumnas)=np.shape(M)
   
  #print(heuristica(5,4,np.array([1,2])))
   
  #print("agregarPorHeuristica")
  
  #print(agregarPorHeuristica(5,4,lista,np.array([5,3])))
  
  #listaCaminos=[np.array([[1,4],[1,3]]),np.array([[1,4],[1,4],[1,4]]),np.array([[1,4],[2,3],[1,2],[0,1]])]
  
  #print("Caminos")
  #print(listaCaminos)
  #print(len(listaCaminos))
  
  #print("Prueba caminos")
  
  #print(agregarPorHeuristicaCaminos(5,4,listaCaminos,np.array([[2,2],[1,3]])))
  
  print("Greedy")
  
  #get the start time
  st = time.time()
  camino_gredy=algoritmoGreedy(M)
  # get the end time
  et = time.time()
  # get the execution time
  elapsed_time = et - st 
  
  print(elapsed_time)

  
  pasos=caminoReverso_a_pasos(camino_gredy)
  
  #print(pasos)
  
  #print(greedy_pasos_01(camino_gredy))
 
  cmap = mpl.colors.ListedColormap(['#000000', '#ff2200', '#00ff00'])
  
  plot1 = plt.figure("laberinto")
  plt.imshow(M, cmap)

  plot2 = plt.figure("recorrido")
  plt.imshow(colorear_pasos(M,pasos), cmap)
  
  plt.show()
  
  return elapsed_time

# end fmain


# run program

greedy()
    
 


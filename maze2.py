import csv
import numpy as np
import matplotlib.pyplot as plt


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
  
  #print(rows) 
  
  
  file.close()
  
  binM = np.zeros(dims)
  
  
  for i in range(nr):
    for j in range(nc):
      if rows[i][j]=='c':
      	binM[i][j]=1
  
  return binM

def posiblesMovimientos(maze,posX,posY):
  return np.array([  maze[posX][posY+1]  , maze[posX+1][posY] , maze[posX][posY-1]  , maze[posX-1][posY] ])
  
#def realizarMovimiento(opcion):
 # if(opcion)
  

def algoritmoProfundidad(M,dimX,dimY):
  maze = M.copy()
  posX=0
  posY=1
  if(maze[0][2]==1):
    opcion=0
    posY+=1 
  elif(maze[1][1]==1):
    opcion=1
    posX+=1
  else:
    opcion=2
    posX-=1
  
  print(opcion)
  
  pasos=[opcion]
  
  while(not(posX==dimX-1 and posY==dimY-2)):
    posibles=posiblesMovimientos(maze,posX,posY)
    
    #Si se queda sin opciones
    
    if(np.array_equal(posibles,np.zeros(4))):
      maze[posX,posY]=0
      pasos[np.arange(pasos.size - 1)]
    else:
      opcion=0
      while(posibles[opcion]==0):
        opcion=(opcion+1)%4
      np.append(pasos,opcion)
      print(opcion)
      
  print(pasos)
    
  
  
  

def fmain():
  print("Ingresar nombre del archivo csv:")
  string = input()
  
  ruta = "maze-examples/" + string + ".csv"
   
  M = read_matrix(ruta)
  C = M.copy()
  
  (nFilas,nColumnas)=np.shape(M)
  
  #algoritmoProfundidad(M,nFilas,nColumnas)
  
  #print(algoritmoProfundidad(M,nFilas,nColumnas))
      	  
  plt.imshow(M, cmap='gray')
  #plt.imshow(C)
  plt.show()
  
  

  #plt.imshow(C)
  #plt.show()

# end fmain


# run program

fmain()








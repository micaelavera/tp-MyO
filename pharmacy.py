from pyscipopt import Model
import numpy as np

model = Model("pharmacy")

drogas = []
cant_necesaria = []
remedios = []
passDrougs = False

#file = input("Ingrese el nombre del archivo y su extensión. Por ejemplo: input1.txt\n")
file = "farma03.in"

# try:
#     with open(file, 'r') as archivo:
#             lines = archivo.readlines()
#             passDrougs = False

#             for line in lines:
#                 if 'REMEDIOS' in line:
#                     passDrougs = True
#                 if not '#' in line and ':' in line and passDrougs == False and not 'DROGAS' in line:
#                     linea = line.rstrip('\n')
#                     split = linea.split(":")
#                     drogas.append(split[0])
#                     cant_necesaria.append(float(split[1].strip()))
#                 else:
#                      if not '#' in line and passDrougs == True and not 'REMEDIOS' in line:
#                         linea = line.rstrip('\n')
#                         split = linea.split(":")
#                         remedio = split[0]
#                         remedios.append(remedio)
#                         drougs = split[1].rstrip('\n')
#                         split2 = drougs.split(",")
#                         cantidades = np.zeros((len(remedios),len(drogas))).astype(int)
#                         for cantDroug in split2:
#                             linea3 = cantDroug.strip()
#                             split3 = linea3.split(" ")
#                             cantidades[remedios.index(remedio)][drogas.index(split3[0])]= float(split3[1])

                    
# except IOError:
#     print ("No existe el archivo", file)

# finally:
#     archivo.close()
try:
    with open(file, 'r') as archivo:
        lines = archivo.readlines()

        for line in lines:
            if 'REMEDIOS' in line:
               passDrougs=True
            if not '#' in line and ':' in line and passDrougs == False and not 'DROGAS' in line:
                linea = line.rstrip('\n')
                split = linea.split(":")
                drogas.append(split[0])
                cant_necesaria.append(float(split[1].strip()))
            else:
                if not '#' in line and passDrougs==True and not 'REMEDIOS' in line:
                    linea = line.rstrip('\n')
                    split = linea.split(":")
                    remedios.append(split[0])
			
                                
    archivo.close()   
except IOError:
    print ("No existe el archivo", file)

cantidades = np.empty((len(remedios),len(drogas)),float)

for j in range(len(remedios)):
   for i in range(len(drogas)): 
       cantidades[j][i]=0

passDrougs=False
try:
    with open(file, 'r') as archivo:
        lines = archivo.readlines()

        for line in lines:
            if 'REMEDIOS' in line:
               passDrougs=True
            if not '#' in line and passDrougs == True and not 'REMEDIOS' in line:
                    linea = line.rstrip('\n')
                    split = linea.split(":")
                    remedio=split[0]
                    linea2=split[1].rstrip('\n')
                    split2=linea2.split(",")
                    for remdrogacant in split2:
                        linea3 = remdrogacant.strip()
                        split3 = linea3.split(" ")
                        cantidades[remedios.index(remedio)][drogas.index(split3[0])]= float(split3[1])
                        
                    

    archivo.close()   
except IOError:
    print ("No existe el archivo", file)
    import sys
    sys.exit()

#### VARIABLES ####
# Remedios
r = {}
for i in range(len(remedios)):
    r[i] = model.addVar(vtype='C', name='%s'%(remedios[i]))

#### RESTRICCIONES ####
for j in range(len(drogas)):
  model.addCons(sum(r[t]*cantidades[t][j] for t in range(len(remedios))) >= cant_necesaria[j])       

for t in range(len(remedios)):
  model.addCons(r[t] >= 0)
 
#### FUNCIÓN OBJETIVO ####
model.setObjective(sum(r[i] for i in range(len(remedios))), "minimize")

model.hideOutput()
model.optimize()

print("\n******************************* SOLUCIÓN *******************************")
#print("Matriz de cantidades del remedio i y droga j\n")
#print(cantidades,"\n")

print ("{:<10} {:<20}".format('Remedio','Cantidad'))
for i in range(len(r)):
  print("{:<10} {:<20}".format(r[i].name, model.getVal(r[i])))

print("La cantidad de remedios distintos utilizados:", model.getObjVal())
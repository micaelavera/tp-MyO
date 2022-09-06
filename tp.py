from pyscipopt import Model, quicksum
import numpy as np

model = Model("tp")
#file = input("Ingrese el nombre del archivo y su extensión. Por ejemplo: input1.txt\n")
file = "input1.txt"

drogas = []
cant_necesaria = []

remedios = []
r_drogas = []
cantidades = []
tupla = [] 

try:
    with open(file, 'r') as archivo:
        lines = archivo.readlines()

        for line in lines:
            if not '#' in line and ':' in line:
                linea = line.rstrip('\n')
                split = linea.split(": ")
                drogas.append(int(split[0]))
                cant_necesaria.append(int(split[1]))
            else:
                if not '#' in line and line.strip():
                    linea = line.rstrip('\n')
                    split = linea.split(" ")
                    remedios.append(int(split[0]))
                    r_drogas.append(int(split[1]))
                    
                    A = np.array([int(split[0]), int(split[1]), int(split[2])]) 
                    tupla.append(A) 

                    
        cantidades = np.zeros((max(remedios),len(r_drogas)-1)).astype(int)

        for i in range(len(tupla)):
            cantidades[(tupla[i][0])-1][(tupla[i][1])-1] = tupla[i][2] # m remedios (filas) y n drogas (columnas)

    archivo.close()   
except IOError:
    print ("No existe el archivo", file)

#### VARIABLES ####
# Drogas
d = {}
for i in range(len(drogas)):
    d[i] = model.addVar(vtype='I')
    d[i] = drogas[i]

# Cantidad necesaria de la droga j
c = {}
for i in range(len(cant_necesaria)):
    c[i] = model.addVar(vtype='I')
    c[i] = cant_necesaria[i]

# Remedios
r = {}
for i in range(len(remedios)):
    r[i] = model.addVar(vtype='I', name='Remedio %d'%(i))
    r[i] = remedios[i]

#### RESTRICCIONES ####
#for j in range(len(d)):
 ##model.addCons(quicksum(cantidades[d[j]][r[t]] for t in range(len(r))) >= c[j-1])
        
#### FUNCIÓN OBJETIVO ####
model.setObjective(quicksum(r[i] for i in r), "minimize")

model.hideOutput()
model.optimize()

print("\n******************************* SOLUCIÓN *******************************")
print("Matriz de cantidades del remedio i y droga j")
print(cantidades)

print("Solución:", model.getObjVal()) 
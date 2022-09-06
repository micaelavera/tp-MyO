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



#def llenar_matriz(remedios, r_drogas):
 #   matriz[0][1] = 2
  #  return matriz

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

        matriz = np.zeros((max(remedios),len(r_drogas)-1)).astype(int)
                                   
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
    r[i] = model.addVar(vtype='I')
    r[i] = remedios[i]

# Droga en el remedio i
rd = {}
for i in range(len(r_drogas)):
    rd[i] = model.addVar(vtype='I')
    rd[i] = r_drogas[i]

# Cantidad de la droga en el remedio i
# x = {}
# for i in range(len(cantidades)):
#     x[i] = model.addVar(vtype='I')
#     x[i] = cantidades[i]


#### RESTRICCIONES ####
    #model.addCons(quicksum(d[j][i]*x[j] for j in F) == z[i], name="Nutr(%s)"%i)

#### FUNCIÓN OBJETIVO ####
model.setObjective(quicksum(r[i] for i in r), "minimize")

model.hideOutput()
model.optimize()

print("\n******************************* SOLUCIÓN *******************************")

print("Solución:", model.getObjVal()) 
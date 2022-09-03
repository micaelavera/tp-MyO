from pyscipopt import Model, quicksum

model = Model("tp")
#file = input("Ingrese el nombre del archivo y su extensión. Por ejemplo: input1.txt\n")

drogas = []
cant_necesaria = []

remedios = []
r_drogas = []
cantidades = []
archivo = open("input1.txt", 'r')
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
            cantidades.append(int(split[2]))
archivo.close()

print(drogas, cant_necesaria)
print(remedios, r_drogas, cantidades )
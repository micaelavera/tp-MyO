# Pharmacy-tp

Un paciente con una enfermedad de la que poco se conoce requiere un tratamiento especial.
Para eso se reunión un comité de médicos, químicos y biólogos; la recomendación es un cóctel de
drogas. Éste debe contener las drogas $d_1$, $d_2$, . . . , $d_n$, en cantidades $q_1$, $q_2$, . . . , $q_n$, respectivamente.
Desafortunadamente, la mayoría de estas drogas no se consigue por separado, y la propuesta es
que el paciente pueda obtenerlas tomando a través de otros remedios $r_1$, $r_2$, . . . , $r_m$. Se sabe que el
remedio $r_i$ contiene la droga $d_j$ en cantidad $k_{ij}$ . Para evitar interacciones innecesarias, se tratará 
de evitar combinar demasiados remedios. Dar un modelo que permita encontrar la menor cantidad
de remedios distintos que permitan cumplir con la cantidad de drogas necesarias.  
El input debe poder leerse de un archivo.

## Tecnologías y herramientas utilizadas
- Python 3.8
- [SCIP](https://scipopt.org/#scipoptsuite)
- PySCIPOpt

## Instalación

### Crear entorno virtual   
```
$ virtualenv env -p python3 
```

### Iniciar entorno virtual   
```
$ source env/bin/activate 
```
### Descargar SCIP
Descargar el _.sh_ de scip: https://www.scipopt.org/download.php?fname=SCIPOptSuite-8.0.1-Linux-ubuntu.sh e instalar.

### Instalar PySCIPOpt
```
$ pip install pyscipopt    
$ export SCIPOPTDIR=<path_to_scip_dir>
```

### Ejecutar proyecto
```
$ python3.8 pharmacy.py
```








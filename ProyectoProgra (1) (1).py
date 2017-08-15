
import random

#Creamos los tableros tanto logicos como el fisico
class Tablero:
    def __init__(self, pfila=0, pcolumna=0):

        self.fila = pfila
        self.columna = pcolumna
        self.tablero = []
        self.tablero1=[]
        self.tablero2=[]
        self.tablerologico1 = []
        self.tablerologico2 = []

#creamos tablero fisico y logicos
    def creatablerofi(self):

        for i in range(0, 5):
            self.tablero.append(["0"] * 5)
            self.tablero1.append(["0"] * 5)
            self.tablero2.append(["0"] * 5)

#creamos tableros logicos 2
    def creatablelogico(self):

        for i in range(0, 5):
            self.tablerologico1.append(["0"] * 5)
            self.tablerologico2.append(["0"]* 5)



#creamos la clase persona con datos generales
class Persona:
    def __init__(self,pNombre="",psexo=""):
        self.Nombre=pNombre
        self.Sexo=psexo

#creamos el metodo jugador usando las variables inicializadas anteriormente
    def Jugador(self):
        self.Nombre=""
        self.Sexo=""

#creamos la clase Barcos e inicializamos variables y creamos los barcos
class Barcos:

    def __init__(self,pNombre="",pmaterial="",pcantbarcos1=0,pcantbarcos2=0):

        self.Nombrebarco=pNombre
        self.Material=pmaterial
        self.CantBarco1=pcantbarcos1
        self.CantBarco2=pcantbarcos2
        self.Bomba=[]
        self.Lanza=[]
        self.Dest=[]
        self.Pesque=[]
        self.Bomba2 = []
        self.Lanza2 = []
        self.Dest2 = []
        self.Pesque2 = []



    def llenabarcos(self):

        for i in range(1):
            self.Bomba.append(['x']*5)
            self.Lanza.append(["x"]*5)
            self.Dest.append(["x"]*5)
            self.Pesque.append(["x"]*5)
            self.Bomba2.append(["x"]*5)
            self.Lanza2.append(["x"]*5)
            self.Dest2.append(["x"]*5)
            self.Pesque2.append(["x"]*5)
            self.CantBarco1=0
            self.CantBarco2=0

#caracteristicas generales de los barcos
    def barcos(self):

        self.Nombrebarco="Bombardero"
        self.Material="Hierro colado"

    def __str__(self):
        return (self.Nombrebarco, self.Material, self.CantBarco1, self.CantBarco2)





#creamos la clase donde vamos a jugar
class Juego(Tablero):

    def juego(self,pfilamisil=0,pfilacolumna=0):
#cargamos las variables que vamos a utilizar y las igualamos a cero
#  algunas deben estar igualadas a 1 para que entren en el ciclo automaticamente

        self.turno=1
        self.turnos=1


        self.filamisil= pfilamisil
        self.columnamisil= pfilacolumna


        self.ultimofila=None
        self.ultimacolumna = None
        self.bomba1 = 0
        self.lanza1 = 0
        self.destru1 = 0
        self.pesque1 = 0
        self.bomba2 = 0
        self.lanza2 = 0
        self.destru2 = 0
        self.pesque2 = 0
        self.Jugador1=" "
        self.Jugador2=" "
        self.Misil=0
        self.Misil2=0
        self.ultimofila1=None
        self.ultimacolumna1 = None
        self.ultimofila2=None
        self.ultimacolumna2 = None


        for i in range(2):
# si el turno es igual a 1 pasa a que el jugador 1 ingrese sus datos
# y se le asignan los barcos y posiciones al azar

        #turno 1
            if self.turno==1:
                Juga.Nombre=str(input("Jugador1\nIngrese su nombre: "))

                self.Jugador1 = Juga.Nombre
            #se aumenta en 1 el numero de turnos y se le asigna un numero aleatorio
                # del 1 al 5 de misiles
                self.turno=self.turno+1
                self.misil1=random.randint(1,5)
                for x in range(4):
                #le asginamos los barcos
                    self.Tipobarco = random.randint(1, 4)

                    if self.Tipobarco == 1:
                        # aqui verificamos que si el numero es 1 el barco que se le asigna es un bombardero
                        # y le aplicamos una condicion para
                        # que entre
                        self.fila = random.randint(0, 4)
                        self.columna = random.randint(0, 4)
                        #fila y columna ya reciben valores y generamos la posicion con base en ellos
                        while True:


                            try:
                                if self.ultimofila != self.fila and self.ultimacolumna != self.columna:
                                    Barco.Nombrebarco = "Bomb"
                                    print(Barco.Nombrebarco)
                                    #aqui mencionamos donde se va a posicionar el barco generado en el tab fisico
                                    #este genera el nombre
                                    Tabfi.tablerologico1[self.fila][self.columna] = Barco.Nombrebarco
                                    #subimos en 1 el valor de bombarderos que tendrá y
                                    # asiganmos los valores de fila y columna por los ultimos
                                    self.bomba1 = self.bomba1 + 1
                                    self.ultimofila = self.fila
                                    self.ultimacolumna = self.columna
                                    #aqui Barco bombardero toma la posicion generada anteriormente
                                    Barco.Bomba[0][self.columna]=self.fila+self.columna
                                break

                            except ValueError:
                                print(" ")

                    elif self.Tipobarco == 2:
                        # aqui verificamos que si el numero es 2 el barco que se le asigna es un lanzamisiles
                        # y le aplicamos una condicion para
                        # que entre

                        self.fila = random.randint(0, 4)
                        self.columna = random.randint(0, 4)
                        #fila y columna reciben valores y con ellos generamos la posicion
                        while True:

                            try:
                                if self.ultimofila != self.fila and self.ultimacolumna != self.columna:
                                    #generamos el nombre del  barco
                                    Barco.Nombrebarco = "Lan"
                                    print(Barco.Nombrebarco)
                                    #posicionamos el nombre de barco en el tablero fisico
                                    Tabfi.tablerologico1[self.fila][self.columna] = Barco.Nombrebarco
                                    #aumentamos en uno el valor de lanzamisiles que tendrá
                                    self.lanza1 = self.lanza1 + 1
                                    #ahora igualamos la posicion de fila y columna
                                    self.ultimofila = self.fila
                                    self.ultimacolumna = self.columna
                                    #el objeto barco.lanza toma la posicion que tiene en el tablero logico

                                    Barco.Lanza[0][self.columna]=self.fila+self.columna

                                break

                            except ValueError:
                                print(" ")

                    elif self.Tipobarco == 3:
                        #si tipo barco es 3 nos genera un destructor

                        self.fila = random.randint(0, 4)
                        self.columna = random.randint(0, 4)
                        #se genera una posicion de fila y de columna aleatorias
                        while True:

                            try:
                                if self.ultimofila != self.fila and self.ultimacolumna != self.columna:
                                    #generamos el nombre del barco en el tab fisico
                                    Barco.Nombrebarco = "Des"
                                    print(Barco.Nombrebarco)
                                    #posicionamos el nombre del barco en el tablero fisico
                                    Tabfi.tablerologico1[self.fila][self.columna] = Barco.Nombrebarco
                                    #aumentamos en 1 el valor de destructores que tendrá
                                    self.destru1 = self.destru1 + 1
                                    #ultimo fila y columna toman los valores de fila y columna
                                    self.ultimofila = self.fila
                                    self.ultimacolumna = self.columna

                                    #el objeto destructor toma la posicion generada
                                    Barco.Dest[0][self.columna]=self.fila+self.columna

                                break
                            except ValueError:
                                print("")

                    elif self.Tipobarco == 4:
                        #si es 4 genera un pesquero
                        self.fila = random.randint(0, 4)
                        self.columna = random.randint(0, 4)
                        #genera una posicion apartir de fila y columna
                        while True:

                            try:
                                if self.ultimofila != self.fila and self.ultimacolumna != self.columna:
                                    #generamos el nombre del barco en el tablero fisico
                                    Barco.Nombrebarco = "Pes"
                                    print(Barco.Nombrebarco)
                                    #asignamos el nombre del barco en el tablero fisico
                                    Tabfi.tablerologico1[self.fila][self.columna] = Barco.Nombrebarco
                                    #aumentamos en 1 el valor de pesqueros que tendrá
                                    self.pesque1 = self.pesque1 + 1
                                    #igualamos el valor de ulti fila y columna por fila y columna generadas
                                    self.ultimofila = self.fila
                                    self.ultimacolumna = self.columna

                                    #el objeto barco pesquero toma su posicion
                                    Barco.Pesque[0][self.columna]=self.fila+self.columna
                                break
                            except ValueError:
                                print(" ")
                                self.ultimofila = self.fila
                                self.ultimacolumna = self.columna
                #asignamos la cantidad de barcos generados
                Barco.CantBarco1 = (self.bomba1 + self.lanza1 + self.destru1 + self.pesque1)
                #indicamos los barcos/misiles que tiene
                print(self.Jugador1,"Tienes {} barcos\n".format(Barco.CantBarco1), self.bomba1, " Bombarderos\n",
                      self.lanza1, " Lanzamisiles\n",
                      self.destru1, " Destructores\n",
                      self.pesque1, " Pesqueros\nEn las siguientes posiciones: ")
                #mencionamos donde están posicionados los barcos del jugador 1
                for i in Tabfi.tablerologico1:
                    print(" ".join(i))


                #si el turno es igual a 2 pasa a que el jugador 2 ingrese sus datos
                #  y se le asignan los barcos y posiciones al azar
            elif self.turno==2:
                Juga.Nombre = str(input("Jugador2\nIngrese su nombre: "))
                self.Jugador2 = Juga.Nombre
                self.turno = self.turno + 1

                #se genera cantidad de misiles
                self.misil2 = random.randint(1, 5)
                for x in range(4):
                    #se generaran 4 barcos aleatorios
                    self.Tipobarco = random.randint(1, 4)

                    if self.Tipobarco == 1:
                        #generamos la posicion que tomará el barco bombardero
                        self.fila = random.randint(0, 4)
                        self.columna = random.randint(0, 4)
                        while True:
                                    #aplicamos una condicion para que entre
                            try:
                                if self.ultimofila != self.fila and self.ultimacolumna != self.columna:
                                    #generamos el nombre del barco
                                    Barco.Nombrebarco = "Bomb"
                                    print(Barco.Nombrebarco)
                                    #generamos la posicion que tomará el barco en el tablero fisico
                                    Tabfi.tablerologico2[self.fila][self.columna] = Barco.Nombrebarco
                                    #aumentamos en 1 para luego contar
                                    self.bomba2 = self.bomba2 + 1
                                    #asignamos los valores
                                    self.ultimofila = self.fila
                                    self.ultimacolumna = self.columna
                                    #mencionamos la posicion del objeto barco bombardero
                                    Barco.Bomba2[0][self.columna]=self.fila+self.columna
                                break

                            except ValueError:
                                print(" ")

                    elif self.Tipobarco == 2:
                        #barco lanzamisiles del jugador 2
                        self.fila = random.randint(0, 4)
                        self.columna = random.randint(0, 4)
                        #generamos la posicion
                        while True:

                            try:
                                if self.ultimofila != self.fila and self.ultimacolumna != self.columna:
                                    #generamos el nombre
                                    print(Barco.Nombrebarco)
                                    Barco.Nombrebarco = "Lan"
                                    #generamos la posicion que tomará el nombre del barco
                                    Tabfi.tablerologico2[self.fila][self.columna] = Barco.Nombrebarco
                                    self.lanza2 = self.lanza2 + 1
                                    #igualamos valores
                                    self.ultimofila = self.fila
                                    self.ultimacolumna = self.columna

                                    #posicion que obtendrá el objeto barco lanzamisiles
                                    Barco.Lanza2[0][self.columna]=self.fila+self.columna

                                break

                            except ValueError:
                                print(" ")

                    elif self.Tipobarco == 3:
                        #barco destructor
                        self.fila = random.randint(0, 4)
                        self.columna = random.randint(0, 4)
                        #generamos posicion
                        while True:

                            try:
                                if self.ultimofila != self.fila and self.ultimacolumna != self.columna:
                                    #generamos nombre del barco
                                    Barco.Nombrebarco = "Des"
                                    print(Barco.Nombrebarco)
                                    #posicionamos el barco en el tablero fisico
                                    Tabfi.tablerologico2[self.fila][self.columna] = Barco.Nombrebarco
                                    #contador de barco +1
                                    self.destru2 = self.destru2 + 1
                                    #igualamos posiciones
                                    self.ultimofila = self.fila
                                    self.ultimacolumna = self.columna
                                    #asignamos posicion del objeto
                                    Barco.Dest2[0][self.columna]=self.fila+self.columna

                                break
                            except ValueError:
                                print("")

                    elif self.Tipobarco == 4:
                        #barco pesquero
                        self.fila = random.randint(0, 4)
                        self.columna = random.randint(0, 4)
                        #generamos posicion del barco pesquero
                        while True:

                            try:
                                if self.ultimofila != self.fila and self.ultimacolumna != self.columna:
                                    #generamos nombre
                                    Barco.Nombrebarco = "Pes"
                                    print(Barco.Nombrebarco)
                                    #posicionamos nombre en el tablero fisico
                                    Tabfi.tablerologico2[self.fila][self.columna] = Barco.Nombrebarco
                                    #contador de pesquero +1
                                    self.pesque2 = self.pesque2 + 1
                                    #igualamos posiciones
                                    self.ultimofila = self.fila
                                    self.ultimacolumna = self.columna

                                    #ubicamos el objeto
                                    Barco.Pesque2[0][self.columna]=self.fila+self.columna
                                break
                            except ValueError:
                                print(" ")
                                self.ultimofila = self.fila
                                self.ultimacolumna = self.columna
                #cantidad de barcos del jugador 2
                Barco.CantBarco2 = (self.bomba2 + self.lanza2 + self.destru2 + self.pesque2)
                #despliegue de barcos misiles del jugador 2
                print(self.Jugador2,"Tienes {} barcos\n".format(Barco.CantBarco2), self.bomba2, " Bombarderos\n",
                      self.lanza2, " Lanzamisiles\n",
                      self.destru2, " Destructores\n",
                      self.pesque2, " Pesqueros\nEn las siguientes posiciones: ")
                #muestra de barcos en el tablero fisico
                for i in Tabfi.tablerologico2:
                    print(" ".join(i))


# aqui comienza el juego

        while self.turnos!=3:
            #si estamos en turno 1 y la cantidad de misiles no es 0 juega jugador 1
            if self.turnos==1 and self.misil1!=0:


 #jugador 1 juega


                print(self.Jugador1, "Tiene {} misiles para atacar".format(self.misil1), ""
                    "\n y tiene {} barcos".format(
                    Barco.CantBarco1))

                print("Tienes estos barcos en las siguientes pocisiones")
                for i in Tabfi.tablerologico1:
                    print(" ".join(i))

                self.retirada1 = str(input("1.si\n2.no\nDesea retirarse?: "))

                if self.retirada1!="si":

                    #contador de turnos +1
                    self.turnos = self.turnos + 1
                    #se resta 1 misil
                    self.misil1=self.misil1-1

                    #despliegue del tablero fisico del jugador 1

                    #despliegue del tablero fisico vacio para claridad de posiciones
                    print("Elige bien donde deseas atacar")
                    for i in Tabfi.tablero2:
                        print(" ".join(i))



                    while True:
                            #se reciben los datos de la posiscion a atacar
                            self.filamisil = int(input("En que fila quiere atacar: "))
                            self.columnamisil = int(input("En que columna quiere atacar: "))
                            #se asigna la posicion donde ira el  misil
                            self.Misil=self.filamisil+self.columnamisil

                            #condicion de entrada
                            if self.filamisil < 5 and self.columnamisil < 5 and self.ultimofila1!=self.filamisil\
                                or self.ultimacolumna1!=self.columnamisil:

                                try:
                                    #se busca si hay un bombardero del jugador 1
                                    if ((Barco.Bomba2[0][0]==self.Misil) or (Barco.Bomba2[0][1]==self.Misil) or
                                        (Barco.Bomba2[0][2]==self.Misil) or (Barco.Bomba2[0][3]==self.Misil) or
                                        (Barco.Bomba2[0][4] == self.Misil)):
                                        #se marca una x en el tablero donde cayó el misil
                                        Tabfi.tablero2[self.filamisil][self.columnamisil] = "x"
                                        Barco.Bomba2[0][self.columna]="x"
                                        #se resta en 1 la cantidad de barcos
                                        Barco.CantBarco2 = Barco.CantBarco2 - 1
                                        #se marca una x en el tablero logico
                                        Tabfi.tablerologico2[self.filamisil][self.columnamisil] = "x"
                                        #se comparan posiciones
                                        self.ultimofila1 = self.filamisil
                                        self.ultimacolumna1 = self.columnamisil


                                        #indica que tipo de barco fue destruido(bombardero) del jugador 2
                                        print("El barco de tipo Bombardero fue destruido")
                                        #muestra la x en el tablero
                                        for i in Tabfi.tablero2:
                                            print(" ".join(i))

                                    #busqueda del barco destructor del jugador 2
                                    elif ((Barco.Lanza2[0][0]==self.Misil) or (Barco.Lanza2[0][1]==self.Misil) or
                                        (Barco.Lanza2[0][2] == self.Misil) or (Barco.Lanza2[0][3] == self.Misil) or
                                        (Barco.Lanza2[0][4] == self.Misil)):
                                        #destruye el barco y coloca una x en lugar del objeto en el tab fisico
                                        Barco.Lanza2[0][self.columna] = "x"
                                        Tabfi.tablero2[self.filamisil][self.columnamisil] = "x"
                                        #cantidad de barcos del jugador -1
                                        Barco.CantBarco2 = Barco.CantBarco2 - 1
                                        #muestra la x
                                        Tabfi.tablerologico2[self.filamisil][self.columnamisil] = "x"
                                        self.ultimofila1 = self.filamisil
                                        self.ultimacolumna1 = self.columnamisil


                                        print("El barco lanzamisiles fue destruido ")
                                        #muestra la x en el tablero
                                        for i in Tabfi.tablero2:
                                                print(" ".join(i))
                                    #busqueda del barco destructor del jugador 2
                                    elif ((Barco.Dest2[0][0]==self.Misil) or (Barco.Dest2[0][1]==self.Misil) or
                                        (Barco.Dest2[0][2] == self.Misil) or (Barco.Dest2[0][3] == self.Misil) or
                                        (Barco.Dest2[0][4] == self.Misil)):
                                        #destruye el objeto y lo sustiuye por una x en el tab fisico
                                        Barco.Dest[0][self.columna] = "x"
                                        Tabfi.tablero2[self.filamisil][self.columnamisil] = "x"
                                        #cantidad de barcos -1
                                        Barco.CantBarco2 = Barco.CantBarco2 - 1
                                        #pone x en  el tablero logico
                                        Tabfi.tablerologico2[self.filamisil][self.columnamisil] = "x"
                                        #compara posiciones
                                        self.ultimofila1 = self.filamisil
                                        self.ultimacolumna1 = self.columnamisil


                                        print("El barco destructor fue destruido ")
                                        #muestra la x en el tablero fisico
                                        for i in Tabfi.tablero2:
                                                        print(" ".join(i))
                                    #busqueda de barco pesquero
                                    elif ((Barco.Pesque2[0][0]==self.Misil) or (Barco.Pesque2[0][1]==self.Misil) or
                                        (Barco.Pesque2[0][2]==self.Misil) or (Barco.Pesque2[0][3]==self.Misil) or
                                        (Barco.Pesque2[0][4] == self.Misil)):
                                        #marca x en el objeto y en el tablero fisico
                                        Barco.Pesque2[0][self.columna] = "x"
                                        Tabfi.tablero2[self.filamisil][self.columnamisil] = "x"
                                        #cantidad de barcos -1
                                        Barco.CantBarco2 = Barco.CantBarco2 - 1
                                        #una x en el tablero logico
                                        Tabfi.tablerologico2[self.filamisil][self.columnamisil] = "x"
                                        #compara posiciones
                                        self.ultimofila1 = self.filamisil
                                        self.ultimacolumna1 = self.columnamisil

                                        print("El barco pesquero fue destruido ")
                                        #muestra la x del tablero fisico
                                        for i in Tabfi.tablero2:
                                            print(" ".join(i))

                                    #si no se cumple ninguna el misil cayó en el agua
                                    else:
                                        print("el misil cayó en el agua")

                                        self.ultimofila1 = self.filamisil
                                        self.ultimacolumna1 = self.columnamisil

                                    break

                                except ValueError:
                                    print("")

                            print("Fuera de rango o posicion repetida digite una posicion valida")

                else:
                    self.turnos=3


            elif self.turnos==2 and self.misil2:
                # si estamos en turno 2 y la cantidad de misiles no es 0 juega jugador 2
                print(self.Jugador2, "Tiene {} misiles para atacar".format(self.misil2),
                      "\n y te quedan {} barcos".format(
                          Barco.CantBarco2))

                print("Tienes estos barcos en las siguientes pocisiones")
                for i in Tabfi.tablerologico2:
                    print(" ".join(i))

                self.retirada2 = str(input("1.si\n2.no\nDesea retirarse?: "))
                if self.retirada2 != "si":


                    #muestra total de misiles y barcos
                    self.turnos = self.turnos -1
                    self.misil2 = self.misil2 - 1
                    #resta 1 misil y un turno



                    #muestra los barcos en sus respectivas posiciones
                    print("Tienes estos barcos en las siguientes pocisiones")
                    for i in Tabfi.tablerologico2:
                        print(" ".join(i))

                    #imprime tablero para mayor comodidad
                    print("Elige bien donde deseas atacar ")
                    for i in Tabfi.tablero1:
                        print(" ".join(i))

                    while True:
                        #recibe posicion de misil
                        self.filamisil = int(input("En que fila quiere atacar: "))
                        self.columnamisil = int(input("En que columna quiere atacar: "))

                        self.Misil2=(self.filamisil+self.columnamisil)

                        #condicion de entrada
                        if self.filamisil < 5 and self.columnamisil < 5 and self.ultimofila2!=self.filamisil\
                                or self.ultimacolumna2 !=self.columnamisil:

                            try:
                                    #busqueda de barco bombardero de jugador 2
                                if ((Barco.Bomba[0][0]==self.Misil2) or (Barco.Bomba[0][1]==self.Misil2) or
                                    (Barco.Bomba[0][2]==self.Misil2) or (Barco.Bomba[0][3]==self.Misil2) or
                                    (Barco.Bomba[0][4] == self.Misil2)):
                                    #destruye el barco y marca una x en el tablero fisico
                                    Tabfi.tablero1[self.filamisil][self.columnamisil] = "x"
                                    Barco.Bomba[0][self.columna] = "x"
                                    #cantidad de barcos -1
                                    Barco.CantBarco1 = Barco.CantBarco1 - 1
                                    #x en el tablero logico
                                    Tabfi.tablerologico1[self.filamisil][self.columnamisil] = "x"
                                    #compara posiciones
                                    self.ultimofila2 = self.filamisil
                                    self.ultimacolumna2 = self.columnamisil


                                    print("El barco bombardero fue destruido ")
                                    #imprime el tablero con sus barcos y sus x
                                    for i in Tabfi.tablero1:
                                        print(" ".join(i))

                                #busqueda del lanzamisiles
                                elif ((Barco.Lanza[0][0]==self.Misil2) or (Barco.Lanza[0][1]==self.Misil2) or
                                    (Barco.Lanza[0][2] == self.Misil2) or (Barco.Lanza[0][3] == self.Misil2) or
                                    (Barco.Lanza[0][4] == self.Misil2)):
                                    #destruye objeto y marca una x ademas asigna la x al tab fisico
                                    Barco.Lanza[0][self.columna] = "x"
                                    Tabfi.tablero1[self.filamisil][self.columnamisil] = "x"
                                    #cantidad de barcos -1 y x en el tablero logico
                                    Barco.CantBarco1 = Barco.CantBarco1 - 1
                                    Tabfi.tablerologico1[self.filamisil][self.columnamisil] = "x"
                                    #se comparan posiciones
                                    self.ultimofila2 = self.filamisil
                                    self.ultimacolumna2 = self.columnamisil


                                    print("El barco lanzamisiles fue destruido ")
                                    #imprime tablero fisico con barcos y x
                                    for i in Tabfi.tablero1:
                                        print(" ".join(i))
                                #busqueda del barco destructor
                                elif ((Barco.Dest[0][0]==self.Misil2) or (Barco.Dest[0][1]==self.Misil2) or
                                    (Barco.Dest[0][2] == self.Misil2) or (Barco.Dest[0][3] == self.Misil2) or
                                    (Barco.Dest[0][4] == self.Misil2)):
                                    #destruye el objeto y marca x en el tablero fisico
                                    Barco.Dest[0][self.columna] = "x"
                                    Tabfi.tablero1[self.filamisil][self.columnamisil] = "x"
                                    #cantidad de barcos -1 y marca x en el tab logico
                                    Barco.CantBarco1 = Barco.CantBarco1 - 1
                                    Tabfi.tablerologico1[self.filamisil][self.columnamisil] = "x"
                                    #compara posiciones
                                    self.ultimofila2 = self.filamisil
                                    self.ultimacolumna2 = self.columnamisil


                                    print("El barco destructor fue destruido ")
                                    #imprime tablero fisico con x
                                    for i in Tabfi.tablero1:
                                        print(" ".join(i))
                                #busqueda de barco pesquero
                                elif ((Barco.Pesque[0][0]==self.Misil2) or (Barco.Pesque[0][1]==self.Misil2) or
                                    (Barco.Pesque[0][2]==self.Misil2) or (Barco.Pesque[0][3]==self.Misil2) or
                                    (Barco.Pesque[0][4] == self.Misil2)):
                                    #destruye objeto y x en tablero fisico
                                    Barco.Pesque[0][self.columna] = "x"
                                    Tabfi.tablero1[self.filamisil][self.columnamisil] = "x"
                                    #cantidad de barcos -1 y X en tablero logico
                                    Barco.CantBarco1 = Barco.CantBarco1 - 1
                                    Tabfi.tablerologico1[self.filamisil][self.columnamisil] = "x"
                                    #comparacion de posicion
                                    self.ultimofila2 = self.filamisil
                                    self.ultimacolumna2 = self.columnamisil


                                    print("El barco pesquero fue destruido ")
                                    #imprime tablero fisico con x
                                    for i in Tabfi.tablero1:
                                        print(" ".join(i))
                                #si no se cumple cae en el agua
                                else:
                                    print("el misil cayó en el agua")
                                    self.ultimofila2 = self.filamisil
                                    self.ultimacolumna2 = self.columnamisil


                                break

                            except ValueError:
                                print("")

                        print("Fuera de rango o posicion repetida digite una posicion valida")

                else:
                    self.turnos=3
        else:
                #condicion para mostrar el ganador como jugador 1

                if Barco.CantBarco1 > Barco.CantBarco2 or self.misil1 > self.misil2:
                    #se crea el archivo de resultados


                    def creartxt():
                        archi = open('resultados.txt', 'w')
                        archi.close()
                    #se escribe en el txt los resultados
                    def grabartxt():
                        archi = open('resultados.txt', 'a')
                        archi.write('el jugador 2 perdió porque tiene {} barcos'.format(Barco.CantBarco2))
                        archi.write('y {} misiles'.format(self.misil2))
                        archi.write('y la cantidad es menor a la de tu contrincante')
                        archi.write('el jugador 1 ganó por que tiene {} barcos'.format(Barco.CantBarco1))
                        archi.write('y {} misiles'.format(self.misil1))
                        archi.write('y la cantidad es mayor a la de tu contrincante')
                        archi.close()
                    #se llaman los metodos
                    creartxt()
                    grabartxt()
                    print(self.Jugador2,"Perdio por que tiene {} barcos".format(Barco.CantBarco2)," ","y {} misiles".format(self.misil2),
                          " y la cantidad es menor a la de tu contrincante")

                    print(self.Jugador1,"Gano por que tiene {} barcos".format(Barco.CantBarco1), " ", "y {} misiles".format(self.misil1),
                          " y la cantidad es mayor a la de tu contrincante")

                elif Barco.CantBarco1 == Barco.CantBarco2 or self.misil1 == self.misil2 or self.retirada2=="si":


                    #se crea el txt de resultados
                    def creartxt():
                        archi = open('resultados.txt', 'w')
                        archi.close()
                    #se escriben los resultados en el txt
                    def grabartxt():
                        archi = open('resultados.txt', 'a')
                        archi.write('el jugador 2 empató porque tiene {} barcos'.format(Barco.CantBarco2))
                        archi.write('y {} misiles'.format(self.misil2))
                        archi.write('')
                        archi.write('el jugador 1 empató por que tiene {} barcos'.format(Barco.CantBarco1))
                        archi.write('y {} misiles'.format(self.misil1))
                        archi.write('')
                        archi.close()
                    #se llaman los metodos
                    creartxt()
                    grabartxt()
                    print(self.Jugador2,"Empato por que tiene {} barcos".format(Barco.CantBarco2)," ","y {} misiles".format(self.misil2))

                    print(self.Jugador1,"Empato por que tiene {} barcos".format(Barco.CantBarco1), " ", "y {} misiles".format(self.misil1))

                else:


                    #se crea el txt de resultados
                    def creartxt():
                        archi = open('resultados.txt', 'w')
                        archi.close()
                    #se escribe en el txt los resultados
                    def grabartxt():
                        archi = open('resultados.txt', 'a')
                        archi.write('el jugador 2 ganó porque tiene {} barcos'.format(Barco.CantBarco2))
                        archi.write('y {} misiles'.format(self.misil2))
                        archi.write('y la cantidad es mayor a la de tu contrincante')
                        archi.write('el jugador 1 perdió por que tiene {} barcos'.format(Barco.CantBarco1))
                        archi.write('y {} misiles'.format(self.misil1))
                        archi.write('y la cantidad es menor a la de tu contrincante')
                        archi.close()
                    #se llaman los metodos
                    creartxt()
                    grabartxt()
                    print(self.Jugador2,"Gano por que tiene {} barcos".format(Barco.CantBarco2), " ", "y {} misiles".format(self.misil2),
                          " y la cantidad es mayor a la de tu contrincante")


                    print(self.Jugador1,"Perdio por que tiene {} barcos".format(Barco.CantBarco1), " ", "y {} misiles".format(self.misil1),
                         " y la cantidad es menor a la de tu contrincante")







             #jugador 2 jugando



#llamadas de metodos y creacion de objetos

print("!Abordo!, estas apunto de comenzar una peligrosa aventura,\n"
"una batalla en las mas peligrosas aguas del oceano?\n" )

Juga=Persona()

Tabfi = Tablero()
Tabfi.creatablelogico()
Tabfi.creatablerofi()



Barco = Barcos()
Barco.llenabarcos()
Barco.barcos()


Juguemos=Juego()

Juguemos.juego()


print("Fin del juego")















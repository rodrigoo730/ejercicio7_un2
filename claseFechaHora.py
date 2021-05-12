from claseHora import Hora

class FechaHora:
    __segundo=0
    __minuto=0
    __hora=0
    __dia = 0
    __mes=0
    __anio=0
    def __init__(self,dia=1,mes=1,anio=2020,hora=0,minuto=0,segundo=0):

        if self.validarDato(dia,mes,anio,hora,minuto,segundo): # si devuelve true se ejecuta
            self.__segundo = segundo
            self.__minuto = minuto
            self.__hora = hora
            self.__dia = dia
            self.__mes = mes
            self.__anio = anio
            print('Fecha valida')
        else:
            self.__anio = 2020
            self.__mes = 1
            self.__dia = 1
            print('Fecha invalida, devuelve valor por defecto')


    def validarDato(self,dia,mes,anio,hora,minuto,segundo):
        bandera = False
        if segundo in range(0,60):
            if minuto in range(0,60):
                if hora in range(0,24):
                    if anio > 0:
                        if mes in range(1,13):
                            if mes == 2:
                                bisiesto = self.anioBisiesto(anio)
                                if not bisiesto:
                                    if dia in range(1,29):
                                        bandera = True
                                elif dia in range(1,30):
                                    bandera = True
                            if mes in [1, 3, 5, 7, 8, 10, 12]:
                                if dia in range(1, 32):
                                    bandera = True
                            if mes in [4,6,9,11]:
                                if dia in range(1,31):
                                    bandera = True
        return bandera




    def ajustarFecha(self):
        bandera= False
        bandera = self.anioBisiesto(self.__anio)
        if self.__segundo >= 60:
            entero = self.__segundo // 60
            resto = self.__segundo % 60

            self.__minuto += entero
            self.__segundo = resto
        if self.__minuto >= 60:
            entero = self.__minuto // 60
            resto = self.__minuto % 60
            self.__hora += entero
            self.__minuto = resto
        if self.__hora >= 24:
            entero = self.__hora // 24
            resto = self.__hora % 24
            self.__dia += entero
            self.__hora = resto
        if self.__mes in [1,3,5,7,8,10,12]:
            if self.__dia > 31:
                self.__mes+=1
                self.__dia -= 31
        if self.__mes in [4,6,9,11]:
            if self.__dia > 30:
                self.__mes +=1
                self.__dia -=30

        if self.__mes == 2:
            if not bandera:
                if self.__dia > 28:
                    self.__mes +=1
                    self.__dia -=28
            elif self.__dia > 29:
                self.__mes += 1
                self.__dia -= 29

        if self.__mes > 12:
            entero = self.__mes // 12
            resto = self.__mes % 12
            self.__anio += entero
            self.__mes = resto


    def Mostrar(self):
        print('La hora es {}:{}:{} con fecha {}/{}/{} '.format(self.__hora,self.__minuto,self.__segundo,self.__dia,self.__mes,self.__anio))

    def PonerEnHora(self,hora=0,minuto=0,segundo=0):
        self.__hora = hora
        self.__minuto = minuto
        self.__segundo = segundo

    def anioBisiesto(self,anio):
        if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
            #print('Es año biciesto')
            return True

            #print('No es año biciesto')

    def AdelantarHora(self,hora=0,minuto=0,segundo=0):
        self.__hora += hora
        self.__minuto += minuto
        self.__segundo += segundo

    def getAnio(self):
        return self.__anio
    def getMes(self):
        return self.__mes
    def getDia(self):
        return self.__dia
    def getHora(self):
        return self.__hora
    def getMinuto(self):
        return self.__minuto
    def getSegundo(self):
        return self.__segundo

    def getDatos(self):
        return [self.__segundo,self.__minuto,self.__hora,self.__dia,self.__mes,self.__anio]


    def __add__(self, other):
        if type(other) == Hora:
            fecha = FechaHora(self.__dia, self.__mes, self.__anio, self.__hora, self.__minuto, self.__segundo)
            fecha.__hora += other.get_Hora()
            fecha.__minuto += other.get_Minuto()
            fecha.__segundo += other.get_Segundo()
            fecha.ajustarFecha()
            return fecha
        else:
            print('Error de tipo de objeto')

    def __radd__(self, other):
        bandera = False
        if type(other) == Hora:
            fecha = FechaHora(self.__dia, self.__mes, self.__anio, self.__hora, self.__minuto, self.__segundo)
            fecha.__hora += other.get_Hora()
            fecha.__minuto += other.get_Minuto()
            fecha.__segundo += other.get_Segundo()
            fecha.ajustarFecha()
            bandera = True
        elif type(other) == int:
            fecha = FechaHora(self.__dia, self.__mes, self.__anio, self.__hora, self.__minuto, self.__segundo)
            fecha.__dia += other
            fecha.ajustarFecha()
            bandera = True
        if not bandera:
            print('Error de tipo de objeto')
        else: return fecha


    def __sub__(self, other):
        if type(other) == int:
            self.__dia -= other
            if self.__dia < 1:
                if self.__mes in [2,4,6,8,9,11,1]:
                    self.__dia +=31
                    self.__mes -= 1
                elif self.__mes in [5,7,10,12]:
                    self.__dia +=30
                    self.__mes -= 1
                elif self.__mes == 3:
                    bisiesto = self.anioBisiesto(self.__anio)
                    if not bisiesto:
                        self.__dia += 28
                    else:
                        self.__dia += 29
                    self.__mes -= 1
            if self.__mes < 1:
                self.__mes += 12
                self.__anio -= 1
            fecha = FechaHora(self.__dia, self.__mes, self.__anio, self.__hora, self.__minuto, self.__segundo)
            return fecha

        else:
            print('Error de tipo de objeto')


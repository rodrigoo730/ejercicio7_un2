
class Hora:
    __hora=''
    __minuto=''
    __segundo=''

    def __init__(self,hora=0,minuto=0,segundo=0):
        self.__hora=hora
        self.__minuto=minuto
        self.__segundo=segundo

    def Mostrar(self):
        print('La hora es {}:{}:{}'.format(self.__hora,self.__minuto,self.__segundo))

    def get_Hora(self):
        return self.__hora
    def get_Minuto(self):
        return self.__minuto
    def get_Segundo(self):
        return  self.__segundo
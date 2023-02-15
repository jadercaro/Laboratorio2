class AFD:
    def __init__(self, cadena):
        self._cadena = cadena
        self._ceroPar = True    # Describen el estado inicial y las condiciones de los estados
        self._unoImpar = False


    def determinarAceptacion(self):
        for i in self._cadena:
            self.funcionTransicion(int(i))

        if(self._ceroPar == True | self._unoImpar == True):
            return "Cumple el criterio de aceptacion"
        else:
            return "La cadena no cumple el criterio de aceptación"

        # Iteramos la cadena usando la funcion de transicion.


    def funcionTransicion(self, simbolo):
        if(simbolo == 0):
            if(self._ceroPar==True):
                self._ceroPar = False
            else:
                self._ceroPar = True
        elif(simbolo == 1):
            if(self._unoImpar == True):
                self._unoImpar = False
            else:
                self._unoImpar = True




# cadena=input(print('Ingrese la cadena de caracteres: '))
automataPrueba = AFD("110010100")

print(automataPrueba.determinarAceptacion())

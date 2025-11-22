class MiClase:
    def __init__(self, Valencia, Tempo, Tonos, listaCanciones, listaBailabilidad):
        self.Valencia = Valencia
        self.Tempo = Tempo
        self.Tonos = Tonos
        self.listaCanciones = listaCanciones
        self.listaBailabilidad = listaBailabilidad

    def ObtieneValencia(self, numero):
        
        numero_str = str(numero)
        digitos_impares = []
        for digit in numero_str:
            numero_entero = int(digit)
            if numero_entero % 2 != 0: 
                digitos_impares.append(numero_entero)

        return len(digitos_impares)

    def DivisibleTempo(self, numero):
        divisores = []
        for i in range(1, numero + 1):
            if numero % i == 0:
                divisores.append(i)

        return divisores

    def ObtieneMasBailable(self, lista):
        if not lista:
            return None


        mayor = lista[0]
        for elemento in lista:
            if elemento > mayor:
                mayor = elemento

        return mayor

    def VerificaListaCanciones(self, lista):
        for song in lista:
            if song is None:
                return False
        return True


################################################################################################
# Ejemplo de ejecución
objeto = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])

print(objeto.ObtieneValencia(1234567))       # Esperado: 4
print(objeto.DivisibleTempo(10))             # Esperado: [1, 2, 5, 10]
print(objeto.ObtieneMasBailable([0.8, 0.9, 0.7]))  # Esperado: 0.9
print(objeto.VerificaListaCanciones(["Canción 1", "Canción 2", "Canción 3"]))  # Esperado: True

#################################################################################################
#Pruebas Unitarias
import pytest 

class TestMiClase:
    
    def setup_method(self): #Ejecución antes de cada prueba
        self.objeto = MiClase(5, 120, 12, ["Cancion1", "Cancion2"], [0.8, 0.9])
    
    #PRUEBAS PARA "ObtieneValencia"
    
    def test_obtiene_valencia_todos_impares(self): #Verifica cuando todos los dígitos son impares
        resultado = self.objeto.ObtieneValencia(13579)
        assert resultado == 5  # Todos los dígitos 1,3,5,7,9 son impares
    
    def test_obtiene_valencia_mixto(self): #Verifica con digitos mixtos
        resultado = self.objeto.ObtieneValencia(1234)
        assert resultado == 2  # Solo 1 y 3 son impares
    
    #PRUEBAS PARA "DivisibleTempo"
    
    def test_divisible_tempo_numero_primo(self): #Verifica con numero primo
        resultado = self.objeto.DivisibleTempo(7)
        assert resultado == [1, 7]  # Solo divisible por 1 y sí mismo
    
    def test_divisible_tempo_numero_compuesto(self): #Verifica con numero compuesto
        resultado = self.objeto.DivisibleTempo(10)
        assert resultado == [1, 2, 5, 10]  # Divisores de 10


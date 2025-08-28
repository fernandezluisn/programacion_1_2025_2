class Calculadora:

    def __init__(self, valor_inic):
        self.valor_inicial = valor_inic

    def saludar(self):
        print("Hola soy una calculadora")

    def sumar(self, num_1, num_2):
        print(f"El resultado es {num_1 + num_2}")

calc_1 = Calculadora(0)

calc_1.sumar(2, 2)
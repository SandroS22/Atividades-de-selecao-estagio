class Triangulo:
    __l1 = 0
    __l2 = 0
    __l3 = 0

    def analise(self, l1, l2, l3):
        if l1 + l2 < l3 or l1 + l3 < l2 or l2 + l3 < l1:  # Verificação para não triângulo
            print('Os lados não formam um triângulo.')
        elif l1 == l2 and l1 == l2 and l3 == l1:  # Verifica se todos os lados são iguais
            print('Este triângulo é equilátero')
        elif l1 != l2 and l1 != l3 and l2 != l3:  # Verifica se todos os lados são diferentes
            print('Este triangulo é escaleno.')
        elif l1 == l2 or l1 == l3 or l2 == l3:  # Verifica se dois lados são iguais
            print('Este triângulo é isóceles')


triangulo = Triangulo()
triangulo.analise(2, 2, 90)

# Object - Vector
# поля - для зберігання координат вектора; для зберігання розмірності вектора;
# методи - введення елементів вектора; виведення елементів вектора у рядку;
# визначення довжини вектора; нормування вектора.

class Vector:
    def __init__(self, size):
        self.size = size
        self.coordinates = []

    def entering_elements(self):
        for i in range(self.size):
            self.coordinates.append(float(input('введіть координату {0} = '.format(i+1))))

    def vector_output(self):
        print(str(self.coordinates))

    def lenth_vector(self):
        return (sum(map(lambda x: x ** 2, self.coordinates)))**(1/2)
    def norma_vector(self):
        return [(x/self.lenth_vector()) for x in self.coordinates]

vector1 = Vector(int(input('введіть розмірність = ')))
vector1.entering_elements()
vector1.vector_output()
print(vector1.lenth_vector())
print(vector1.norma_vector())
# дано одновимірний, скласти список більші за 1 менші за остнній піднесені в квадрат
import random
a = [random.randint(-10,10) for el in range(int(input('к-сть ел: ')))]
# a = map(lambda x : x**2 if x > x[0] and x < x[-1], a)
a = map(lambda x : x**2, filter(lambda x : x[0] < x < x[-1], a))
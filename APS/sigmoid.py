import math
class Calculo:
    def __init__(self):
        pass

    def sigmoid(self,x):
        return 1 / (1 + math.exp(-x))
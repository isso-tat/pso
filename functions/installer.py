from functions.sphere import Sphere
from functions.rastrigin import Rastrigin
from functions.rosenbrock import Rosenbrock
from functions.griewank import Griewank
from functions.alpine import Alpine
from functions.minima_2n import Minima2n


class FunctionInstaller:
    def __init__(self):
        pass

    @staticmethod
    def function_install(dimension):
        # return Sphere(dimension)
        # return Rastrigin(dimension)
        # return Rosenbrock(dimension)
        # return Griewank(dimension)
        # return Alpine(dimension)
        return Minima2n(dimension)

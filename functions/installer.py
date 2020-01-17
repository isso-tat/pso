from functions.sphere import Sphere
from functions.rastrigin import Rastrigin
from functions.rosenbrock import Rosenbrock
from functions.griewank import Griewank


class FunctionInstaller:
    @staticmethod
    def function_install(dimension):
        # return Sphere(dimension)
        # return Rastrigin(dimension)
        # return Rosenbrock(dimension)
        return Griewank(dimension)

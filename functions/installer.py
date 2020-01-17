from functions.sphere import Sphere
from functions.rastrigin import Rastrigin
from functions.rosenbrock import Rosenbrock


class FunctionInstaller:
    @staticmethod
    def function_install(dimension):
        # return Sphere(dimension)
        # return Rastrigin(dimension)
        return Rosenbrock(dimension)

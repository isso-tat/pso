from functions.sphere import Sphere
from functions.rastrigin import Rastrigin


class FunctionInstaller:
    @staticmethod
    def function_install(dimension):
        # return Sphere(dimension)
        return Rastrigin(dimension)

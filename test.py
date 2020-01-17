from functions.installer import FunctionInstaller

dimension = 3

functionClient = FunctionInstaller.function_install(dimension)


# test
val = .5
test = []
for i in range(dimension):
    test.append(val)
h = functionClient.hulistic(test)
print(h, test)

# pso
## About
A model to find the minimum value of multidimensional functions. <br>
It uses: <br>
**Partical Swap Optimization** <br>
https://en.wikipedia.org/wiki/Particle_swarm_optimization <br>
<br>
**Artificial Bee Colony algorithm** <br>
https://en.wikipedia.org/wiki/Artificial_bee_colony_algorithm


## How to start
```
cd pso
python3 main.py
```
Shows the lowest value, and position at that time. <br>
Also plots the history of the lowest value on Semi-log graph. <br>
Firstly runs with PSO, and then ABC.

## How to test

### change functions
In `functions.installer`, change below:
```
class FunctionInstaller:
    ...
    def function_install(dimension):
        # return Sphere(dimension) <- remove comment out of the function you wanna use.
        ...
        return Minima2n(dimension) <- comment out functions you don't wanna use.
```

Then, run `test.py`
```
cd pso
python3 test.py
```

# py_TSP
**Travelling Salesman Problem** is defined as "Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city and returns to the origin city?". It is an NP-hard problem in combinatorial optimization, important in operations research and theoretical computer science.

**Genetic Algorithm** s a metaheuristic inspired by the process of natural selection that belongs to the larger class of evolutionary algorithms (EA). Genetic algorithms are commonly used to generate high-quality solutions to optimization and search problems by relying on biologically inspired operators such as mutation, crossover and selection.

This is an implementation of [this paper](https://www.researchgate.net/publication/264819943_Improved_genetic_algorithms_for_the_travelling_salesman_problem) for solving TSP with modified genetic algorithm.

## Dataset
[Here](http://www.math.uwaterloo.ca/tsp/data/index.html) is the real world dataset that can be used for testing TSP algorithms.

## Steps involved
**Step 1**

**Initialisation**: generate initial population of chromosomes of a predefined
population size. This implementation generates random populations.

**Step 2**

**Evaluation**: find objective function value for each of the chromosomes in the
population. In this step, a fitness function is defined to measure how good an individual(route) is.


**Step 3**


**Selection**: select chromosomes into next generation from the current population
according to some criteria. This implementation has a feature **Elitism** which selects best individual in the current population for mating to create next generation.


**Step 4**


**Crossover**: a pair of parent chromosomes is chosen sequentially from the top of
the population. Perform crossover operation using any of the crossover
operations to generate offspring. Since, SCX generates one offspring at a time,
so, second parent selected for a crossover is considered as first parent in the next
pair.


**Step 5**


**Mutation**: A chromosome is chosen sequentially from the top of the population.
Decide according probability of mutation whether it is going to generate a new
chromosome using mutation operation. If yes, perform mutation operation.
Repeat this process for all chromosomes in the population.


**Step 6**


**Generation**: Repeat Steps 2–5 until termination condition is satisfied. 


## Usage
1. Open a virtual environment to load packages needed.
2. To open a virtual environment open a terminal and paste `python3 -m venv py-TSP`. If you don't have virtual environment installed you can install it by `pip install virtualenv` or go to link [here](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) for more information.
3. After activating with  `cd py-TSP` and `source bin/activate`  install the packages in **requirements.txt** file by `pip install requirements.txt`.
4. Before we run our project we need to change some files in **Folium**. For this copy the files **folium.py** and **features.py** into folium folder by using `cp py_TSP/static/folium.py lib64/python3.8/site-packages/folium/` and `cp py_TSP/static/features.py lib64/python3.8/site-packages/folium/`.
5. Run `python3 app.py`.
6. After successfully running, go to `http://127.0.0.1:5000/` on web browser and you should see like this.

![Image](https://github.com/aakash0121/py_TSP/blob/master/static/1.png)

7. Add a few locations for delivery and the first location you enter is the location where the vehicle will start travelling.
8. Enter the desired values of Population Size, Elitism, Mutation Rate and Generations.

![Image](https://github.com/aakash0121/py_TSP/blob/master/static/2.png)

9. Hit **Start**.

## Output

![Image](https://github.com/aakash0121/py_TSP/blob/master/static/3.png)

10. To see the plot of distance and generations(iterations) go to Plot and on hover you would see a plot.

![Image](https://github.com/aakash0121/py_TSP/blob/master/static/plot.png)

This represents how the distance of route is reduced with generations. We want to decrease the distance as described in the vehicle routing problem.



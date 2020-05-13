import random
import numpy as np 
import operator
import pandas as pd
import matplotlib.pyplot as plt 
from math import radians, cos, sin, asin, sqrt 
from read_write_data import loadData

class City:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
    
    # calculate distance between two points on map
    def distance(self, city):

        # converting latitudes and longitudes degrees into radians
        lat1 = radians(self.lat)
        lon1 = radians(self.lon)
        lat2 = radians(city.lat)
        lon2 = radians(city.lon)

        # haversine formula
        dlat = lat2 - lat1
        dlon = lon2 - lon1

        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * asin(sqrt(a))
        
        # Radius of earth in kilometers. Use 3956 for miles 
        r = 6371

        return(c * r)
    
    # representing co-ordinates with a simple method
    def __repr__(self):
        return "(" + str(self.lat) + "," + str(self.lon) + ")"
    
    def __radd__(self, other):
        return self.__add__(other) 


class Fitness:
    def __init__(self, route):
        self.route = route
        self.distance = 0
        self.fitness = 0.0

    def routeDistance(self):
        if self.distance == 0:
            path_distance = 0

            # calculating distance through whole route
            for i in range(len(self.route)):
                from_city = self.route[i]

                # taking care of calculating distance for returning to starting city
                if i + 1 < len(self.route):
                    # destination city is the next index city
                    to_city = self.route[i+1]
                else:
                    to_city = self.route[0]
                
                # adding path distance to total distance
                path_distance += from_city.distance(to_city)

            self.distance = path_distance
            return self.distance

    def routeFitness(self):
        if self.fitness == 0:
            self.fitness = 1 / float(self.routeDistance())
        return self.fitness
    
def plot_distance_with_iterations(distance_list):
    plt.plot(distance_list)
    # plt.semilogy(out.bestcost)
    plt.xlim(0,)
    plt.xlabel('Iterations')
    plt.ylabel('Best Cost')
    plt.title('Genetic Algorithm (GA)')
    plt.grid(True)
    # plt.show()
    plt.savefig('static/plot.png')

# returns list of results in sorted order of their fitness scores in descending order    
def rankRoutes(population):
    fitnessResults = {}

    for i in range(len(population)):
        fitnessResults[i] = Fitness(population[i]).routeFitness()
    
    return sorted(fitnessResults.items(), key=operator.itemgetter(1), reverse=True)

# individuals gets selected for mating
def individuals_selection(pop_ranked, eliteSize):
    selection_results = []

    # a dataset containing index, fitness, cumulative sum, cumulative percentage
    df = pd.DataFrame(np.array(pop_ranked), columns=["Index", "Fitness"])

    # finding cumulative sum of fitness column
    df['cum_sum'] = df.Fitness.cumsum()

    # finding cumulative percentage of cumulative sum
    df['cum_perc'] = 100*df.cum_sum/df.Fitness.sum()
    
    # selection is reserved for eliteSize because they are fittest
    for i in range(0, eliteSize):
        selection_results.append(pop_ranked[i][0])

    # selection of rest of the individuals on the basis of roulette wheel
    for i in range(0, len(pop_ranked) - eliteSize):
        pick = 100*random.random()
        for i in range(0, len(pop_ranked)):
            if pick <= df.iat[i,3]:
                selection_results.append(pop_ranked[i][0])
                break

    return selection_results

# This will return the individual for breeding
def matingPool(population, selectionResults):
    mating_pool = []
    for i in range(len(selectionResults)):
        index = selectionResults[i]
        mating_pool.append(population[index])
    return mating_pool

# create an offspring from parents
def breed(parent1, parent2):
    child = []
    childP1 = []
    childP2 = []
    
    # randomly selecting two indexes for crossover
    geneA = int(random.random() * len(parent1))
    geneB = int(random.random() * len(parent1))
    startGene = min(geneA, geneB)
    endGene = max(geneA, geneB)

    # applying crossover
    for i in range(startGene, endGene):
        childP1.append(parent1[i])
        
    childP2 = [item for item in parent2 if item not in childP1]

    child = childP1 + childP2
    return child

# this will return the children by mating individuals in matingpool
def breedPopulation(mating_pool, eliteSize):
    children = []
    length = len(mating_pool) - eliteSize

    # shuffling the matingpool
    pool = random.sample(mating_pool, len(mating_pool))

    # preserving best individuals from the matingpool
    for i in range(0,eliteSize):
        children.append(mating_pool[i])
    
    # creating children by breeding rest of the individuals
    for i in range(0, length):
        child = breed(pool[i], pool[len(mating_pool)-i-1])
        children.append(child)
    return children

# this function mutates an individual with probability of mutationRate(swapped mutation)
def mutate(individual, mutationRate):
    for swapped in range(len(individual)):
        if(random.random() < mutationRate):
            swap_with = int(random.random() * len(individual))
            
            city1 = individual[swapped]
            city2 = individual[swap_with]
            
            individual[swapped] = city2
            individual[swap_with] = city1
    return individual

# this function returns mutated population(next generation)
def mutatePopulation(population, mutationRate):
    mutated_pop = []
    
    for ind in range(0, len(population)):
        mutated_ind = mutate(population[ind], mutationRate)
        mutated_pop.append(mutated_ind)
    return mutated_pop

# creates next generation population
def nextGeneration(pop, eliteSize, mutationRate):
    # sorted rank routes in a population
    pop_ranked = rankRoutes(pop)

    # individuals selected for mating
    selection_individuals = individuals_selection(pop_ranked, eliteSize)

    # the list of individuals for breeding
    mating_pool = matingPool(population=pop, selectionResults=selection_individuals)

    # the list of children after breeding
    children = breedPopulation(mating_pool, eliteSize)

    # the list of next generation population
    next_generation = mutatePopulation(children, mutationRate)
    return next_generation


# creates random routes of size of cityList
def createRoute(cityList):
    route = random.sample(cityList, len(cityList))
    return route

# generates initial population
def initialPopulation(popSize, cityList):
    population = []

    # create individuals(or routes) of size of popSize each of length of len(cityList)
    for i in range(popSize):
        population.append(createRoute(cityList))
    
    return population    
    
def execute_genetic(popSize, eliteSize, mutationRate, generations):
        city_list = []

        data = loadData('static/data.csv')

        for i in data:
            x, y = i
            city_list.append(City(x, y))

        # geneticAlgo(city_list, popSize, eliteSize, mutationRate, generations)

        # initial population
        pop = initialPopulation(popSize, city_list)

        # Distance of intial population's best individual(best route)
        print("Initial distance: " + str(1 / rankRoutes(pop)[0][1]))

        # Running for generations for finding optimum route(population)
        for i in range(0, generations):
            pop = nextGeneration(pop, eliteSize, mutationRate)

            # returning best route(individual)
            bestRouteIndex = rankRoutes(pop)[0][0]
            bestRoute = pop[bestRouteIndex]

            # best individual distance in the generation
            distance = 1/rankRoutes(pop)[0][1]
            
            yield [bestRoute, distance]
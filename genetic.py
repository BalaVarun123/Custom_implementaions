import random
import math
import numpy as np
class Gene:
    def __init__(self,init_features):
        self.features = init_features.copy()
    def mutate1(self,num_features,mutation_strength):
        i = 0
        j = 0
        while (i<num_features):
            j = random.randint(0,len(self.features)-1)
            self.features[j] = self.features[j] + random.uniform(-mutation_strength,mutation_strength)
            i+=1
    def replicate1(self,mute_num,mute_strength):
        t = Gene(self.features)
        t.mutate1(mute_num,mute_strength)
        return t
class Individual:
    def __init__(self,parent,mutation_rate = 2 ,mutation_strength = 1):
        self.PARENT = parent
        self.gene = parent.gene.replicate1(mutation_rate,mutation_strength)
        self.GENERATION = parent.GENERATION + 1
    def replicate(self,num):
        l = []
        i = 0
        while (i<num):
            l.append(Individual(self))
        return l
    @classmethod
    def create_randomly(self,num_features,multiplier=1):
        j = 0
        g = []
        while (j<num_features):
            g.append(random.choice((-1,1))*random.random()*multiplier)
            j += 1
        class dummy:
            def __init__(self):
                self.GENERATION = -1
                self.gene = Gene(g)
        return Individual(dummy())
class Environment:
    def __init__(self,max_population=math.inf):
        self.population= []
        self.max_population = max_population
    def initiate_population(self,population):
        l = len(populaiton)
        if l<=self.max_population:
            self.population = population
    def initiate_population_randomly(self,num_features,multiplier=1):
        i = 0
        population = []
        while (i<self.max_population):
            population.append(Individual.create_randomly(num_features,multiplier))
            i += 1
        self.population = population
    def extend_popultation(self,extention):
        self.population.extend(extention)
    def extend_population_randomly(self,num_individuals,num_features,multiplier=1):
        i = 0
        while (i<self.max_population):
            self.population.append(Individual.create_randomly(num_features,multiplier))
            i += 1
    def set_fitness_function(self,fitness_function):
        """fitness_function(individual)"""
        self.calculate_fitness = fitness_function
    def calculate_fitness_for_all(self):
        fitness = {}
        i = 0
        while (i<len(self.population)):
            fitness[self.population[i]] = self.calculate_fitness(self.population[i])
            i += 1
        return fitness
    def select_top(self,n):
        result = self.calculate_fitness_for_all()
        print(n)
        return  sorted(result,key = lambda m : result[m])[:n]
    def select_bottom(self,n):
        result = self.calculate_fitness_for_all()
        return  sorted(result,key = lambda m : result[m])[-n:]
    def kill(self,individuals):
        for i in individuals:
            self.population.pop(i)
    def evolve_one_step(self,n,replicate='top_per',num_replications = 1,kill = 'all'):
        if replicate == 'top_n' :
            selection  = self.select_top(n)
        elif replicate == 'bottom_n':
            selection  = self.select_bottom(n)
        elif replicate == 'random_n':
            selection = []
            for i in range(n):
                selection.append(random.choice(self.population))
        elif replicate == 'top_per' :
            selection  = self.select_top(round(len(self.population)*(n/100)))
        elif replicate == 'bottom_per':
            selection  = self.select_bottom(round(len(self.population)*(n/100)))
        elif replicate == 'random_per':
            selection = []
            for i in range(round(len(self.population)*(n/100))):
                selection.append(random.choice(self.population))
        elif replicate=='all':
            selection = self.population
            
        else :
            selection = []
        new_pop = []
        for i in selection:
             new_pop.append(i.replicate(num_replications))
        selection = None
        if kill == 'top_n' :
            selection  = self.select_top(n)
        elif kill == 'bottom_n':
            selection  = self.select_bottom(n)
        elif kill == 'random_n':
            selection = []
            for i in range(n):
                selection.append(random.choice(self.population))
        elif kill == 'top_per' :
            selection  = self.select_top(round(len(self.population)*(n/100)))
        elif kill == 'bottom_per':
            selection  = self.select_bottom(round(len(self.population)*(n/100)))
        elif kill == 'random_per':
            selection = []
            for i in range(len(self.population)*(n/100)):
                selection.append(random.choice(self.population))
        
        if kill == 'all':
            self.population.clear()
        elif kill == None:
            pass
        else:
            for i in selection:
                self.popuplation.pop(i)
        self.population.extend()
        select.num_popuplation = len(self.population)
    def evolve(self,num_steps,n,replicate='top_per',kill = 'all'):
        for i in range(numsteps):
            self.evolve(n,replicate,kill)

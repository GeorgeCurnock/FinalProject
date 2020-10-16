# FinalProject
Git repository to hold the code for my Msci final year project. I am investigating the importance of the crossover and mutation operators when evoling neural networks. I will evaluate the implemented operators on the board game Pentago.

# Pentago
  Pentago is a variation of noughts and crosses. It is played on a 6x6 grid which is also split down into 4 smaller 3x3 grids that can each rotate. The objective is to obtain 5 of your colour tiles in a row.
  A turn consists of a player placing one of their tiles in an available space on the board and then choosing one of the four smaller grids to rotate 90 degrees clockwise or anti-clockwise. 

# Crossover Operator
  The crossover operator is inspired by the concept of reproduction and survival of the fittest that occurs in natural evolution. 2 individuals from the population being evolved are selected for crossover and combined in some manner depending on their genotypic information to produce offspring that, in theory, take the common and favourable qualities of both the parents. The primary role of crossover is to better explore the population search space by combining traits of individuals that unlock new areas of the search space.

# Mutation Operator
  The mutation operator is inspired by genetic mutation that occurs in nature. An individuals genotypic information is randomly altered in some way to produce slightly different bahviours. These behaviours can sometimes be detrimental to the individual but sometimes can be a positive change that presents a more optimum solution to the problem. If the mutation results in a positive change then that individual will have a higher fitness and therefore perform the desired task better.  The primary role of mutation is exploitation of a local search space around a promising individual. Mutation is what drives convergence when promising individuals exist in the population as it can in theory continuously move through the search space iteratively improving from one individual to an optimum solution. 
  
# Permutation problem
  We must be careful when evolving neural networks through evolutionary algorithms given how we represent them. It is possible that a individual in the population(Phenotype) can have a number of different representations(Genotype). This can cause problems when recombining individuals through crossover as 2 almost indistuinguishable phenotypes can have completly different genotypic structure resulting in non functional offspring. Ideally we would like to find a crossover operator that is able to ensure neural networks can be recombined in a positive way that maintains the common behaviour of the parents. This is known as safe crossover
  
  Similarly when dealing with deep and recurrent neural networks that consists of hundreds of thousands of parameters the fragility of mutation also comes into play. Applying mutation to certain values within the genotypic structure can have more drastically then desired effects on the overal behaviour of the individual. For example altering weights closer to the inputs of a neural network will have much larger rippling effects that altering the weights closer to the outputs. It is because of this we look for a mutation operator that is able to predict the sensitivity of certain neuron outputs and alter the scale of mutation accordingly. This is known as safe mutation.

# Evaluation
  To evaluate the implementation of the researched safe crossover and safe mutation operators I will compare then to a number of different algorithms on the pentago proble. First I will compare to that of a random rule based Pentago player that has random moves. I will implement a standard neuroevolution algorithm using standard crossover and mutation operators to present the permutation problem. I will implement the safe crossover and safe mutation operators individually to observe how they alter the behaviour of the algorithm and then look to combine them. Finally, if time is available, I will look at a standard NEAT implementation and compare the performance of NEAT to that of my combined algorithm as a benchmark test.

# If I have time
  If time is available towards the end of the project I will look to improve upon my developed algorithm by looking for parallelisation opportunities and any potential for reducing the evaluation time of an individual in the population.

# Expected Timeline
 - Implement a working version of Pentago
 - Implement some form of simple GUI to observe pentago works correctly
 - Implement random AI as a a baseline of testing performance
 - Implement standard neuroevolution approach
 - Implement a number of different standard crossover/mutation operators
 - Implement Safe mutation operator
 - Implement Safe crossover operator
 - Apply either/both operators to the developed algorithm
 - Find NEAT implementation 
 - Parallelisation (May come earlier if poor performance)
 - Reduce evaluation function to NN outputs?
 - Minimise evaluation via minimax?


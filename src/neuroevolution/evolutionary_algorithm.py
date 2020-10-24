'''

4 main stages of evolutionary algorithm
 - initialization
 - selection
 - genetic operators
 - termination

 -- initialization
    create a random population of neural networks.
    Should they be completely random?
    Should they start at minimal architecture?
    How are we going to represent the neural network (genotype)?

 -- selection
    Decide which neural networks will be carried through to next generation
    what selection method should we choose? tournament? elitist?
    What fitness function will we evaluate off?
        number of moves?, win/lose/draw?

 -- genetic operators
        * Crossover
            Implement single point crossover
            Implement n point crossover
            Implement safe crossover through neuron alignment
            Implement Simba
            Implement 3 parent crossover for some of the above operators

        * Mutation
            Implement Gaussian random mutation
            Implement binary mutation?
            Implement safe mutation
            Think of a new mutation

        * Mischellaneous
            ideas of explicit fitness sharing, speciation and crowding
            combining back-propagation with evolutionary concepts
            reducing the fitness evaluation to evaluation of outputs
            parallelising evaluation

 -- termination
    when should the algorithm finish?
        when we have reached a sufficient win percentage?
        when the increments between improvements decreases to such a level?
        Human observed optimum level?


'''

from brkgaAPI.BRKGA import BRKGA
from SampleDecoder import SampleDecoder



def main():
 
    print("Welcome to the BRKGA API sample driver. \n Finding a (heuristic) minimizer for f(x) = sum_i (x_i * i) where x \\in [0,1)^n.")
    
    import pdb; pdb.set_trace()
    decoder = SampleDecoder()

    algorithm = BRKGA(n= 10,
                      p = 100,
                      pe = 0.1,
                      pm = 0.1,
                      rhoe = 0.7,
                      k = 3,
                      refDecoder = decoder,
                      MAX_Threads = 1
                     )

    X_INTVL = 100
    X_NUMBER = 2
    MAX_GENS = 1000

    for generation in range(MAX_GENS):
        algorithm.evolve()

        check_generation = generation + 1

        if check_generation % X_INTVL == 0:
            algorithm.exchangeElite(X_NUMBER)


    bound = min(algorithm.p, 10)

    for i in range(algorithm.k):
        print("Population # " + str(i))

        for j in range(bound):          

            print("\t" + str(j) + " : " + str(algorithm.getPopulation(i).getFitness(j)))



    print("Best solution found has objective value = " + str(algorithm.getBestFitness()))
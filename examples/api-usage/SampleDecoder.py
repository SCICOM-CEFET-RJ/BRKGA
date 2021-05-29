

"""
 * The chromosome's fitness is computed as the sum of its individual alleles. We also show how to
 * generate a random permutation of {0, 1, ..., n-1} using the supplied chromosome.
 """

class SampleDecoder:

    def decode(self, chromossome):

        myFitness = 0.
        #import pdb; pdb.set_trace()

        for i in range(len(chromossome)):
            myFitness += float((i + 1)) * chromossome[i]

        
        return myFitness




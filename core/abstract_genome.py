class AbstractGenome:
    def __init__(self) -> None:
        pass


    # Mutation, Crossover, Copy
    def makeCopy(self,):
        pass

    def makeMutatedCopy(self,):
        pass

    def mutate(self,):
        pass

    def makeCrossedCopy(self,*others):
        pass

    def cross(self,*others):
        pass


    # Reading / Transcription / Translation
    def readInt(self,a,b)->int:
        pass

    def readFloat(self,)->float:
        pass

    def readBool(self,)->bool:
        pass
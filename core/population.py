from organism import Organism


class Population:
    def __init__(self,popSize) -> None:
        self.size = popSize
        self.organisms = [Organism() for _ in range(self.size)]
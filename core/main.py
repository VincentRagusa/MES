from parameters import Parameters

#commandLine Parameters
# -s <path> save config file
# -c <path> load config file


PT = Parameters()
if loadConfigFile:
    PT.readConfigFile(pathToConfig)
if saveConfigFile:
    PT.writeConfigFile(pathToConfig)
    exit()


# imports after config finished
from population import Population






thisPopulation = Population(parameters["PopSize"])

# INIT POPULATION(S)
#   INIT ORGANISMS
#       INIT GENOME(S)
#       INIT CONTROLLER(S)
# INIT ENVIRONMENT
# INIT SCRIBE
# INIT BREEDER

for generation in range(parameters["Generations"]):
    pass
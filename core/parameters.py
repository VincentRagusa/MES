
# parameters are not write protected. 
class Parameters:
    def __init__(self) -> None:
        self.parameters = {}
        self.register("GLOBAL-environmentName","abstract_environment","name of environment component to use")
        self.register("GLOBAL-breederName","abstract_breeder","name of breeder component to use")
        self.register("GLOBAL-controllerName","abstract_controller","name of controller component to use")
        self.register("GLOBAL-genomeName","abstract_genome","name of genome component to use")
        self.register("GLOBAL-scribeName","abstract_scribe","name of the scribe component to use")

    def register(self,name,defaultValue,description):
        self.parameters[name] = (defaultValue,description)

    def writeConfigFile(self,pathToFile):
        # writes a config file to disk, saves name, default value, and description in a known format (JSON? YAML?)
        pass

    def readConfigFile(self,pathToFile):
        # reads a config file from disk, matches names and stores values from a known format.
        pass
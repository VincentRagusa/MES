# Modular Evolution Simulator (MES)
This code implements MES (/mɛs/), a modular framework for building evolutionary simulations. You can use this software to build a diverse range of evolutionary simulations and conduct scientific research on evolving systems. The modular nature of the software allows for decentralized developement, instant integration, and combination of new components.
## What can I build with MES?
You can use MES to construct many of the traditional evolutionary computation framework such as Genetic Algorithms and Genetic Programming.
MES can also build more complicated evolving systems like [Avida](https://alife.org/encyclopedia/digital-evolution/avida/).
MES supports complex optimization algorithms such as NSGA-II, MAP-Elites, and ALPS.
## What are Components?
Components represent various functionally independent pieces of evolving systems. MES connects components together and orchastrates their interactions through a standard intarface. Components are combined, mixed and matched, and connected through MES to form evolutionary simulations. Because Components function independently, swapping one component for another instantly implements a different evolutionary simulation.
### Component Types
- Genome
  - Holds, mutates, and combines heritable information.
- Controller
  - Makes decisions, based on inputs, by providing outputs.
- Breeder
  - Selects organisms for reproduction.
- Environment
  - Holds and changes the world state, provides input to Controllers, and implements natural selection.
- Scribe
  - Maintains a record of information gathered during execution.
## Development Information
We develop MES in Python 3.x. MES currently has no 3rd party dependencies. We have plans to develop a [NIM](https://nim-lang.org/) version of MES.

#WAP to import a module and access its members from an other file
import EXERCISES.exo18 as exo18

from exo18 import atm

HDFC = atm(2000,1234)
HDFC.display()



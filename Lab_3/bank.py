import abc 
import collections  
from atm import ATM

class Bank():

    collections.abc.Sequence.register(ATM)


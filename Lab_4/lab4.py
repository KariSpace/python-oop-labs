from abc import abstractmethod
from typing import Protocol, Iterable
import re


class SupportsPhone(Protocol):
    @abstractmethod
    def call(self) -> None:
        raise NotImplementedError


class Phone(SupportsPhone):              

    def __init__(self, company, battery):
        self.company = company   
        self.battery = battery

    def call(self): 
        phone_number = "0000000000"
        print(f'\nCalling to {phone_number}...')


class MobilePhone():                
    
    def __init__(self, company, battery, screen):
        self.screen =  screen
        self.company = company   
        self.battery = battery

    def call(self): 
        phone_number = "0000000000"
        print(f'Calling to {phone_number} by facetime...')



def phone_all(phones: Iterable[SupportsPhone]) -> None:
    for t in phones:
        t.call()



phone_all([Phone("Samsung", 2500)])  # ok
phone_all([Phone("Samsung", 2500), MobilePhone("Samsung", 900, "16inch")])  # ok

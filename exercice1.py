from abc import ABC, abstractmethod


class Boisson(ABC):

    @abstractmethod
    def imprimer_ingredient(self):
        pass


class OrangeMax(Boisson):

    def __init__(self, marque):
        self._marque = marque


# Modifiez la classe enfant pour éviter que le code donne une erreur de Type
orange_max = OrangeMax("Orange Max")
orange_max.imprimer_ingredient()
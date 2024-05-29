"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02 import exceptions


class Plane(Vehicle):
    cargo: float = 0
    max_cargo: float = 0

    def __init__(self, weight: float, fuel: float, fuel_consumption: float, max_cargo: float) -> None:
        self.max_cargo = max_cargo
        super().__init__(weight, fuel, fuel_consumption)

    def load_cargo(self, cargo: float) -> None:
        if self.cargo + cargo <= self.max_cargo:
            self.cargo += cargo
        else:
            raise exceptions.CargoOverload

    def remove_all_cargo(self) -> float:
        cargo = self.cargo
        self.cargo = 0
        return cargo

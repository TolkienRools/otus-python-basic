from abc import ABC
from homework_02 import exceptions


class Vehicle(ABC):
    weight: float = 0
    started: bool = False
    fuel: float = 0
    fuel_consumption: float = 0

    def __init__(self, weight: float, fuel: float, fuel_consumption: float) -> None:
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self) -> None:
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise exceptions.LowFuelError

    def move(self, distance: float) -> None:
        if self.fuel - distance * self.fuel_consumption >= 0:
            self.fuel -= distance * self.fuel_consumption
        else:
            raise exceptions.NotEnoughFuel

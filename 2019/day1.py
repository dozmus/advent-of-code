import math
from decimal import Decimal

from benchmark import benchmark
from custom_io import read_lines


def fuel_required(mass):
    return math.floor(mass / 3) - 2


@benchmark
def day1a(lines):
    return sum([fuel_required(l) for l in lines])


def fuel_required_fuel_also_requires_fuel(mass):
    fuel = math.floor(mass / 3) - 2

    if fuel <= 0:
        return 0
    return fuel + fuel_required_fuel_also_requires_fuel(fuel)


@benchmark
def day1b(lines):
    return sum([fuel_required_fuel_also_requires_fuel(l) for l in lines])
    

input = [Decimal(l) for l in read_lines('data/day1.txt')]

print(day1a(input))
print(day1b(input))

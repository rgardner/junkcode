#!/usr/bin/env python3
"""Google Interview Question July 2015

The goal of this was to be able to draw countries randomly with the underlying
distributino being the population of the country.

"""

from __future__ import print_function
from collections import defaultdict
import random


def reverse_map(values, func):
    result = defaultdict(list)
    for value in values:
        result[func(value)].append(value)
    return result


def build_random_country(populations):
    total_population = 0
    countries = {}
    for country, population in populations.items():
        countries[country] = total_population + population
        total_population += population

    def random_country():
        pop = random.randrange(total_population)
        for country, population in countries.items():
            if pop < population:
                return country

    return random_country


print(reverse_map((1, 2, 3, 4), lambda x: x * 2))

populations = {'USA': 10, 'Canada': 30}
random_country = build_random_country(populations)
print(random_country())

def unique_elements(input_list):
    return list(set(input_list))


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def primes_in_range(min_num, max_num):
    primes = [num for num in range(min_num, max_num + 1) if is_prime(num)]
    return primes


import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calculate_distance(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

    def get_coordinates(self):
        return self.x, self.y

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y


def sort_strings(strings):
    sorted_by_length = sorted(strings, key=len)
    sorted_by_length_reverse = sorted_by_length[::-1]
    return sorted_by_length, sorted_by_length_reverse

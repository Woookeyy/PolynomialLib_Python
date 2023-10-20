from itertools import product


def get_num_superscript(num):
    num = str(num)
    result = str()

    digit_dict = {
        '0': '\u2070',
        '1': '\u00b9',
        '2': '\u00b2',
        '3': '\u00b3',
        '4': '\u2074',
        '5': '\u2075',
        '6': '\u2076',
        '7': '\u2077',
        '8': '\u2078',
        '9': '\u2079'
    }

    for dig in num:
        result += digit_dict[dig]

    return result


class Polynomial:
    def __init__(self, coefficients):

        zeros = 0
        for coefficient in coefficients:
            if coefficient == 0:
                zeros += 1
            else:
                break

        coefficients = coefficients[zeros:]

        coefficients.reverse()

        if len(coefficients) == 0:
            coefficients = [0]

        self._coefficients = coefficients

        self._deg = len(self._coefficients) - 1

        if len(coefficients) == 1 and 0 in coefficients:
            self._deg = None

    def __str__(self):

        if self.deg() is None:
            return '0'

        string = str()
        for x_pow, coefficient in enumerate(self._coefficients):
            if coefficient == 0:
                continue

            if x_pow > 1:
                string = get_num_superscript(x_pow) + string

            if x_pow > 0:
                string = 'x' + string

            if coefficient not in {-1, 1} or x_pow == 0:
                string = str(coefficient) + string

            if coefficient > 0:
                string = '+' + string

            if coefficient == -1 and x_pow != 0:
                string = '-' + string

        if string[0] == '+':
            string = string[1:]

        return string

    def __add__(self, other):

        if self.deg() is None:
            return other
        if other.deg() is None:
            return self

        new_coefficients = list()

        for x_pow in range(min(self.deg(), other.deg()) + 1):
            new_coefficient = self.get_coefficient(x_pow) + other.get_coefficient(x_pow)
            new_coefficients.append(new_coefficient)

        for x_pow in range(min(self.deg(), other.deg()) + 1, max(self.deg(), other.deg()) + 1):

            if self.deg() > other.deg():
                new_coefficients.append(self.get_coefficient(x_pow))
            if other.deg() > self.deg():
                new_coefficients.append(other.get_coefficient(x_pow))

        new_coefficients.reverse()

        return Polynomial(new_coefficients)

    def __iadd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):

        if self.deg() is None and other.deg() is None:
            return Polynomial([0])

        if self.deg() is None:
            return Polynomial([-other.get_coefficient(coe) for coe in reversed(range(other.deg() + 1))])
        if other.deg() is None:
            return self

        new_coefficients = list()

        for x_pow in range(min(self.deg(), other.deg()) + 1):
            new_coefficient = self.get_coefficient(x_pow) - other.get_coefficient(x_pow)
            new_coefficients.append(new_coefficient)

        for x_pow in range(min(self.deg(), other.deg()) + 1, max(self.deg(), other.deg()) + 1):

            if self.deg() > other.deg():
                new_coefficients.append(-self.get_coefficient(x_pow))
            if other.deg() > self.deg():
                new_coefficients.append(-other.get_coefficient(x_pow))

        new_coefficients.reverse()

        return Polynomial(new_coefficients)

    def __isub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):

        if self.deg() is None or other.deg() is None:
            return Polynomial([0])

        new_coefficients = [0 for _ in range(self.deg() + other.deg() + 1)]

        for x_pow1, x_pow2 in product(range(self.deg() + 1), range(other.deg() + 1)):

            new_coefficient = self.get_coefficient(x_pow1) * other.get_coefficient(x_pow2)
            new_x_pow = x_pow1 + x_pow2

            new_coefficients[new_x_pow] += new_coefficient

        new_coefficients.reverse()

        return Polynomial(new_coefficients)

    def deg(self):
        return self._deg

    def get_coefficient(self, x_power):
        return self._coefficients[x_power]

    def __imul__(self, other):
        return self.__mul__(other)

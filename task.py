class City:
    def __init__(self, name, population, square, year):
        self.name = name
        self.population = population
        self.square = square
        self.year = year

    def __add__(self, other):
        new_name_city = 'New City'
        population = self.population + other.population
        square = self.square + other.square
        year = present_year()
        return City(new_name_city, population, square, year)

    def __str__(self):
        return f'City {self.name}, ' \
               f'{self.population} person, ' \
               f'{self.square} m3, ' \
               f'{self.year} year of foundation'

    def __gt__(self, other):
        if self.population > other.population and \
                self.square > other.square and \
                self.year > other.year:
            return True
        else:
            return False

    def __sub__(self, other):
        return WrongOperatorError('Error!!! Operator subtraction is not available')

    def __le__(self, other):
        return WrongOperatorError('Error!!! Operator less than or equal are not available')

    def __ge__(self, other):
        return WrongOperatorError('Error!!! Operator greater than or equal are not available')


def present_year():
    import datetime
    present_date = datetime.datetime.now()
    year = present_date.year
    return year


class WrongOperatorError(Exception):
    """"This is exception when the wrong operation is used"""
    pass

city_1 = City('Paris', 500, 400, 1112)
city_2 = City('London', 400, 300, 1111)
new_city = city_1 + city_2
print(new_city)

compare = city_1 > city_2
print(compare)

subtraction = city_1 - city_2
print(subtraction)

compare_2 = city_2 <= city_1
print(compare_2)

compare_3 = city_1 >= city_2
print(compare_3)

class City:
    def __init__(self, name, population, square, year):
        self.name = name
        self.population = population
        self.square = square
        self.year = year

    def __add__(self, other):
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
        return (self.population, self.square, self.year) > (other.population, other.square, other.year)

    def __sub__(self, other):
        return WrongOperatorError(error_sub)

    def __le__(self, other):
        return WrongOperatorError(error_le)

    def __ge__(self, other):
        return WrongOperatorError(error_ge)


def present_year():
    import datetime
    present_date = datetime.datetime.now()
    year = present_date.year
    return year


class WrongOperatorError(Exception):
    """"This is exception when the wrong operation is used"""
    pass


error_sub = 'Error!!! Operator subtraction is not available'
error_le = 'Error!!! Operator less than or equal are not available'
error_ge = 'Error!!! Operator greater than or equal are not available'

new_name_city = 'New City'

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

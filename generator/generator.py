from faker import Faker
from data.data import City

faker = Faker()
Faker.seed()


def get_city():
    yield City(
        city=faker.location_on_land()
    )


def get_correct_city_name(city):
    city_name = str(city).split("'")[5]
    country_name = str(city).split("'")[7]
    correct_city_name = ', '.join([city_name, country_name])
    return correct_city_name

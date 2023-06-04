from faker import Faker
from data.data import City

faker = Faker()
Faker.seed()


def get_city():
    yield City(
        city=faker.location_on_land()
    )

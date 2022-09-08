from data_generators.generators import RandomGrapeBuyer, RandomGrapeSeller
from app.schema import GrapeBuyer, GrapeSeller


def validate_grape_buyer():
    assert all(GrapeBuyer(**vars(RandomGrapeBuyer())) for _ in range(1000))


def validate_grape_seller():
    assert all(GrapeSeller(**vars(RandomGrapeSeller())) for _ in range(1000))


def validate_schemas():
    validate_grape_buyer()
    validate_grape_seller()


if __name__ == '__main__':
    validate_schemas()

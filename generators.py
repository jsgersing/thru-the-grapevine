import uuid

from data_options import *


class Printable:
    """Parent Class"""
    def __str__(self):
        return "\n".join(f"{k}: {v}" for k, v in vars(self).items())


class RandomGrapeBuyer(Printable):
    """Generates GrapeBuyer record"""

    def __init__(self):
        self.profile_id = uuid.UUID()
        self.name = f"{last_name_buyer} Family Winery"
        self.email = f"{first_name_buyer}.{last_name_buyer}@gmail.com"
        self.state = state_buying
        self.grape_seeking = grape_buying
        self.volume_seeking = tons_seeking


class RandomGrapeSeller(Printable):
    """Generates GrapeSeller record"""

    def __init__(self):
        self.profile_id = uuid.UUID()
        self.name = f"{last_name_seller} Family Vineyard"
        self.email = f"{first_name_seller}.{last_name_seller}@gmail.com"
        self.state = state_selling
        self.grape_selling = grape_selling
        self.volume_selling = tons_selling



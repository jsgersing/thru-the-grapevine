import names

from data_generators.data_options import *


class Printable:
    """Parent Class"""
    def __str__(self):
        return "\n".join(f"{k}: {v}" for k, v in vars(self).items())


class RandomGrapeBuyer(Printable):
    """Generates GrapeBuyer record"""

    def __init__(self):
        self.profile_id = generate_uuid(16)
        self.first_name = names.get_first_name()
        self.last_name = names.get_last_name()
        self.winery = f"{self.last_name} Family Winery"
        self.email = f"{self.first_name}.{self.last_name}@{random.choice(email_ending_buyer)}"
        self.state = random.choice(state)
        self.grapes_seeking = random.sample(grape_variety, k=random.randint(1, 4))
        self.volume_seeking = [str(random.randint(1, 10) * 5) for _ in self.grapes_seeking]


class RandomGrapeSeller(Printable):
    """Generates GrapeSeller record"""

    def __init__(self):
        self.profile_id = generate_uuid(16)
        self.first_name = names.get_first_name()
        self.last_name = names.get_last_name()
        self.vineyard = f"{self.last_name} Family Vineyard"
        self.email = f"{self.first_name}.{self.last_name}@{random.choice(email_ending_seller)}"
        self.state = random.choice(state)
        self.grapes_selling = random.sample(grape_variety, k=random.randint(1, 4))
        self.volume_selling = [str(random.randint(1, 10) * 5) for _ in self.grapes_selling]

import random
import string
from itertools import chain
from math import ceil, floor

import names

first_name_buyer = names.get_first_name()
last_name_buyer = names.get_last_name()
winery_name = f"{last_name_buyer} Family Winery"

first_name_seller = names.get_first_name()
last_name_seller = names.get_last_name()
vineyard_name = f"{last_name_seller} Family Vineyard"

email_ending_buyer = ("gmail.com", "hotmail.com", "yahoo.com", "aol.com")
email_ending_seller = ("gmail.com", "hotmail.com", "yahoo.com", "aol.com")

random_email_buyer = random.choice(email_ending_buyer)
random_email_seller = random.choice(email_ending_seller)


grape_variety = (
    "Chardonnay", "Viognier", "Sauvignon blanc", "Riesling", "Semillon",
    "Roussanne", "Marsanne", "Pinot blanc", "Pinot gris",
    "Pinot noir", "Cabernet Sauvignon", "Nebbiolo", "Sangiovese",
    "Syrah", "Merlot", "Petit Verdot", "Granache", "Mourvedre"

)

grapes_seeking = random.sample(grape_variety, k=random.randint(1, 4))
grapes_selling = random.sample(grape_variety, k=random.randint(1, 4))

state = (
    "California", "Washington", "Oregon"
)

state_buying = random.choice(state)
state_selling = random.choice(state)

tons_seeking = [random.randint(1, 10) * 5 for _ in grapes_seeking]
tons_selling = [random.randint(1, 10) * 5 for _ in grapes_selling]


def generate_uuid(n_len: int) -> str:
    n1 = ceil(n_len / 2)
    n2 = floor(n_len / 2)
    prefix = random.choices(string.ascii_letters, k=n1)
    suffix = map(str, random.choices(range(0, 9), k=n2))
    uuid_list = list(chain(prefix, suffix))
    random.shuffle(uuid_list)
    uuid = "".join(uuid_list)
    return uuid


if __name__ == "__main__":
    print(
        f"""Buyer: {winery_name}
        Contact: {first_name_buyer} {last_name_buyer}
        Email: {first_name_buyer.lower()}.{last_name_buyer.lower()}@{random_email_buyer}
        Grape Variety: {grapes_seeking}, 
        Volume: {tons_seeking} tons
        State: {state_buying}""")
    print(
        f"""Seller: {vineyard_name}
        Contact: {first_name_seller} {last_name_seller}
        Email: {first_name_seller.lower()}.{last_name_seller.lower()}@{random_email_seller}
        Grape Variety: {grapes_selling}, 
        Volume: {tons_selling} tons
        State: {state_selling}""")

import random

import names

first_name_buyer = names.get_first_name()
last_name_buyer = names.get_last_name()
winery_name = f"{last_name_buyer} Family Winery"

first_name_seller = names.get_first_name()
last_name_seller = names.get_last_name()
vineyard_name = f"{last_name_seller} Family Vineyard"


grape_variety = (
    "Chardonnay", "Viognier", "Sauvignon blanc", "Riesling", "Semillon",
    "Roussanne", "Marsanne", "Pinot blanc", "Pinot gris",
    "Pinot noir", "Cabernet Sauvignon", "Nebbiolo", "Sangiovese",
    "Syrah", "Merlot", "Petit Verdot", "Granache", "Mourvedre"

)

grape_buying = random.sample(grape_variety, k=random.randint(1, 4))
grape_selling = random.sample(grape_variety, k=random.randint(1, 4))

state = (
    "California", "Washington", "Oregon"
)

state_buying = random.choice(state)
state_selling = random.choice(state)

tons_seeking = random.randint(1, 10) * 5
tons_selling = random.randint(1, 20) * 5


if __name__ == "__main__":
    print(
        f"""Buyer: {winery_name}
        Contact: {first_name_buyer} {last_name_buyer}
        Grape Variety: {grape_buying}, 
        Volume: {tons_seeking} tons
        State: {state_buying}""")
    print(
        f"""Seller: {vineyard_name}
        Contact: {first_name_seller} {last_name_seller}
        Grape Variety: {grape_selling}, 
        Volume: {tons_selling} tons
        State: {state_selling}""")



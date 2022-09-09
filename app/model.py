from typing import List

from pandas import DataFrame, Series, merge

from app.data import MongoDB


class BuyerSellerMatcher:
    """ Callable matching class implementing sorted search algorithm """
    db = MongoDB()

    def __call__(self, n_matches: int, profile_id: str) -> List[str]:
        """ Return a list of profile_id for matched sellers """
        buyer_id = profile_id

        grape_buyers = DataFrame(self.db.projection("GrapeBuyers", {}, {
                "_id": False,
                "profile_id": True,
                "grapes_seeking": True,
                "volume_seeking": True,
            })
        )
        grape_buyers = grape_buyers.explode(column=["grapes_seeking", "volume_seeking"])
        grape_buyers.rename(columns={"grapes_seeking": "variety", "volume_seeking": "tons"}, inplace=True)
        grape_buyers["side"] = "Buyer"
        grape_buyers["tons"] = Series([int(num) for num in grape_buyers["tons"]])

        grape_sellers = DataFrame(self.db.projection("GrapeSellers", {}, {
                "_id": False,
                "profile_id": True,
                "grapes_selling": True,
                "volume_selling": True,
            })
        )

        grape_sellers = grape_sellers.explode(column=["grapes_selling", "volume_selling"])
        grape_sellers.rename(columns={"grapes_selling": "variety", "volume_selling": "tons"}, inplace=True)
        grape_sellers["side"] = "Seller"
        grape_sellers["tons"] = Series([int(num) for num in grape_sellers["tons"]])

        together = merge(grape_buyers, grape_sellers, how='inner', on=['variety'])
        together = together.loc[(together.tons_x <= together.tons_y)]
        together["tons_difference"] = together["tons_y"] - together["tons_x"]

        buyer_indexes = (together[together["profile_id_x"] == buyer_id]).index.to_list()
        seller_profile_id = [together.iloc[num]["profile_id_y"] for num in buyer_indexes]
        return seller_profile_id[:n_matches]

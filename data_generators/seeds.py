from app.data import MongoDB
from data_generators.generators import RandomGrapeBuyer, RandomGrapeSeller
from tests.schema_validation import validate_schemas


class SeedMongo:
    validate_schemas()
    db = MongoDB()

    def grape_buyers(self, fresh_db: bool, count: int):
        if not fresh_db:
            self.db.delete("GrapeBuyers", {})
            self.db.drop_index("GrapeBuyers")
        else:
            self.db.make_field_unique("GrapeBuyers", "profile_id")
        self.db.create_index("GrapeBuyers")
        grape_buyers = (vars(RandomGrapeBuyer()) for _ in range(count))
        self.db.create_many("GrapeBuyers", grape_buyers)

    def grape_sellers(self, fresh_db: bool, count: int):
        if not fresh_db:
            self.db.delete("GrapeSellers", {})
            self.db.drop_index("GrapeSellers")
        else:
            self.db.make_field_unique("GrapeSellers", "profile_id")
        self.db.create_index("GrapeSellers")
        grape_sellers = (vars(RandomGrapeSeller()) for _ in range(count))
        self.db.create_many("GrapeSellers", grape_sellers)

    def __call__(self, fresh: bool):
        self.grape_buyers(fresh, 100)
        self.grape_sellers(fresh, 20)


if __name__ == '__main__':
    seed_mongo = SeedMongo()
    seed_mongo(fresh=False)

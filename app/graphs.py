from app.data import MongoDB
from pandas import DataFrame, concat, Series
from altair import Chart, Color, Y, X, Tooltip


def title_fix(string: str) -> str:
    return string.title().replace("_", " ")


def stacked_bar_chart(df: DataFrame, column_1: str, column_2: str, column_3: str) -> Chart:
    return Chart(
        df,
        title=f"{title_fix(column_1)} by {title_fix(column_2)} by {title_fix(column_3)}",
    ).mark_bar().encode(
        x=X(column_3, title=title_fix(column_3), sort="-y"),
        y=Y(column_1),
        color=Color(column_2, title=title_fix(column_2)),
        tooltip=Tooltip([column_2, column_3, column_1])
    ).properties(
        width=480,
        height=400,
        padding=24,
    ).configure(
        legend={"padding": 24},
        title={"fontSize": 20, "offset": 24},
        view={"stroke": "#FFF"},
    )


def grouped_by_chart(df: DataFrame, column_1: str, column_2: str, column_3: str) -> Chart:
    return Chart(df).mark_bar().encode(
        x=column_2,
        y=column_3,
        color=column_2,
        column=column_1
    )


def df_grapes_by_side(database: MongoDB) -> DataFrame:
    grape_buyers = DataFrame(database.projection("GrapeBuyers", {}, {"grapes_seeking": True, "volume_seeking": True}))
    grape_buyers = grape_buyers.explode(column=["grapes_seeking", "volume_seeking"])
    grape_buyers.rename(columns={"grapes_seeking": "variety", "volume_seeking": "tons"}, inplace=True)
    grape_buyers["side"] = "Buyer"
    grape_buyers["tons"] = Series([int(num) for num in grape_buyers["tons"]])
    grape_buyers = grape_buyers.groupby(["variety", "side"]).agg({"tons": "sum"}).reset_index()

    grape_sellers = DataFrame(database.projection("GrapeSellers", {}, {"grapes_selling": True, "volume_selling": True}))
    grape_sellers = grape_sellers.explode(column=["grapes_selling", "volume_selling"])
    grape_sellers.rename(columns={"grapes_selling": "variety", "volume_selling": "tons"}, inplace=True)
    grape_sellers["side"] = "Seller"
    grape_sellers["tons"] = Series([int(num) for num in grape_sellers["tons"]])
    grape_sellers = grape_sellers.groupby(["variety", "side"]).agg({"tons": "sum"}).reset_index()
    return concat([grape_buyers, grape_sellers])

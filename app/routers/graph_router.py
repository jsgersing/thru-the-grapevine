from fastapi import APIRouter
from app.graphs import stacked_bar_chart, df_grapes_by_side, df_grapes_by_state_buyer, df_grapes_by_state_seller, \
    grouped_bar_chart, df_tons_by_state_combined, donut_chart, df_tons_by_variety_buyer, df_tons_by_variety_seller
from app.data import MongoDB


Router = APIRouter(
    prefix="/graph",
    tags=["Graph Operations"]
)


@Router.get("/df-grapes-by-side")
async def grapes_by_side():
    """ Variety Volume by Side - stacked bar chart
    Returns an Altair Chart in JSON format """
    return stacked_bar_chart(
        df_grapes_by_side(MongoDB()),
        "tons",
        "side",
        "variety"
    ).to_dict()


@Router.get("/df-grapes-by-state-buyer")
async def grapes_by_state_buyer():
    """ Variety Volume by State for Buyers - stacked bar chart
    Returns an Altair Chart in JSON format """
    return stacked_bar_chart(
        df_grapes_by_state_buyer(MongoDB()),
        "tons",
        "state",
        "variety"
    ).to_dict()


@Router.get("/df-grapes-by-state-seller")
async def grapes_by_state_seller():
    """ Variety Volume by State for Sellers - stacked bar chart
    Returns an Altair Chart in JSON format """
    return stacked_bar_chart(
        df_grapes_by_state_seller(MongoDB()),
        "tons",
        "state",
        "variety"
    ).to_dict()


@Router.get("/df-grapes-by-state-combined")
async def tons_by_state_combined():
    """ Variety Volume by Side by State - Grouped bar chart
    Returns an Altair Chart in JSON format """
    return grouped_bar_chart(
        df_tons_by_state_combined(MongoDB()),
        "tons",
        "side",
        "variety",
        "state"
    ).to_dict()


@Router.get("/df-tons-by-variety-buyer")
async def tons_by_variety_buyer():
    """ Variety Volume for Buyer - Donut Chart
    Returns an Altair Chart in JSON format """
    return donut_chart(
        df_tons_by_variety_buyer(MongoDB()),
        "variety",
        "tons"
    ).to_dict()


@Router.get("/df-tons-by-variety-seller")
async def tons_by_variety_seller():
    """ Variety Volume for Seller - Donut Chart
    Returns an Altair Chart in JSON format """
    return donut_chart(
        df_tons_by_variety_seller(MongoDB()),
        "variety",
        "tons"
    ).to_dict()

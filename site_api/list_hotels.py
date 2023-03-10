from aiohttp import ClientSession

from loader import RAPID_API_TOKEN
from .details_hotel import request_hotels_detail

payload = {
    "currency": "USD",
    "eapid": 1,
    "locale": "ru_RU",
    "siteId": 300000001,
    "destination": {"regionId": "3023"},
    "checkInDate": {
        "day": 4,
        "month": 3,
        "year": 2023
    },
    "checkOutDate": {
        "day": 10,
        "month": 3,
        "year": 2023
    },
    "rooms": [
        {
            "adults": 1,
            "children": []
        }
    ],
    "resultsStartingIndex": 0,
    "resultsSize": 1000,
    "sort": "PRICE_LOW_TO_HIGH",
    "filters": {"price": {
        "max": 2000,
        "min": 1
    }}
}

user_info = {"quantity": 0,
             "high": False,
             "distance": None}


async def request_hotels(quantity_photo: int = None, payload_info: dict = None,
                         quantity_hotels: int = None):

    async with ClientSession() as hotels_session:

        url = "https://hotels4.p.rapidapi.com/properties/v2/list"

        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": RAPID_API_TOKEN,
            "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
        }

        payload_detail = {
            "currency": "USD",
            "eapid": 1,
            "locale": "ru_RU",
            "siteId": 300000001,
            "propertyId": "2528760"
        }

        list_info_hotels = []

        async with hotels_session.post(url, json=payload_info, headers=headers) as hotels_response:

            if hotels_response.ok:

                try:

                    hotels_json = await hotels_response.json()

                    if user_info["high"]:
                        list_hotel = hotels_json["data"]["propertySearch"]["properties"][::-1]
                        user_info["high"] = False
                    elif user_info["distance"]:
                        list_hotel = [hot for hot in hotels_json["data"]["propertySearch"]["properties"]
                                      if hot["destinationInfo"]["distanceFromDestination"]["value"]
                                      <= user_info["distance"]
                                      ]
                        user_info["distance"] = None
                    else:
                        list_hotel = hotels_json["data"]["propertySearch"]["properties"]

                    for hotel in list_hotel[:quantity_hotels]:

                        payload_detail["propertyId"] = hotel["id"]

                        list_info_hotels.append((hotel["price"]["lead"]["formatted"],
                                                hotel["price"]["displayMessages"][1]["lineItems"][0]["value"].split()[0],
                                                hotel["name"],
                                                f"https://www.hotels.com/h{hotel['id']}" +
                                                 '.Hotel-Information',
                                                 hotel["propertyImage"]["image"]["url"],
                                                 await request_hotels_detail(payload_info=payload_detail,
                                                                             headers=headers,
                                                                             quantity_photo=quantity_photo),
                                                 hotel["destinationInfo"]["distanceFromDestination"]["value"]

                                                 ))
                except (KeyError, TypeError):
                    pass

    return list_info_hotels
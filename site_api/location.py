from aiohttp import ClientSession
from loader import RAPID_API_TOKEN


async def request_location(location=None) -> list:

    list_location = []

    if location:

        async with ClientSession() as location_session:

            url = "https://hotels4.p.rapidapi.com/locations/v3/search"

            querystring = {"q": location, "locale": "ru_RU", "langid": "1033", "siteid": "300000001"}

            headers = {"X-RapidAPI-Key": RAPID_API_TOKEN,
                       "X-RapidAPI-Host": "hotels4.p.rapidapi.com"}

            async with location_session.get(url=url, headers=headers, params=querystring) as location_response:

                if location_response.ok:

                    location_json = await location_response.json()

                    for loc in location_json["sr"]:
                        if loc["@type"] == "gaiaRegionResult":
                            list_location.append([loc["regionNames"]["fullName"], loc["gaiaId"]])

    return list_location

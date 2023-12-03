from aiohttp import ClientSession


async def request_hotels_detail(quantity_photo: int = None,
                                payload_info: dict = None, headers: dict = None):

    url_photo_list = []

    async with ClientSession() as detail_session:

        url = "https://hotels4.p.rapidapi.com/properties/v2/detail"

        async with detail_session.post(url, json=payload_info, headers=headers) as detail_response:

            if detail_response.ok:
                detail_json = await detail_response.json()
                address = detail_json["data"]["propertyInfo"]["summary"]["location"]["address"]["addressLine"]

                if quantity_photo:
                    for info_hotel in detail_json["data"]["propertyInfo"]["propertyGallery"]["images"]:
                        if len(url_photo_list) >= quantity_photo:
                            break
                        url_photo_list.append(info_hotel["image"]["url"])
                else:
                    url_photo_list = None

    return address, url_photo_list


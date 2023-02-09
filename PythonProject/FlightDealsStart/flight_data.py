import requests

class FlightData:
    #This class is responsible for structuring the flight data.

    def compareLowestPrice(self, cheapest_ticket):

        # Compare the lowest price and then edit data from google sheet
        BEARER_TOKEN = "Bearer askldjaskldj1201234908asdnklasd091njkxzn90012094u1912e"

        ticket_header = {
            "Authorization": BEARER_TOKEN,
            "Content-Type" : "application/json"
        }

        for info in cheapest_ticket:
            update_price_on_sheet_url = f"https://api.sheety.co/714305910239e5787bf0d55849d16ac1/flightDealsSb/prices/{info['id']}"
            ticket_info_body = {
                "price": {
                    "city": info["cityTo"],
                    "iataCode": info["iataCode"],
                    "lowestPrice": info["lowestPrice"]
                }
            }

            response = requests.put(url=update_price_on_sheet_url, json=ticket_info_body, headers=ticket_header)
            response.raise_for_status()
            print(response.text)
            print()

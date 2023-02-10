import requests

class FlightData:
    #This class is responsible for structuring the flight data.

    def __init__(self, stop_overs, via_city, origin_city, origin_airport, destination_city, destination_airport, date_from, date_to, id, iataCode, lowestPrice):
        self.stop_overs = stop_overs
        self.via_city = via_city
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.date_from = date_from
        self.date_to = date_to
        self.id = id
        self.iataCode = iataCode
        self.lowestPrice = lowestPrice


    def compareLowestPrice(self):

        # Compare the lowest price and then edit data from google sheet
        BEARER_TOKEN = "Bearer askldjaskldj1201234908asdnklasd091njkxzn90012094u1912e"

        ticket_header = {
            "Authorization": BEARER_TOKEN,
            "Content-Type" : "application/json"
        }


        update_price_on_sheet_url = f"https://api.sheety.co/714305910239e5787bf0d55849d16ac1/flightDealsSb/prices/{self.id}"
        ticket_info_body = {
            "price": {
                "city": self.destination_city,
                "iataCode": self.iataCode,
                "lowestPrice": self.lowestPrice
            }
        }

        response = requests.put(url=update_price_on_sheet_url, json=ticket_info_body, headers=ticket_header)
        response.raise_for_status()
        print(response.text)
        print()

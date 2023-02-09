import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def retrieveFlightFromSheet(self):
        # Retrieve flight info from google sheet
        flight_info_url = "https://api.sheety.co/714305910239e5787bf0d55849d16ac1/flightDealsSb/prices"
        BEARER_TOKEN = "Bearer askldjaskldj1201234908asdnklasd091njkxzn90012094u1912e"

        ticket_header = {
            "Authorization": BEARER_TOKEN
        }

        response = requests.get(url=flight_info_url, headers=ticket_header)
        response.raise_for_status()
        flight_lists = response.json()

        return flight_lists
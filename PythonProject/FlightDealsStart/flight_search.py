from pprint import pprint

import requests
from datetime import datetime
from dateutil.relativedelta import relativedelta


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def searchFlight(self, flight_lists):

        # Search the cheapest flight from tomorrow to 6 months using Tequlia API
        from_date = datetime.now().strftime("%d/%m/%Y")
        to_date = (datetime.today() + relativedelta(months=+6)).strftime("%d/%m/%Y")

        tequlia_API = "LyNhQMHzNDqgfuGmFGQgjdQzwpUFsIM3"
        search_cheapest_ticket_header = {
            "apikey": tequlia_API
        }

        search_iata_code_url = "https://api.tequila.kiwi.com/locations/query"

        for index in range(0, len(flight_lists["prices"])):
            search_iata_body = {
                "term" : flight_lists["prices"][index]["city"]
            }

            response = requests.get(url=search_iata_code_url, params=search_iata_body, headers=search_cheapest_ticket_header)

            # if flight_lists["prices"][index]["city"] == response.json()["locations"][0]["name"]:
            #     flight_lists["prices"][index]["iataCode"] = response.json()["locations"][0]["code"]
            try:
                response.json()["locations"][0]
            except IndexError:
                print(f"----------------------------- No flight for {flight_lists['prices'][index]['city']} -----------------------------")
                del flight_lists["prices"][index]
            else:
                flight_lists["prices"][index]["iataCode"] = response.json()["locations"][0]["code"]


        cheapest_flight_info_url = "https://api.tequila.kiwi.com/v2/search"
        cheapest_ticket = []

        for city in flight_lists["prices"]:
            cheapest_flight_body = {
                "fly_from": "NYC",
                "fly_to": city["iataCode"],
                "date_from": from_date,
                "date_to": to_date,
                "id": city["id"]
            }

            response = requests.get(url=cheapest_flight_info_url, params=cheapest_flight_body, headers=search_cheapest_ticket_header)

            if city["iataCode"] == response.json()["data"][0]["cityCodeTo"] and city["lowestPrice"] > response.json()["data"][0]["price"]:
                tmpDic = {
                    "iataCode": response.json()["data"][0]["cityCodeTo"],
                    "lowestPrice": response.json()["data"][0]["price"],
                    "fly_from": "NYC",
                    "cityTo": response.json()["data"][0]["cityTo"],
                    "date_from": from_date,
                    "date_to": to_date,
                    "id": city["id"]
                }
                cheapest_ticket.append(tmpDic)

        return cheapest_ticket
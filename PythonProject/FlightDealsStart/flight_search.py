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


            if flight_lists["prices"][index]["city"] == response.json()["locations"][0]["name"]:
                flight_lists["prices"][index]["iataCode"] = response.json()["locations"][0]["code"]


        cheapest_flight_info_url = "https://api.tequila.kiwi.com/v2/search"
        cheapest_ticket = []


        for city in flight_lists["prices"]:

            cheapest_flight_body = {
                "fly_from": city["cityFrom"],
                "airport_from": city["flyFrom"],
                "fly_to": city["cityTo"],
                "airport_to": city["flyTo"],
                "date_from": from_date,
                "date_to": to_date,
                "nights_in_dst_from": 7,
                "nights_in_dst_to": 30,
                "flight_type": "round",
                "curr": "USD",
                "one_for_city": 1,
                "max_stopovers": 0,
                "id": city["id"]
            }



            response = requests.get(url=cheapest_flight_info_url, params=cheapest_flight_body, headers=search_cheapest_ticket_header)



            # if city["iataCode"] == response.json()["data"][0]["cityCodeTo"] and city["lowestPrice"] > response.json()["data"][0]["price"]:
            try :
                data = response.json()["data"][0]
            except IndexError:
                print(f"----------------------------- No flight for {city['city']} -----------------------------")

                cheapest_flight_body["max_stopovers"] = 2
                response = requests.get(url=cheapest_flight_info_url, params=cheapest_flight_body, headers=search_cheapest_ticket_header)
                data_stopovers = response.json()["data"][0]

                pprint(data_stopovers)

                tmpDic = {
                    "iataCode": data_stopovers["cityCodeTo"],
                    "lowestPrice": data_stopovers["price"],
                    "fly_from": data_stopovers["route"][0]["cityFrom"],
                    "airport_from": data_stopovers["route"][0]["flyFrom"],
                    "city_to": data_stopovers["route"][1]["cityTo"],
                    "airport_to": data_stopovers["route"][1]["flyTo"],
                    "date_from": from_date,
                    "date_to": to_date,
                    "nights_in_dst_from": 7,
                    "nights_in_dst_to": 30,
                    "flight_type": "round",
                    "curr": "USD",
                    "one_for_city": 1,
                    "max_stopovers": cheapest_flight_body["max_stopovers"],
                    "via_city": data_stopovers["cityTo"],
                    "id": city["id"]
                }
                print()
            else:
                tmpDic = {
                    "iataCode": data["cityCodeTo"],
                    "lowestPrice": data["price"],
                    "fly_from": data["cityFrom"],
                    "airport_from": data["flyFrom"],
                    "cityTo": data["cityTo"],
                    "airport_to": data["flyTo"],
                    "date_from": from_date,
                    "date_to": to_date,
                    "nights_in_dst_from": 7,
                    "nights_in_dst_to": 30,
                    "flight_type": "round",
                    "curr": "USD",
                    "one_for_city": 1,
                    "max_stopovers": data["max_stopovers"],
                    "via_city": "",
                    "id": city["id"]
                }
            finally:
                cheapest_ticket.append(tmpDic)

        return cheapest_ticket
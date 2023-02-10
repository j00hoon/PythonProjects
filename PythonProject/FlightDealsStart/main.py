from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

dataManager = DataManager()
flightSearch = FlightSearch()
notificationManager = NotificationManager()

flight_list = dataManager.retrieveFlightFromSheet()
cheapest_ticket = flightSearch.searchFlight(flight_list)

for data in cheapest_ticket:
    flightData = FlightData(data["max_stopovers"], data["via_city"], data["fly_from"], data["airport_from"],
                            data["destination_city"], data["destination_airport"], data["date_from"],
                            data["date_to"], data["id"], data["iataCode"], data["lowestPrice"])
    flightData.compareLowestPrice(cheapest_ticket)

notificationManager.sendNotification(cheapest_ticket)















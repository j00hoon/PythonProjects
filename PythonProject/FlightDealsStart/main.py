from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

dataManager = DataManager()
flightSearch = FlightSearch()
flightData = FlightData()
notificationManager = NotificationManager()

flight_list = dataManager.retrieveFlightFromSheet()
cheapest_ticket = flightSearch.searchFlight(flight_list)
# flightData.compareLowestPrice(cheapest_ticket)
# notificationManager.sendNotification(cheapest_ticket)















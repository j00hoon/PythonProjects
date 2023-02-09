from twilio.rest import Client

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    def sendNotification(self, cheapest_ticket):

        # Send text notification
        TWILIO_ACC_ID = "AC1a305ab447847a279048063326d49dba"
        TWILIO_AUTH_TOKEN = "7016c5d1caf402afae73575b691aca51"
        client = Client(TWILIO_ACC_ID, TWILIO_AUTH_TOKEN)

        notification_body = [f"From : {data['fly_from']}, To : {data['cityTo']}\n" \
                        f"Date from : {data['date_from']}, Date to : {data['date_to']}\n" \
                        f"Arrival city IATA code : {data['iataCode']}, Price : {data['lowestPrice']}\n\n" for data in cheapest_ticket]

        for notification in notification_body:
            message = client.messages.create(
                body=notification,
                from_="+18777152263",
                to="2016915073"
            )
            print(message.status)

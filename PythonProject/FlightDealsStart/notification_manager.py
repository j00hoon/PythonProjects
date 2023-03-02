from twilio.rest import Client
import smtplib

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    def sendNotification(self, cheapest_ticket):

        # Send text notification
        TWILIO_ACC_ID = "AC1a305ab447847a279048063326d49dba"
        TWILIO_AUTH_TOKEN = "7016c5d1caf402afae73575b691aca51"
        client = Client(TWILIO_ACC_ID, TWILIO_AUTH_TOKEN)

        # Send email
        EMAIL = "j00hoon1101@gmail.com"
        PASSWORD = ""
        "STN.SXF.2020-08-25*SXF.STN.2020-09-08"
        URL = f"https://www.google.co.uk/flights?hl=en#flt="

        notification_body = [f"From : {data['fly_from']}, To : {data['cityTo']}\n" \
                        f"Date from : {data['date_from']}, Date to : {data['date_to']}\n" \
                        f"Arrival city IATA code : {data['iataCode']}, Price : {data['lowestPrice']}\n" \
                             f"{URL}{data['fly_from']}.{data['cityTo']}.{data['date_from']}*{data['cityTo']}.{data['fly_from']}.{data['date_to']}"
                             for data in cheapest_ticket]

        # Send text and email
        for notification in notification_body:
            message = client.messages.create(
                body=notification,
                from_="+18777152263",
                to="2016915073"
            )
            print(message.status)

            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=EMAIL, password=PASSWORD)
                connection.sendmail(
                    from_addr=EMAIL,
                    to_addrs="j00hoon1101@gmail.com",
                    msg=notification
                )


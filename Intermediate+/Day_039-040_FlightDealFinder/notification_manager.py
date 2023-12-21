from twilio.rest import Client


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight
    # details.
    def __init__(self, auth_token: str = "", account_sid: str = "", phone_number: str = "", receiver_number: str = "") -> None:
        self.auth_token = auth_token
        self.account_sid = account_sid
        self.phone_number = phone_number
        self.receiver_number = receiver_number

    def set_credentials(
            self,
            auth_token: str = "",
            account_sid: str = "",
            phone_number: str = "",
            receiver_number: str = "",
            ):
        if auth_token != "":
            self.auth_token = auth_token
        if account_sid != "":
            self.account_sid = account_sid
        if phone_number != "":
            self.phone_number = phone_number
        if receiver_number != "":
            self.receiver_number = receiver_number

    def send_message(self, message: str, receiver_number: str):
        """Send message to specified number"""
        client = Client(self.account_sid, self.auth_token)
        response = client.messages.create(
            body=message,
            to=receiver_number,
            from_=self.phone_number
            )
        print(response.status)

    def price_alert(
            self,
            iata_departure: str,
            departure_city: str,
            iata_arrival: str,
            arrival_city: str,
            departure_date: str,
            flight_cost: str,
            ):
        """Sends an alert containing flight info"""
        notice = "Low price alert!"
        price = f"Only €{flight_cost} to fly"
        locations = f"from {departure_city}-{iata_departure} to {arrival_city}-{iata_arrival},"
        dates = f"on {departure_date}."
        message = " ".join([notice, price, locations, dates])
        self.send_message(message=message, receiver_number=self.receiver_number)

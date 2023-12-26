from twilio.rest import Client
import smtplib


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight
    # details.
    def __init__(
            self,
            auth_token: str = "",
            account_sid: str = "",
            phone_number: str = "",
            receiver_number: str = "",
            smtp_email: str = "",
            smtp_password: str = "",
            smtp_receivers: list[dict] = list()
            ) -> None:
        self.auth_token = auth_token
        self.account_sid = account_sid
        self.phone_number = phone_number
        self.receiver_number = receiver_number
        self.smtp_email = smtp_email
        self.smtp_password = smtp_password
        self.smtp_receivers = smtp_receivers

    def set_credentials(
            self,
            auth_token: str = "",
            account_sid: str = "",
            phone_number: str = "",
            receiver_number: str = "",
            smtp_email: str = "",
            smtp_password: str = "",
            smtp_receivers: list[dict] = list(),
            ):
        if auth_token != "":
            self.auth_token = auth_token
        if account_sid != "":
            self.account_sid = account_sid
        if phone_number != "":
            self.phone_number = phone_number
        if receiver_number != "":
            self.receiver_number = receiver_number
        if smtp_email != "":
            self.smtp_email = smtp_email
        if smtp_password != "":
            self.smtp_password = smtp_password
        if len(smtp_receivers) > 0:
            self.smtp_receivers = smtp_receivers

    def send_message(self, message: str, receiver_number: str):
        """Send message to specified number"""
        client = Client(self.account_sid, self.auth_token)
        response = client.messages.create(
            body=message,
            to=receiver_number,
            from_=self.phone_number
            )
        print(response.status)

    def send_emails(self, message: str, receiver_emails: list):
        with smtplib.SMTP("smtp.gmail.com") as server:
            server.starttls()
            server.login(user=self.smtp_email, password=self.smtp_password)
            for receipient in receiver_emails:
                personal_message = f"Good news {receipient['name']} {receipient['surname']}!\n{message}"
                personal_message = f"Subject:Flight Deal Price Alert\n\n{personal_message}"
                server.sendmail(from_addr=self.smtp_email, to_addrs=receipient["email"], msg=personal_message.encode("utf-8"))

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
        price = f"Only {'€'}{flight_cost} to fly"
        locations = f"from {departure_city}-{iata_departure} to {arrival_city}-{iata_arrival},"
        dates = f"on {departure_date}."
        message = " ".join([notice, price, locations, dates])
        # self.send_message(message=message, receiver_number=self.receiver_number)
        self.send_emails(message=message, receiver_emails=self.smtp_receivers)

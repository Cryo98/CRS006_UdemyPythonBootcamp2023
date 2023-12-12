SHEETY_ENDPOINT = "https://api.sheety.co/"


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self.token = ""
        self.url = ""

    def set_authentication(self, token):
        self.token = token

    def set_sheet(self, url):
        self.url = SHEETY_ENDPOINT + url

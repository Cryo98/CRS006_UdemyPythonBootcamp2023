SHEETY_ENDPOINT = "https://api.sheety.co/"


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self.token = ""
        self.url = ""
        self.authentication_set = False
        self.sheet_set = False

    def set_authentication(self, token):
        self.token = token
        self.authentication_set = True

    def set_sheet(self, url):
        self.url = SHEETY_ENDPOINT + url
        self.sheet_set = True

    def check_response(self, func):
        """Checks"""
        def run_until(kwargs):
            status_code = 503
            while status_code == 503:
                response = func(**kwargs)
                status_code = response.status_code
            return response
        return run_until

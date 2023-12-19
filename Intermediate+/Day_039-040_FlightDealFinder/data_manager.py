import requests

SHEETY_ENDPOINT = "https://api.sheety.co/"


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self.token = ""
        self.url = ""
        self.authentication_set = False
        self.sheet_set = False

    def set_authentication(self, token) -> None:
        self.token = token
        self.header = {"Authorization": f"Bearer {token}"}
        self.authentication_set = True

    def set_sheet(self, url) -> None:
        self.url = SHEETY_ENDPOINT + url
        self.sheet_set = True

    @staticmethod
    def check_response(func):
        """Checks the response from a HTTP request and handles errors."""
        def wrapper(self, *args, **kwargs) -> requests.Response | None:
            response: requests.Response
            if not self.authentication_set or not self.sheet_set:
                print("No valid authentication and sheet have been chosen.")
                print("Please set them using 'set_authentication' and 'set_sheet'.")
                return None
            response: requests.Response = func(self, *args, **kwargs)
            try:
                response.raise_for_status()
            except requests.HTTPError as error:
                if response.status_code == 401:
                    print("Invalid authorization, please insert the correct token.")
                else:
                    print(f"HTTP Error occurred: {error}")
            finally:
                return response
        return wrapper

    @check_response
    def get_data(self) -> requests.Response:
        response = requests.get(self.url, headers=self.header)
        return response

    @check_response
    def set_data(self, row: int, body: dict) -> requests.Response:
        header = self.header
        header["Content-Type"] = "application/json"
        response = requests.put(self.url + f"/{row}", json=body, headers=header)
        return response

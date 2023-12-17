import requests

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
        self.header = {"Authorization": f"Bearer {token}"}
        self.authentication_set = True

    def set_sheet(self, url):
        self.url = SHEETY_ENDPOINT + url
        self.sheet_set = True

    def get_data(self) -> requests.Response:
        response = requests.get(self.url, headers=self.header)
        return response

    def set_data(self, row: int, column: str, data) -> requests.Response:
        print(self.url + f"/{row}")
        header = self.header
        header["Content-Type"] = "application/json"
        body = {
            column: data,
        }
        response = requests.post(self.url + f"/{row}", json=body, headers=header)
        return response

    def check_response(self, func):
        """Checks the response from a HTTP request and handles errors."""
        def request_checked(kwargs):
            response: requests.Response
            if not self.authentication_set or not self.sheet_set:
                print("No valid authentication and sheet have been chosen.")
                print("Please set them using 'set_authentication' and 'set_sheet'.")
                return None
            try:
                response = func(**kwargs)
                response.raise_for_status()
            except requests.HTTPError:
                if response.status_code == 401:
                    print("Invalid authorization, please insert the correct token.")
            finally:
                return response
        return request_checked

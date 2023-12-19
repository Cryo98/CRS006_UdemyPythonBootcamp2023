from data_manager import DataManager


class FlightData(DataManager):
    # This class is responsible for structuring the flight data.
    def __init__(self) -> None:
        super().__init__()

    def set_iata_code(self, code: str, idx: int) -> bool:
        body = {
            "prices": {
                "iataCode": code
            }
        }
        response = self.set_data(row=idx+2, body=body)
        return response.status_code == 200

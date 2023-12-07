import requests
import os
from datetime import datetime

# TODO: update docs

# TODO: think about how to handle credentials, maybe global variable that can
# be set using a function? Or maybe handled by the app, and the input is
# always required

# TODO: Convert date input into datetime object and apply format inside the
# function (or directly using another function)

PIXELA_API_USER = "https://pixe.la/v1/users"
# TODO: make it insertable within the app, not here
PIXELA_USER = "cryo"

pixela_token = os.environ.get("PIXELA_TOKEN", "")


# TODO: convert it into a decorator that can run a function multiple times
# based on the error type (in particular error 503 for the random 25% chance)
def response_error_handler(response: requests.Response):
    """Handles errors"""
    try:
        response.raise_for_status()
        print(response.json()["message"])
    except requests.HTTPError:
        print(f"Error <{response.status_code}>")
        print(response.json()["message"])


# USER
def create_user(username: str, token: str):
    """Creates a new user using the PIXELA_USER as name"""
    params = {
        "token": token,
        "username": username,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }
    response = requests.post(url=PIXELA_API_USER, json=params)
    response_error_handler(response)


# GRAPHS
def create_graph(
        username: str,
        token: str,
        id: str,
        name: str = "Unnamed Graph",
        unit: str = "Times",
        type: str = "int",
        color: str = "sora"
        ):
    """Creates a new graph with the given characteristics.

    Parameters
    ----------
    id : str
        unique ID of the graph to use
    name : str, optional
        Name of the graph to show, by default "Unnamed Graph"
    unit : str, optional
        Unit which the quantity represents, by default "Times"
    type : str, optional
        If the quantity is an integer (int) or a floating point (float), by
        default "int"
    color : str, optional
        Shade to use to color the graph, list available at
        https://docs.pixe.la/entry/post-graph, by default "sora"
    """
    header = {
        "X-USER-TOKEN": token,
    }

    params = {
        "id": id,
        "name": name,
        "unit": unit,
        "type": type,
        "color": color,
    }
    request_url = PIXELA_API_USER + f"/{username}/graphs"
    response = requests.post(url=request_url, headers=header, json=params)
    response_error_handler(response)


# PIXELS
def add_pixel_to_graph(
        username: str,
        token: str,
        graph_id: str,
        date: str = datetime.today().strftime("%Y%m%d"),
        quantity: str = "1"
        ):
    """Adds a pixel at the requested graph and date with the given
    quantity

    Parameters
    ----------
    graph_id : str
        id of the graph.
    date : str, optional
        string representing the date where the pixel is to be removed,
        following the format %Y%m%d, by default
        datetime.today().strftime("%Y%m%d").
    quantity : str, optional
        value to insert, by default "1"
    """
    header = {
        "X-USER-TOKEN": token,
    }

    params = {
        "date": date,
        "quantity": quantity,
    }

    response = requests.post(
        url=f"{PIXELA_API_USER}/{username}/graphs/{graph_id}",
        headers=header,
        json=params
        )
    response_error_handler(response)


def update_pixel_in_graph(
        username: str,
        token: str,
        graph_id: str,
        date: str = datetime.today().strftime("%Y%m%d"),
        quantity: str = "1"
        ):
    """Updates the pixel at the requested graph and date with the given
    quantity

    Parameters
    ----------
    graph_id : str
        id of the graph.
    date : str, optional
        string representing the date where the pixel is to be removed,
        following the format %Y%m%d, by default
        datetime.today().strftime("%Y%m%d").
    quantity : str, optional
        value to insert, by default "1"
    """
    header = {
        "X-USER-TOKEN": token,
    }

    params = {
        "quantity": quantity,
    }

    response = requests.put(
        url=f"{PIXELA_API_USER}/{username}/graphs/{graph_id}/{date}",
        headers=header,
        json=params
        )
    response_error_handler(response)


def delete_pixel_in_graph(
        username: str,
        token: str,
        graph_id: str,
        date: str = datetime.today().strftime("%Y%m%d"),
        ):
    """Deletes the pixel at the specified date in the given graph

    Parameters
    ----------
    graph_id : str
        id of the graph in which to remove the pixel.
    date : str, optional
        string representing the date where the pixel is to be removed,
        following the format %Y%m%d, by default
        datetime.today().strftime("%Y%m%d").
    """
    header = {
        "X-USER-TOKEN": token,
    }

    response = requests.delete(
        url=f"{PIXELA_API_USER}/{username}/graphs/{graph_id}/{date}",
        headers=header,
        )
    response_error_handler(response)

import requests
import os
from datetime import datetime


PIXELA_API_USER = "https://pixe.la/v1/users"
PIXELA_USER = "cryo"
PIXELA_API_GRAPHS = f"https://pixe.la/v1/users/{PIXELA_USER}/graphs"

TEST_GRAPH = {
    "id": "test",
    "name": "Unnamed Graph",
    "unit": "Times",
    "type": "int",
    "color": "sora"
}

pixela_token = os.environ.get("PIXELA_TOKEN", "")


def create_user():
    """Creates a new user using the PIXELA_USER as name"""
    params = {
        "token": pixela_token,
        "username": PIXELA_USER,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }
    response = requests.post(url=PIXELA_API_USER, json=params)
    try:
        response.raise_for_status()
        print(response.json()["message"])
    except requests.HTTPError:
        print(f"Error <{response.status_code}>")
        print(response.json()["message"])


def create_graph(
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
        "X-USER-TOKEN": pixela_token,
    }

    params = {
        "id": id,
        "name": name,
        "unit": unit,
        "type": type,
        "color": color,
    }
    response = requests.post(url=PIXELA_API_GRAPHS, headers=header, json=params)
    try:
        response.raise_for_status()
        print(response.json()["message"])
    except requests.HTTPError:
        print(f"Error <{response.status_code}>")
        print(response.json()["message"])


def add_pixel_to_graph(
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
        "X-USER-TOKEN": pixela_token,
    }

    params = {
        "date": date,
        "quantity": quantity,
    }

    response = requests.post(
        url=f"{PIXELA_API_GRAPHS}/{graph_id}",
        headers=header,
        json=params
        )
    try:
        response.raise_for_status()
        print(response.json()["message"])
    except requests.HTTPError:
        print(f"Error <{response.status_code}>")
        print(response.json()["message"])


def update_pixel_in_graph(
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
        "X-USER-TOKEN": pixela_token,
    }

    params = {
        "quantity": quantity,
    }

    response = requests.put(
        url=f"{PIXELA_API_GRAPHS}/{graph_id}/{date}",
        headers=header,
        json=params
        )
    try:
        response.raise_for_status()
        print(response.json()["message"])
    except requests.HTTPError:
        print(f"Error <{response.status_code}>")
        print(response.json()["message"])


def delete_pixel_in_graph(
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
        "X-USER-TOKEN": pixela_token,
    }

    response = requests.delete(
        url=f"{PIXELA_API_GRAPHS}/{graph_id}/{date}",
        headers=header,
        )
    try:
        response.raise_for_status()
        print(response.json()["message"])
    except requests.HTTPError:
        print(f"Error <{response.status_code}>")
        print(response.json()["message"])


if __name__ == "__main__":
    create_user()
    create_graph(**TEST_GRAPH)
    add_pixel_to_graph(graph_id=TEST_GRAPH["id"], quantity="1")
    update_pixel_in_graph(graph_id=TEST_GRAPH["id"], quantity="2")
    delete_pixel_in_graph(graph_id=TEST_GRAPH["id"])

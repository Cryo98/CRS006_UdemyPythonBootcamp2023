import pixela
import os
# from app import HabitTracker


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


if __name__ == "__main__":
    pixela.create_user(username=PIXELA_USER, token=pixela_token)
    pixela.create_graph(username=PIXELA_USER, token=pixela_token, **TEST_GRAPH)
    pixela.add_pixel_to_graph(username=PIXELA_USER, token=pixela_token, graph_id=TEST_GRAPH["id"], quantity="1")
    pixela.update_pixel_in_graph(username=PIXELA_USER, token=pixela_token, graph_id=TEST_GRAPH["id"], quantity="2")
    pixela.delete_pixel_in_graph(username=PIXELA_USER, token=pixela_token, graph_id=TEST_GRAPH["id"])

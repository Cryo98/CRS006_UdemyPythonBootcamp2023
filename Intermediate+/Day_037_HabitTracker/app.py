import tkinter as tk


class HabitTracker(tk.Tk):

    def __init__(self, screenName: str | None = None, baseName: str | None = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: str | None = None) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.title("Habit Tracker")
        self.geometry("500x700")
        self.mainloop()

    def __init_graph_canvas(self):
        """Initializes the canvas showing the graph"""
        self.graph = tk.Canvas(width=400, height=200)
        self.graph.grid(column=0, row=0)

    def __init_buttons(self):
        """Initializes the control buttons"""
        pass


if __name__ == "__main__":
    app = HabitTracker()

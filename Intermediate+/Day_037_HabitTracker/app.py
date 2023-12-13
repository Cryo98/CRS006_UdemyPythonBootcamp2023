import tkinter as tk


class HabitTracker(tk.Tk):

    def __init__(self, screenName: str | None = None, baseName: str | None = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: str | None = None) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.title("Habit Tracker")
        self.geometry("500x700")
        self.graphs = [""]
        self.graph = tk.StringVar()
        self.__init_graph_canvas()
        self.__init_buttons()
        self.mainloop()

    def __init_graph_canvas(self):
        """Initializes the canvas showing the graph"""
        self.graph_canvas = tk.Canvas(width=400, height=200)
        self.graph_canvas.grid(column=0, row=0, columnspan=2)
        self.habit_plot = tk.Canvas(width=400, height=100)
        self.habit_plot.grid(column=0, row=2, columnspan=2)

    def __init_buttons(self):
        """Initializes the control buttons"""
        self.add_button = tk.Button(text="Add entry")
        self.add_button.grid(column=0, row=1)
        self.graphs_list = tk.OptionMenu(self, self.graph, *self.graphs)
        self.graphs_list.grid(column=1, row=1)
        pass


if __name__ == "__main__":
    app = HabitTracker()

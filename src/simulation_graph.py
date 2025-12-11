import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class SimulationGraph:
    def __init__(self) -> None:
        """
        Initialize the simulation graph with Tkinter and Matplotlib.
        Sets up the main window, figure, axes, and line objects for tunas, sharks, and megalodons.
        Also initializes lists to store chronon and population data.
        Also configures the visual appearance of the graph.
        """
        
        self.root = tk.Tk()
        self.root.title("Population Graph")
        self.root.configure(bg="#05668D")

        self.fig = Figure(figsize=(8, 6), facecolor="#217CA0")
        self.ax = self.fig.add_subplot(111, facecolor="#217CA0")

        self.chronons = []
        self.tunas = []
        self.sharks = []
        self.megalodons = []

        self.line_tunas, = self.ax.plot([], [], label="Tunas", color="#00D9FF", linewidth=2.5)
        self.line_sharks, = self.ax.plot([], [], label="Sharks", color="#FF4444", linewidth=2.5)
        self.line_megalodons, = self.ax.plot([], [], label="Megalodons", color="#00FF88", linewidth=2.5)
        
        legend = self.ax.legend(facecolor="#05668D", edgecolor="white", fontsize=11, framealpha=0.9)
        for text in legend.get_texts():
            text.set_color("white")
        
        self.ax.set_xlabel("Chronons", fontsize=12, color="white", fontweight="bold")
        self.ax.set_ylabel("Population", fontsize=12, color="white", fontweight="bold")
        self.ax.set_title("Population Over Time", fontsize=24, fontweight="bold", color="white", pad=20)
        self.ax.legend()
        self.ax.grid(True, color="white", alpha=0.3, linestyle="--", linewidth=0.5)
        for spine in self.ax.spines.values():
            spine.set_color("white")
            spine.set_linewidth(1.5)
        
        self.ax.tick_params(colors="white", labelsize=10)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.canvas.get_tk_widget().configure(bg="#05668D")
    
    def show(self):
        """
        Display the Tkinter window with the graph.
        """
        
        self.root.mainloop()
    
    def update(self, chronon, tunas, sharks, megalodons):
        """
        Update the graph with new population data.
        
        Parameters:
            chronon (int): Current chronon number
            tunas (int): Current tuna population
            sharks (int): Current shark population
            megalodons (int): Current megalodon population
        """
        
        self.chronons.append(chronon)
        self.tunas.append(tunas)
        self.sharks.append(sharks)
        self.megalodons.append(megalodons)
        
        self.line_tunas.set_data(self.chronons, self.tunas)
        self.line_sharks.set_data(self.chronons, self.sharks)
        self.line_megalodons.set_data(self.chronons, self.megalodons)
        
        self.ax.relim()          
        self.ax.autoscale_view()
        
        self.canvas.draw()
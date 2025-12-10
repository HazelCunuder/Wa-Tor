import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class SimulationGraph:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Population Graph")
        
        self.fig = Figure(figsize=(8, 6))
        self.ax = self.fig.add_subplot(111)
        
        self.chronons = []
        self.tunas = []
        self.sharks = []
        self.megalodons = []
        
        self.line_tunas, = self.ax.plot([], [], label='Tunas', color='blue')
        self.line_sharks, = self.ax.plot([], [], label='Sharks', color='red')
        self.line_megalodons, = self.ax.plot([], [], label='Megalodons', color='green')
        
        self.ax.set_xlabel('Chronons')
        self.ax.set_ylabel('Population')
        self.ax.set_title('Population Over Time')
        self.ax.legend()
        self.ax.grid(True)
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()
    
    def show(self):
        self.root.mainloop()
    
    def update(self, chronon, tunas, sharks, megalodons):
        """
        Add new data point and redraw the graph.
        
        Args:
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
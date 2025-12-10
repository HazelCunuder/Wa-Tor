import psycopg2
from configparser import ConfigParser
from pathlib import Path

class DataManager:
    def __init__(self) -> None:
        """
        Initialize the DataManager and load database credentials from config file.
        
        Reads database connection parameters from a local 'database.ini' file rather than hardcoding them.
        This was done to keep the credentials out of the code by keeping it on a local platform rather than an online repository

        Raises:
            KeyError: If the expected sections or keys are missing from the config file.
            FileNotFoundError: If the database.ini file does not exist.
        """
        
        self.filename = Path(__file__).parent / "database.ini"
        self.config = ConfigParser()
        self.config.read(self.filename)
        self.host = self.config["postgresql"]["host"]
        self.database = self.config["postgresql"]["database"]
        self.user = self.config["postgresql"]["user"]
        self.password = self.config["postgresql"]["password"]

    
    def connect_to_db(self) -> None:
        """
        Connect to the PSQL database.
        
        Creates a database connection using the credentials loaded during initialization and stores both the connection and cursor as instance variables.
        
        We create instance variables at this moment and not during initializations because we do not want to connect to the database before it is necessary.
        Adding them here lets us access those only when needed to save some data.        
        """
        
        self.connection = psycopg2.connect(
            host= self.host,
            database=self.database, 
            user=self.user, 
            password=self.password
        )
        
        self.cursor = self.connection.cursor()
    
    def save_sim_data(self, results_dict: dict):
        """
        Save simulation data to the database and return the generated simulation ID.
        
        Extracts simulation parameters from the results dictionary and inserts them into our table before returning the simulation id.
        
        We created 2 different save methods because they are both independent from one another.
        We fetch the id so that we can link the chronon data to the correct simulation.
        
        Parameters:
            results_dict (dict): A dictionary containing simulation results with keys:
                - 'experiment_date' (str or datetime): When the simulation was run
                - 'hours' (int): Hour component of simulation duration
                - 'minutes' (int): Minute component of simulation duration
                - 'grid_height' (int): Height of the simulation grid in units
                - 'grid_width' (int): Width of the simulation grid in units
                - 'chronons_reached' (int): Number of time steps completed
                
        Returns:
            simulation_id: int: The id of the simulation we just saved in our table. It will be used as a parameter in the
            save_chronon_data() method, to link the recorded history to this simulation.
        """
        
        self.connect_to_db()
        
        self.cursor.execute("""
                            INSERT INTO simulation (experiment_date, hours, minutes, grid_height, grid_width, chronons_reached)
                            VALUES (%s, %s, %s, %s, %s, %s)
                            RETURNING id
                            """,
                            (
                            results_dict["experiment_date"], 
                            results_dict['hours'],
                            results_dict['minutes'],
                            results_dict['grid_height'],
                            results_dict['grid_width'],
                            results_dict['chronons_reached']
                            )
                            )
        simulation_id = self.cursor.fetchone()[0] #type: ignore
        
        self.connection.commit()
        self.disconnect_from_db()
        
        return simulation_id
        
    def save_chronon_data(self, sim_id: int, chronon_history: list):
        """
        Save the data in our simulation at certain chronon intervals.
        
        We turn our simulation data at a given chronon into a tuple with the id of the simulation it happened in.
        We then insert everything at once with a batch insert.
        
        We decided to do it this way because it was more efficient than doing a for loop and inserting them one by one.
        
        Parameters:
            sim_id (int): The simulation ID we got from the save_sim_data() method. Used to link this save to the correct simulation
            chronon_history (list): A list of tuples, where each tuple contains:
                - [0] current_chronon (int): The time step number
                - [1] nb_tunas (int): Number of tuna at this time step
                - [2] nb_sharks (int): Number of shark at this time step
                - [3] nb_megalodons (int): Number of megalodon at this time step
        """
        
        history: list = []
        
        for index, data_tuple in enumerate(chronon_history):
            current_sim = (data_tuple[0], data_tuple[1], data_tuple[2], data_tuple[3], sim_id)
            
            history.append(current_sim)
            
        self.connect_to_db()
        
        self.cursor.executemany("""
                                INSERT INTO current_sim (current_chronon, nb_tunas, nb_sharks, nb_megalodons, simulation_id)
                                VALUES (%s, %s, %s, %s, %s)
                                """, history
                                )
        
        self.connection.commit()
        self.disconnect_from_db()
    
    def disconnect_from_db(self):
        """
        Close the database cursor and connection once we no longer need to be connected to it.
        
        This method ensures that database resources are properly released after each
        operation, preventing connection leaks and allowing the database to manage
        its connection pool efficiently. Called after each transaction completes.
        """
        
        self.cursor.close()
        self.connection.close()
    
    def create_tables(self):
        """
        Creates the tables of our database IF the tables do not already exist within the db
        
        This makes sure that the data we collect is going to be properly stored in our database
        """
        
        self.connect_to_db()
        
        self.cursor.execute("""
                            CREATE TABLE IF NOT EXISTS simulation (
                                id SERIAL PRIMARY KEY,
                                experiment_date DATE NOT NULL,
                                hours INT NOT NULL,
                                minutes INT NOT NULL,
                                grid_height INT NOT NULL,
                                grid_width INT NOT NULL,
                                chronons_reached INT NOT NULL
                            )
                            """)
        
        self.connection.commit()
        
        self.cursor.execute("""
                            CREATE TABLE IF NOT EXISTS current_sim(
                                id SERIAL PRIMARY KEY,
                                current_chronon INT NOT NULL,
                                nb_tunas INT NOT NULL,
                                nb_sharks INT NOT NULL,
                                nb_megalodons INT NOT NULL,
                                simulation_id INT NOT NULL REFERENCES simulation(id)
                            )
                            """)
        
        self.connection.commit()
        
        self.disconnect_from_db()
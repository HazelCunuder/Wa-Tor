import psycopg2
from configparser import ConfigParser
from pathlib import Path

class DataManager:
    def __init__(self) -> None:
        self.filename = Path(__file__).parent / "database.ini"
        self.config = ConfigParser()
        self.config.read(self.filename)
        self.host = self.config["postgresql"]["host"]
        self.database = self.config["postgresql"]["database"]
        self.user = self.config["postgresql"]["user"]
        self.password = self.config["postgresql"]["password"]

    
    def connect_to_db(self) -> None:
        self.connection = psycopg2.connect(
            host= self.host,
            database=self.database, 
            user=self.user, 
            password=self.password
        )
        
        self.cursor = self.connection.cursor()
    
    def save_sim_data(self, results_dict: dict):
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
        self.cursor.close()
        self.connection.close()
        
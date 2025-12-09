import psycopg2
import datetime
from configparser import ConfigParser
from pathlib import Path

class DataManager:
    def __init__(self) -> None:
        self.filename = Path(__file__).parent / "database.ini"
        self.config = ConfigParser()
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
        pass
    
    def get_time(self):
        pass
    
    def get_date(self):
        pass
    
    def disconnect_from_db(self):
        pass
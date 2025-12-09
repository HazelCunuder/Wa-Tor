import psycopg2
import datetime
from configparser import ConfigParser
from pathlib import Path

class DataManager:
    def __init__(self, filename='database.ini', section='postgresql') -> None:
        pass
    
    def connect_to_db(self):
        pass
    
    def save_data(self):
        pass
    
    def get_time(self):
        pass
    
    def get_date(self):
        pass
    
    def disconnect_from_db(self):
        pass
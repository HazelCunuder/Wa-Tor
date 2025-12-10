class ConfigurationWator:
    def __init__(self):
      
        self.grid_width = self.ask_user_input(
            "Enter your grid width:",
            10,
            min_value=5,
            max_value=100
        )

        self.grid_height = self.ask_user_input(
            "Enter your grid height:",
            10,
            min_value=5,
            max_value=100
        )

        self.nb_tuna = self.ask_user_input(
            "Choose the number of tuna:",
            25,
            min_value=0,
            max_value=self.grid_width * self.grid_height
        )

        self.nb_shark = self.ask_user_input(
            "Choose the number of sharks:",
            1,
            min_value=0,
            max_value=self.grid_width * self.grid_height
        )

        self.time_breed_tuna = self.ask_user_input(
            "Enter the time of breed for the tunas:",
            3,
            min_value=1,
            max_value=20
        )

        self.times_breed_shark = self.ask_user_input(
            "Enter the time of breed for the sharks:",
            5,
            min_value=1,
            max_value=20
        )

        self.energy_shark = self.ask_user_input(
            "Enter the initial energy for the sharks",
            3,
            min_value=1,
            max_value=20
        )

        self.recovery_energy_shark = self.ask_user_input(
            "Choose a point of energy for the sharks when they eat a tuna",
            2,
            min_value=1,
            max_value=20
        )

        self.nb_megalodon = self.ask_user_input(
            "Choose the number of megalodons:",
            1,
            min_value=0,
            max_value=self.grid_width * self.grid_height
        )

        self.times_breed_megalodon = self.ask_user_input(
            "Enter the time of breed for the megalodons:",
            10,
            min_value=1,
            max_value=20
        )

        self.energy_megalodon = self.ask_user_input(
            "Enter the initial energy for the megalodons:",
            3,
            min_value=1,
            max_value=20
        )

        self.recovery_energy_megalodon = self.ask_user_input(
            "Choose energy points for megalodons when they eat:",
            1,
            min_value=1,
            max_value=20
        )

        self.display_summary()


    def ask_user_input(self, prompt: str, default_value: int, max_value:int, min_value:int) -> int :
        
        while True:
            user_input = input(f"{prompt}(defaut: {default_value})")
            if user_input.strip() == "":
                return default_value
            try:
                if min_value < int(user_input) < max_value:
                    return int(user_input)
                else:
                    print("Please enter a valid number")
            except ValueError:
                print("Please enter a valid number")  
                continue     

    def display_summary(self):
        print("\n===== CONFIGURATION =====")
        print(f"Grid : {self.grid_width} x {self.grid_height}")
        print(f"Tunas : {self.nb_tuna}")
        print(f"sharks : {self.nb_shark}")
        print(f"Tuna breeding time : {self.time_breed_tuna}")
        print(f"Shark breeding time: {self.times_breed_shark}")
        print(f"Énergy shark : {self.energy_shark}")
        print(f"Énergy gained : {self.recovery_energy_shark}")
        print(f"Megalodons : {self.nb_megalodon}")
        print(f"Megalodon breeding time: {self.times_breed_megalodon}")
        print(f"Energy megalodon : {self.energy_megalodon}")
        print(f"Energy gained (megalodon): {self.recovery_energy_megalodon}")
        print("=========================\n")


class ConfigurationWator:
    def __init__(self):
        self.grid_width = 10
        self.grid_height = 10
        self.nb_tuna = 25
        self.nb_shark = 1
        self.time_breed_tuna = 3
        self.times_breed_shark = 5
        self.energy_shark = 3
        self.recovery_energy_shark = 2


        self.grid_width = self.ask_user_input ("enter your grid width",self.grid_width)
        self.grid_height = self.ask_user_input ("enter your grid height",self.grid_height)
        self.nb_tuna = self.ask_user_input ("enter your number of tuna",self.nb_tuna )
        self.nb_shark = self.ask_user_input ("enter your number of shark ",self.nb_shark )
        self.time_breed_tuna = self.ask_user_input ("enter the time of breed for the tuna",self.time_breed_tuna )
        self.times_breed_shark = self.ask_user_input ("enter the time of breed for the shark",self.times_breed_shark)
        self.energy_shark = self.ask_user_input ("enter the initial energy of shark",self.energy_shark)
        self.recovery_energy_shark = self.ask_user_input ("Enter the energy gained by sharks when eating tuna",self.recovery_energy_shark)

        self.grid_width = self.ask_user_input(
            "grid width",
            self.grid_width,
            min_value=5,
            max_value=100
        )

        self.grid_height = self.ask_user_input(
            "grid height",
            self.grid_height,
            min_value=5,
            max_value=100
        )

        self.nb_tuna = self.ask_user_input(
            "Nombre de thons",
            self.nb_tuna,
            min_value=0,
            max_value=self.grid_width * self.grid_height
        )

        self.nb_shark = self.ask_user_input(
            "Nombre de requins",
            self.nb_shark,
            min_value=0,
            max_value=self.grid_width * self.grid_height
        )

        self.time_breed_tuna = self.ask_user_input(
            "Temps reproduction thons",
            self.time_breed_tuna,
            min_value=1,
            max_value=20
        )

        self.times_breed_shark = self.ask_user_input(
            "Temps reproduction requins",
            self.times_breed_shark,
            min_value=1,
            max_value=20
        )

        self.energy_shark = self.ask_user_input(
            "Énergie initiale des requins",
            self.energy_shark,
            min_value=1,
            max_value=20
        )

        self.recovery_energy_shark = self.ask_user_input(
            "Énergie gagnée en mangeant un thon",
            self.recovery_energy_shark,
            min_value=1,
            max_value=20
        )

       
        self.display_summary()


    def ask_user_input(self, prompt: str, default_value: int) -> int :
        
        while Truerue:
            user_input = input(f"[prompt](defaut: {default_calue})")
            if user_input.strip() == "":
                return default_value
            
            try:
                return int(user_input)
            except ValueError:
                print("please enter a valid number")
                continue

            if min_value is not None and value < min_value:
                print(f"Value too small (minimum : {min_value}).")
                continue

            if max_value is not None and value > max_value:
                print(f"Value too high (maximum : {max_value}).")
                continue

            return value


def display_summary(self):
    print("\n===== CONFIGURATION =====")
    print(f"Grid : {self.grid_width} x {self.grid_height}")
    print(f"Tunas : {self.nb_tuna}")
    print(f"sharks : {self.nb_shark}")
    print(f"Tuna breeding time : {self.time_breed_tuna}")
    print(f"Shark breeding time: {self.times_breed_shark}")
    print(f"Énergy shark : {self.energy_shark}")
    print(f"Énergy gained : {self.recovery_energy_shark}")
    print("=========================\n")


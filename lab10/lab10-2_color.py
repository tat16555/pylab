class autobus:
    # ANSI color codes
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'

    def __init__(self):
        print(self.GREEN + "โปรแกรมคำนวณ BMI และตรวจสุขภาพ" + self.RESET)
        self.dt = float(input(self.YELLOW + "Distance traveled? (km): " + self.RESET))
        self.set_autobus_type()

    def set_autobus_type(self):
        while True:
            try:
                self.c_ty = int(input(self.YELLOW + "autobus type? -> 1 (air conditioned autobus), 2 (autobus with fan): " + self.RESET))
                if self.c_ty in [1, 2]:
                    break
                else:
                    print(self.RED + "Invalid input. Please enter 1 or 2." + self.RESET)
            except ValueError:
                print(self.RED + "Invalid input. Please enter a number." + self.RESET)

        self.fee_text_c()
        self.Calculate_travel()

    def fee_text_c(self):
        if self.c_ty == 1:
            self.fee = 100
            self.c_ty = self.GREEN + "air conditioned autobus" + self.RESET
        else:
            self.fee = 50
            self.c_ty = self.YELLOW + "autobus with fan" + self.RESET

    def Calculate_travel(self):
        if self.dt >= 400:
            self.fpkm = 6
        elif self.dt >= 200:
            self.fpkm = 5.50
        elif self.dt >= 100:
            self.fpkm = 4
        else:
            self.fpkm = 2.5
        self.fare = (self.dt * self.fpkm) + self.fee
        self.tax = self.fare * 7 / 100
        self.net = self.fare + self.tax

    def display_info(self):
        print(self.YELLOW + "--------------------------------------------------" + self.RESET)
        print(f"Distance traveled: {self.GREEN}{int(self.dt)} Km.{self.RESET}")
        print(f"autobus type: {self.c_ty}")
        print(f"Bus operating fees : {self.GREEN if self.c_ty == 'air conditioned autobus' else self.YELLOW}{int(self.fee)} THB{self.RESET}")
        print(f"Travel cost per kilometer : {self.fpkm:.1f} THB")
        print(f"Travel costs do not include taxes.: {self.fare:.1f} THB")
        print(f"tax : {self.tax:.1f} THB")
        print(f"Net travel expenses : {self.net:.1f} THB")
        print(self.YELLOW + "--------------------------------------------------" + self.RESET)

# Example usage:
bus = autobus()
bus.display_info()

class autobus:
    def __init__(self):
        print("Fare calculator")
        self.dt = float(input("Distance traveled? (km): "))
        while True:
                self.c_ty = int(input("autobus type? -> 1 (air conditioned autobus), 2 (autobus with fan): "))
                if self.c_ty in [1, 2]:
                    break
                else:
                    print("Invalid input. Please enter 1 or 2.")
        self.fee_text_c()
        self.Calculate_travel()

    def fee_text_c(self):
        if self.c_ty == 1:
            self.fee = 100
            self.c_ty = "air conditioned autobus"
        else:
            self.fee = 50
            self.c_ty = "autobus with fan"

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
        print("--------------------------------------------------")
        print(f"Distance traveled: {int(self.dt)} Km.")
        print(f"autobus type: {self.c_ty}")
        print(f"Bus operating fees : {int(self.fee)} THB")
        print(f"Travel cost per kilometer : {self.fpkm:.1f} THB")
        print(f"Travel costs do not include taxes.: {self.fare:.1f} THB")
        print(f"tax : {self.tax:.1f} THB")
        print(f"Net travel expenses : {self.net:.1f} THB")
        print("--------------------------------------------------")

# Example usage:
bus = autobus()
bus.display_info()

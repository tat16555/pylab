class autobus:
    def __init__(self):
        print("----")
        self.month = int(input("Current meter number : "))
        while True:
                 self.lastmonth = int(input("previous meter number : "))
                 if self.lastmonth < self.month:
                     break
                 else:
                     print("Enter a new value.")
        self.Calculate_travel()

    def Calculate_travel(self):
        self.use = self.month - self.lastmonth
        if self.use <= 80:
            self.price = 4.5
        elif self.use <= 500:
            self.price =6.5
        elif self.use <= 1000:
            self.price = 8.0
        else:
            self.price = 10.0
        self.total = self.use * self.price
        self.ft = self.total * 0.75/100
        self.mai = 150
        self.vat = self.total *7/100
        self.net = self.total + self.ft + self.mai

    def display_info(self):
        print("--------------------------------------------------")
        print(f"Current meter number : {self.month:.1f}")
        print(f"previous meter number : {self.lastmonth:.1f}")
        print(f"Quantity used : {self.use:.1f}")
        print(f"Unit price : {self.price:.1f} THB")
        print(f"ft : {self.ft:.1f}")
        print(f"Maintenance cost : {self.mai:.1f} THB")
        print(f"vat : {self.vat:.1f} THB")
        print(f"net : {self.net:.1f} THB")
        print("--------------------------------------------------")

# Example usage:
bus = autobus()
bus.display_info()

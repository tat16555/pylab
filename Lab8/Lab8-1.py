import argparse

class BMI_health:
    def __init__(self, height, weight, gender):
        self.height = height
        self.weight = weight
        self.gender = gender
        self.bmi = 0
        self.Lv_health = ""
        self.calculate_bmi()
        self.health_level()

    def calculate_bmi(self):
        if self.gender == 1:
            self.bmi = self.height - 110
        else:
            self.bmi = self.height - 100

    def text_gender(self):
        if self.gender == 1:
            self.gender = "Male"
        else:
            self.gender = "Female"

    def health_level(self):
        if self.weight > self.bmi:
            self.Lv_health = "Fat"
        else:
            self.Lv_health = "Healthy"

    def display_info(self):
        print("--------------------------------------------------")
        print(f"Your Height: {int(self.height)} cm. and Weight: {int(self.weight)} kg.")
        print(f"Your Gender: {self.gender}")
        print(f"Your BMI: {self.bmi:.2f}")
        print(f"Your health level is: {self.Lv_health}")
        print("--------------------------------------------------")

def main():
    parser = argparse.ArgumentParser(description='BMI Calculation and Health Check Program')
    parser.add_argument('-H', '--height', type=float, required=True, help='Height in cm')
    parser.add_argument('-w', '--weight', type=float, required=True, help='Weight in kg')
    parser.add_argument('-g', '--gender', type=int, required=True, choices=[1, 2], help='Gender (1 for Male, 2 for Female)')
    args = parser.parse_args()

    bmi = BMI_health(args.height, args.weight, args.gender)
    bmi.display_info()

if __name__ == "__main__":
    main()

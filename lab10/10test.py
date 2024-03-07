print("----")
month = int(input("Current meter number: "))
while True:
    lastmonth = int(input("Previous meter number: "))
    if lastmonth < month:
        break
    else:
        print("Enter a new value.")

use = month - lastmonth
if use <= 80:
    price = 4.5
elif use <= 500:
    price = 6.5
elif use <= 1000:
    price = 8.0
else:
    price = 10.0

total = use * price
ft = total * 0.75 / 100
mai = 150
vat = total * 7 / 100
net = total + ft + mai

print("--------------------------------------------------")
print(f"Current meter number: {month:.1f}")
print(f"Previous meter number: {lastmonth:.1f}")
print(f"Quantity used: {use:.1f}")
print(f"Unit price: {price:.1f} THB")
print(f"FT: {ft:.1f} THB")
print(f"Maintenance cost: {mai:.1f} THB")
print(f"VAT: {vat:.1f} THB")
print(f"Net: {net:.1f} THB")
print("--------------------------------------------------")

import math

first_pizza_diameter = int(input("Anna ensimmäisen pizzan halkaisija: "))
first_pizza_price = int(input("Anna ensimmäisen pizzan hinta: "))
second_pizza_diameter = int(input("Anna toisen pizzan halkaisija: "))
second_pizza_price = int(input("Anna toisen pizzan hinta: "))

def unit_price(diameter, price):
    area = math.pi * (diameter/100/2)*2
    return price/area

uPrice1 = unit_price(first_pizza_diameter, first_pizza_price)
uPrice2 = unit_price(second_pizza_diameter, second_pizza_price)

print(f"1. pizzan yksikköhinta on {uPrice1:.2f}€/m2.")
print(f"2. pizzan yksikköhinta on {uPrice2:.2f}€/m2.")

if uPrice1 < uPrice2:
    print("Pizza 1 antaa paremman vastineen rahoillesi.")
else:
    print("Pizza 2 antaa paremman vastineen rahoillesi.")
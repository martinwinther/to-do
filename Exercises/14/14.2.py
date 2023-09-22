import functions

temperature = float(input("Enter water temperature: "))

state = functions.water_state(temperature)
print(state)
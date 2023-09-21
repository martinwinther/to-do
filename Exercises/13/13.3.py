def get_age(year_of_birth, current_year=2023):
    calculated_age = current_year - year_of_birth
    return calculated_age


year = int(input("What is your yeara of birth? "))
age = (get_age(year))
if age <= 120:
    print(age)
else:
    print("I'm sorry to hear that")

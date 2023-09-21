def get_age(year_of_birth, current_year=2023):
    calculated_age = current_year - year_of_birth
    return calculated_age


year = int(input("What is your yeara of birth? "))
print(get_age(year))

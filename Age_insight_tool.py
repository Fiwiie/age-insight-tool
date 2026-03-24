"""
Age Insight Tool

Built by Fawaz

This program:
- Collects user's name and birth year
- Calculates current age
- Predicts future age
- Calculates age in days (optional)

Created as part of my Python learning journey.
"""


def get_user_info():
    name = input("Enter your name:")
    birth_year = int(input("Enter your birth year:"))
    return name, birth_year
name,birth_year = get_user_info()
print(f"{name}, born in  {birth_year}")
print(f"Hello {name}!")
def calculate_age(birth_year):
    current_year=2026
    age = current_year-birth_year
    return age 
age = calculate_age(birth_year)
print(f"You are {age}!")
def predict_future_age(age):
    future_year = int(input("Enter a future year:"))
    current_year = 2026
    if future_year<current_year:
        print("That year is in the past!")
    else:
        future_age = age + (future_year - current_year)
        print(f"In {future_year}, you will be {future_age} years old.")
predict_future_age(age)
def age_in_days(age):
    answer = input("Do you want your age in days?(yes/no):")
    if answer.lower() == "yes":
        age_in_days=age*365
        print(f"Age in days ={age_in_days}")
age_in_days(age)







    
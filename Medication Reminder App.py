"""
Name: Yedidia Medication Reminder App
For: This is an health medication reminder programming software
Year: 2021
Version: 1
Author: Yedidia Software
(c) 2021 - Yedidia Software

This is an app that will remind my nanny about her medication

Firstly, she will enter her first name and surname
Secondly, she will enter the name of the medication
Thirdly, she will assume either it is pills or sirop or other
Fourthly, she will enter the posology as when to take the medication as well as the frequency
Fifthly, Python will remind her with a phone call

"""

#Check the patient information
patient_first_name = input("Your first name: ")
medication_name = input("Medication name: ")

#Multiple choices for the medication type
import random
list = ["Pills", "pills", "pill", "Sirop", "sirop", "Other", "other"]
item = random.choice(list)
item_prompt = input("Dear {0} what is the {1} property? Pills? Sirop? Other?: " .format(patient_first_name, medication_name))
if "Other" or "other":
    other_data = input("Name: ")
else:
    print(item)

#Posology (When to take the medication)
# first_day_medic_taken = input("When do you start to take the medication? ")
# import calendar
# calendar.setfirstweekday(0)
# frequency_medic_taken = input()

    

#----------------------------------------------------------#
# Calculate how many years you will have to commute your   #
#       given distance to achieve a moon return trip.      #
#----------------------------------------------------------#
import os

single_direction_commute = float(input("Enter commute distance (miles): "))
daily_commute = single_direction_commute * 2
weekly_commute = daily_commute * 5
yearly_commute = weekly_commute * 52
yearly_distance = yearly_commute * 1.609  # from miles to km

moon_distance = 384400 * 2  # Distance in km
years = moon_distance / yearly_distance

os.system('cls')

print(
    f"You will travel the equivalent distance of going\nto the moon and back in {years} years!")

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
total_days_age_90 = 365 * 90
total_weeks_age_90 = 52 * 90
total_months_age_90 = 12 * 90

left_days_to_live = total_days_age_90 - (int(age)*365)
left_weeks_to_live = total_weeks_age_90 - (int(age)*52)
left_months_to_live = total_months_age_90 - (int(age)*12)

print(f"You have {left_days_to_live} days, {left_weeks_to_live} weeks, and {left_months_to_live} months left.")









hourly_rate = float(input("What is your hourly rate?"))
hours_worked = int(input("How long did you work this week in hours?"))
earnings = (hourly_rate * hours_worked) * 0.85
print("this is your weekly earnings with tax: {}$".format(earnings))


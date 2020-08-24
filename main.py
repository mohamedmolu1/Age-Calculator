# Here I am going to create an age calculator 
def age_program():
  seconds_or_years = input("Give me seconds (s) or years (y)? ")
  if seconds_or_years == "s":
    # convert seconds into years
    user_value = input ("Enter the number of seconds you've lived for: ")
    print("You've lived for {} years".format(int(user_value) /60 / 60 / 24 / 365))
  elif seconds_or_years == "y":
    # convert years into seconds
    user_value = input("Enter the number of years you've lived for: ")
    print("you've lived for {} seconds ".format(int(user_value) * 365 * 24 * 60 * 60))
age_program()

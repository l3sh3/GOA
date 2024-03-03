#declaring targets for what is required
required_weight = 50
required_height = 170

#letting user to enter their results
user_weight = int(input("Enter your weihgt:"))
user_height = int(input("enter your height:"))

#sending to the screen final result of user
print(user_weight == required_weight and user_height == required_height)
print(user_weight != required_weight and user_height == required_height)
print(user_weight == required_weight or user_height == required_height)
print(user_weight == required_weight or user_height != required_height)
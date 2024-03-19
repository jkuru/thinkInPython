print("Hello world")

# Arithmetic operators

print(type(2))

print(type(42.0))

print(2 + +2)

# How many seconds are there in 42 minutes 42 seconds?
print("How many seconds are there in 42 minutes 42 seconds = ", 42 * 60 + 42)
# How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.
x: float = 10 / 1.61
print("How many miles are there in 10 kilometers? = ", x)
# If you run a 10 kilometer race in 42 minutes 42 seconds,
# what is your average pace (time per mile in minutes and seconds)?
# What is your average speed in miles per hour?
averagePace: float = 10 / ((42 * 60) + 42)
print("what is your average pace (time per mile in minutes and seconds)? = ", averagePace)
averageSpeed: float = averagePace * 3600
print("What is your average speed in miles per hour? = ", averageSpeed)
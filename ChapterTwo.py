# Exercise 2.1
# We’ve seen that n = 42 is legal. What about 42 = n?
n = 42
# assigning a variable to a numeric number is a compile error for eg: 42 = n
x = y = 1
d = 10  # ; is not allowed
b = x * y
print(b)
# Exercise 2.2
# The volume of a sphere with radius r is 43 πr3. What is the volume of a sphere with radius 5?
vol = 43 * 3.46666 * 5 ** 3
print(vol)
print(43 * 3.46666)  # 149.06638
print(5 ** 3)  # 125
print(149.06638 * 125)
# Suppose the cover price of a book is $24.95, but bookstores get a 40% discount.
# Shipping costs $3 for the first copy and 75 cents for each additional copy.
# What is the total wholesale cost for 60 copies?
cost = (24.95 / 100) * 60 * 60 + 3 + (.75 * 59)  # 24.95 / 100 - Will give me cost of 1 % ,
# multiply with 60 % will give me cost of single book
print(cost)
# If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile),
# then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again,
# what time do I get home for breakfast?
timeInSecondsForRun = (2 * ((8 * 60) + 15) + 3 * ((7 * 60) + 12))
# We converted the run time (38:06 minutes) to hours:
# There are 60 minutes in an hour. So, we divide the total run time in minutes by 60 to get the time in hours: 38.06
# minutes / 60 minutes/hour = 0.634 hours.
print(timeInSecondsForRun / 60 / 60)
# We added the run time in hours to your starting time:
# Since we want to know what time you get back for breakfast,
# we need to add the time it takes to run (0.634 hours) to the time you leave (6:52 am).
# treat 6:52 am as 6.52 hours (since there are 6 hours before 6:00 am and 0.52 for the remaining 52 minutes).
# Then, simply add the hours: 6.52 hours + 0.634 hours = 7.154 hours.
print(6.52 + (timeInSecondsForRun / 60 / 60))

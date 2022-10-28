#------Variables: Objects containing specific values.------

iAmVar = 10     # NUmeric or integer variable

iAmString = "Did you see i am string variable"  # string variable

iAmVar = iAmVar + 10        # use the value of previous variable and update it
print(iAmVar)


#------Types/class of variable------

type(iAmVar)        #nothing we will see
print(type(iAmVar))
print(type(iAmString))

#-----Rules to declare a Variable-------
# 1- The variable should use letters, numbers or underscore
# 2 - Do not start with numbers
# 3 - Spaces are no allowed
# 4 - Do not use keywords used in functions (break, media, test etc)
# 5 - Short and descriptive
# 6 - Case senstivity (lowercase and uppercase letters, lowercase should be used)

fruit_basket = "orange", "banana"
fruit_basket = 10

del fruit_basket
print(type(fruit_basket))
print(fruit_basket)
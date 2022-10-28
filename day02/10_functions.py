# DRY - is programming concept which means 
# Donot Repeat Yourself

print("I am learning python with Ammar")
print("I am learning python with Ammar")
print("I am learning python with Ammar")
print("I am learning python with Ammar")
print("I am learning python with Ammar")
print("I am learning python with Ammar")


# defining a function

# 1
def print_codanic():
    print("I am learning python with Ammar")

print_codanic()


# 2
def print_codanic():
    text = "I am learning python with Ammar"
    print(text)

print_codanic()


# 3
def print_codanic(text):
    print(text)

print_codanic("I am learning python with Ammar")

# functions also return a value
# we have two kinds of loops

# while loops
# for loops

for val in range(5, 10):
    print(val)


# arrays or list
days = ["sun", "mon", "tue", "wed", "thurs", "fri", "sat"]
for d in days:
    if d == "fri": continue     # skips fri
    print(d)
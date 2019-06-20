# variable types_of_people gets value 10
types_of_people = 10
# variable x gets string "There are 10 types of people."
x = f"There are {types_of_people} types of people."

# variable binary gets string "binary"
binary = "binary"
# variable do_not gets string "don't"
do_not = "don't"

# variable y gets string "Those who know binary and those don't."
y = f"Those who know {binary} and those {do_not}."

# outputs "There are 10 types of people."
print(x)
# outputs "Those who know binary and those don't."
print(y)

# outputs "I said: There are 10 types of people."
print(f"I said: {x}")
# outputs "I also said: Those who know binary and those don't."
print(f"I also said: {y}")

# variable hilarious gets boolean value False
hilarious = False
# variable joke_evaluation gets string "Isn't that joke so funny?! {}"
joke_evaluation = "Isn't that joke so funny?! {}"

# format method performs text replacement with value of hilarious and returns
# string "Isn't that joke so funny?! False" which is then output to stdout
print(joke_evaluation.format(hilarious))

# variable w gets "This is the left side of..."
w = "This is the left side of..."
# variable e gets "a string with a right side."
e = "a string with a right side."

# outputs "This is the left side of...a string with a right side.", the
# concatenated value of strings w and e
print(w + e)

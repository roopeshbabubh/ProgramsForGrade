# Take the input from user
string1 = str(input("Enter a string/word: ")).lower()

# Create a variable to store the string
unique_letters = ""

# Iterate the input String1
for i in string1:

    # Check if the letter already present in the unique_letters
    if i not in unique_letters:
        # Add the letter if not present
        unique_letters += i

# Print the output
print("uniqueLetters = ", ",".join(unique_letters))

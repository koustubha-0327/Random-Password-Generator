import random
import array

# required maximum password length 
# This can be adjusted to fit the length of your password.
MAXIMUM_LENGTH = 12

# declare arrays containing the characters required for our password.
# To facilitate string concatenation, characters are used.
NUM_DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
LOWERCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
					'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
					'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
					'z']

UPPERCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
					'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
					'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
					'Z']

SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
		'*', '(', ')', '<']

# combines all of the above character arrays to make a single array.
COMBINED_LIST = NUM_DIGITS + UPPERCASE_CHARACTERS + LOWERCASE_CHARACTERS + SYMBOLS

# Choose at least one character at random from each of the character sets listed above.
random_digit = random.choice(NUM_DIGITS)
random_upper = random.choice(UPPERCASE_CHARACTERS)
random_lower = random.choice(LOWERCASE_CHARACTERS)
random_symbol = random.choice(SYMBOLS)

# combine the above-mentioned characters
# The password has just four characters at this point, but
# We require a password of 12 characters.
temporary_password = random_digit + random_upper + random_lower + random_symbol


# Now that we know we have at least one character from each of the 
# character groups, we fill in the remaining 
# password length by selecting characters at random from the combined 
# list of characters above. 
for i in range(MAXIMUM_LENGTH - 4):
	temporary_password = temporary_password + random.choice(COMBINED_LIST)

	# Make a temporary password array and shuffle it.
	# Keep it from following a constant pattern,
	# If the password's beginning is predictable
	temporary_password_list = array.array('u', temporary_password)
	random.shuffle(temporary_password_list)

# add the characters to the temporary password array
# to form the password
generated_password = ""
for i in temporary_password_list:
		generated_password = generated_password + i
		
# print out the random generated password
print("Generated Password is:",generated_password)

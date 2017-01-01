from cipher import l
import time
from itertools import permutations

start = time.time()

ASCII_LOWERCASE_START = 97
ASCII_LOWERCASE_END = 122
PASSWORD_LENGTH = 3
COMMON_WORD = " the " 

# Iterate through all possible lower case three letter words
permutations = list(permutations(range(ASCII_LOWERCASE_START, ASCII_LOWERCASE_END+1), PASSWORD_LENGTH))
for permutation in permutations:
	# xor with the cipher
	decrypted_ascii = [l[i] ^ permutation[i % PASSWORD_LENGTH] for i in range(len(l))]
	# convert to english
	decrypted_english = ''.join([chr(c) for c in decrypted_ascii])
	# check if " the " is in it [not the strongest way to do this]
	if COMMON_WORD in decrypted_english:
		# print the values of the ascii characters
		print(sum(decrypted_ascii))

print(time.time() - start)
#107359
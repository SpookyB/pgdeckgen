from random import getrandbits

## Returns A∧B∧R and A∧B∧¬R where R is a random number who's bitlength
## is at most the length of the bitstring of A∧B
def oneifboth(a, b):
	conj = a & b
	rand = getrandbits(conj.bit_length())
	return conj & rand, conj & ~rand

## Returns a list of cards that exist in a deck given a bitstring
## where card numbers are represented by their position in the reverse string
def cards(binrep):
	return [pos for pos, digit in enumerate(reversed(bin(binrep))) if digit == '1']

	
## Variant 2: Power Grid with both power plant decks
## ref: http://riograndegames.com/getFile.php?id=245
def methodtwo(gy, gn):
	gy, gn = oneifboth(gy, gn)
	print("Grey cards:")
	print(cards(gy))
	print("Green cards:")
	print([1, 2] + cards(gn))
	
####   6555555555544444444443333333333222222222211111111110000000000
####   0987654321098765432109876543210987654321098765432109876543210
gy = 0b0000000000100010101011111111111111111111111111111111111111000
gn = 0b1001001010100010101011111111111111111111110011111111111111110

methodtwo(gy, gn)

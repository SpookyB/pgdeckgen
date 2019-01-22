from random import getrandbits

def oneifboth(a, b, highcard):
	conj = a & b
	rand = getrandbits(highcard)
	return rand & conj, ~rand & conj
	
def cards(binrep, highcard):
	return [pos for pos, digit in enumerate(str(bin(binrep + 2**highcard))[2:]) if digit == '1'][1:]

def methodtwo(gy, gn, highcard):
	gy, gn = oneifboth(gy, gn, highcard)
	print("Grey cards:")
	print(cards(gy, highcard))
	print("Green cards:")
	print([1, 2] + cards(gn, highcard))
	
####   000000000111111111122222222223333333333444444444455555555556
####   123456789012345678901234567890123456789012345678901234567890
gy = 0b001111111111111111111111111111111111111101010100010000000000
gn = 0b111111111111111100111111111111111111111101010100010101001001
highcard = 60

methodtwo(gy, gn, highcard)

from random import getrandbits

def oneifboth(a, b):
	conj = a & b
	rand = getrandbits(conj.bit_length())
	return conj & rand, conj & ~rand
	
def cards(binrep):
	return [pos for pos, digit in enumerate(reversed(str(bin(binrep)))) if digit == '1']

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

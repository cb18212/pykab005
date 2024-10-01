import math
#Part 1

#Task 1
def is_valid_part(part):
	part_string = str(part)

	try:
		part = int(part)
	except:
		#print(part_string, False)
		return False

	part = int(part)
	is_valid = True
	is_valid = is_valid and part >= 0 and part <= 255 #Check that part is in 0-255 range
	is_valid = is_valid and not (part_string[0]=="0" and len(part_string) > 1)
	#print(part_string, is_valid)
	return is_valid
#Task 2
def is_valid_ip(addr):
	try:
		addr = str(addr)
	except:
		print("Error Address passed was not a string.")
		return False
	components = addr.split(".")
	if len(components) != 4:
		return False

	is_valid = True
	for i in addr.split("."):
		is_valid = is_valid and is_valid_part(i)

	return is_valid

def test_1_1():
	print("\nNumber/ip component testing:")
	print("should be true: ")
	print(is_valid_part(0))
	print(is_valid_part(100))
	print(is_valid_part("100"))
	print(is_valid_part(255))
	print(is_valid_part("0"))

	print()
	print("should be false: ")
	print(is_valid_part(-1))
	print(is_valid_part("-1"))
	print(is_valid_part(507))
	print(is_valid_part("aoher"))
	print(is_valid_part("0050"))
	print(is_valid_part("05"))

	print("\nIP testing:")
	print("\nShould be true:")
	print(is_valid_ip("192.168.1.1"))  # True
	print("\nShould be false:")
	print(is_valid_ip("192.168.256.1"))  # False
	print(is_valid_ip("192.168.1"))  # False
	print(is_valid_ip("192.168.01.1"))  # False

#Part 2

#Task 1

def decimal_to_binary(n):
	str_n = str(n)
	n = int(str_n)
	remainder = n - (n//2 * 2)
	#print(n//2,remainder)
	if n == 0:
		return "0"
	elif n//2 == 0:
		return str_n
	else:
		return str(remainder) + decimal_to_binary(n//2)

print(decimal_to_binary(10))   # "1010"
print(decimal_to_binary(255))  # "11111111"
print(decimal_to_binary(1))    # "1"

#Task 2

def binary_to_decimal(n):
	if n =="": return 0
	else:
		return int(n[0])*math.pow(2,len(n)-1) + binary_to_decimal(n[1:])

print(binary_to_decimal("1010"))      # 10
print(binary_to_decimal("11111111"))  # 255
print(binary_to_decimal("1"))         # 1

#Part 3

def ip_to_binary(ip):
	if ip == "":
		result = ""
		for part in ip.split("."):
			result += decimal_to_binary(part) + "."
	else:


ip_to_binary("asethsth")
# Convert decimal subnet mask to bit representation and vice versa.

import sys

try:
    input_mask = sys.argv[1]
    to_decimal = "-d" in sys.argv
except:
    if input_mask not in locals():
        print("Provide mask to convert.")
        exit()

    to_decimal = False

def decimals_to_bits(decimal_mask):
    octets = decimal_mask.split(".")
    bits = []
    for octet in octets:
        bit_string = bin(int(octet)).replace("0b","")
        # Pad string
        if len(bit_string) < 8:
            bit_string = "0"*(8-len(bit_string))+bit_string
        bits.append(bit_string)
                

    return (".".join(bits))

def bits_to_decimals(bit_mask):
    octets = bit_mask.split(".")
    decimals = []
    for octet in octets:
        decimal_string = str(int(octet,2))

        decimals.append(decimal_string)

    return (".".join(decimals))

if __name__ == "__main__":
    if to_decimal:
        print(bits_to_decimals(input_mask))
    else:
        print(decimals_to_bits(input_mask))

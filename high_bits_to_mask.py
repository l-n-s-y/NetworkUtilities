# Convert dash notation mask to decimal notation (i.e /24 => 11111111.11111111.11111111.00000000 => 255.255.255.0)

# (Use -d to specify decimal output)

import sys, re

mask_length = 32

try:
    dash_mask = sys.argv[1]
    to_decimal = "-d" in sys.argv
except:
    if (dash_mask not in locals()):
        print("Provide mask.")
        exit()
    to_decimal = False

def dash_to_mask(dash_mask,to_decimal):
    pattern = re.compile("[/][0-9]{1,2}")
    if not pattern.search(dash_mask):
        print("Invalid dash mask format. i.e /24, /16, etc.")
        exit()


    high_bits = int(dash_mask[1:])
    bit_mask = ""
    #for i in range(high_bits):
    for i in range(mask_length):
        if i < high_bits:
            bit_mask += "1"
        else:
            bit_mask += "0"

        if (i+1)%8==0 and i != mask_length-1:
            bit_mask += "."

    if to_decimal:
        from convert_subnet_mask import bits_to_decimals
        bit_mask = bits_to_decimals(bit_mask)

    return bit_mask

if __name__ == "__main__":
    print(dash_to_mask(dash_mask,to_decimal))


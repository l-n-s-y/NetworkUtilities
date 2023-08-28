# Specify a dash-notation subnet mask to derive the number of available host addresses (including first and last unusable addresses)


import sys
from high_bits_to_mask import dash_to_mask

try:
    mask = sys.argv[1]
except:
    print("Provide mask.")
    exit()

def get_host_addr_count(mask):
    bit_mask = dash_to_mask(mask,False)

    zero_index = bit_mask.find("0")
    if zero_index == -1:
        print("No host bits in mask.")
        exit()

    host_bits = bit_mask[zero_index:]

    raw_bits = "1"*len(host_bits.replace(".","")) # Convert '0' mask bits to '1' host bits
    total_bits = 0
    for i in range(int("0b"+raw_bits,2)):
        total_bits += 1

    return total_bits


if __name__ == "__main__":
    print(get_host_addr_count(mask))

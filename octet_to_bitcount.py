# Determines the number of 1's in a given address octet.
# e.g. 192 = 0b11000000 => 2 bits

def octet_to_bitcount(o):
    try:
        o = int(o)
    except:
        return -1
    i=0;
    [i:=i+1 for b in bin(o) if b=="1"]
    return i

if __name__ == "__main__":
    from sys import argv
    try:
        bc = octet_to_bitcount(argv[1])
    except IndexError:
        print(f"usage: python3 {argv[0]} [OCTET]")
        exit()

    if (bc == -1):
        print("Invalid octet input.")
        exit()
    print(bc)

def array_packing(arr):
    binary = []
    for i in arr[::-1]:
        i_bin = bin(i)[2:]
        binary.append('0'*(8 - len(i_bin)) + i_bin)
    str_long = ''.join(binary)
#    print(str_long)
    return int(str_long, 2)

def array_packing(arr):
    return int.from_bytes(arr, 'little')

def array_packing(arr):
	return sum(num * 256**i for i, num in enumerate(arr))


def array_packing(arr):
    return int(''.join('{:08b}'.format(n) for n in reversed(arr)), 2)
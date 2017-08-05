# incomplete
a = int(input('please enter an integer: '))
src_int = a >> 4
mask_int = ~(~0<<4)
dest_int = a & mask_int
print dest_int
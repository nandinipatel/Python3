# with open("binary", 'bw') as bin_file: #b for binary and w for write
#     for i in range(17):
#         #passed a list to bytes
#         bin_file.write(bytes([i])) #converting i to byte format and writing it into binary

# with open("binary", 'br') as binFile:
#     for b in binFile:
#         print(b)

a = 65534 #FF FE
c = 65536 #00 01 00 00

with open("binary2", "bw") as bin_file:
    bin_file.write(a.to_bytes(2, 'big')) #2 is the number of bytes needed to store the value 
    bin_file.write(c.to_bytes(4, 'big'))

#reading from a binary file
with open("binary2", 'br') as binFile:
    e = int.from_bytes(binFile.read(2), 'big')
    print(e)
    f = int.from_bytes(binFile.read(4), 'big')
    print(f)
#struct

from struct import *

#store as bytes data
# pack is the function used to convert into byte format
packed_data = pack('iif',6,19,4.73) # 1st is format i for integet and f for float
print(packed_data)


#calcsize is used to convert into byte
print(calcsize('i'))
print(calcsize('f'))
print(calcsize('iif'))

#To get the bytes data back to normal
#unpack function is used to convert into the integer
original_data = unpack('iif',packed_data) #packed_data = 'b'\x06\x00\x00\x00\x13\x00\x00\x00)\\\x97@''
print(original_data)

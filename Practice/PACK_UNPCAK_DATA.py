#struct

from struct import *

#stores as bytes data
#pack is the function used to convert into bytes
packed_data = pack('iif',6,19,4.73) # 1st is the format i for integer and f for float
print(packed_data)

packed_int = pack('i',6) # gives tewlve digit and separated by slash(\) after 3 digits
print(packed_int)

packed_float = pack('f',4.78) # gives 8 digit number last digit will be @
print(packed_float)

print(calcsize('i'))#Used to calculate the size from bytes byte
print(calcsize('f'))
print(calcsize('iif'))

#To get the byte data back to normal value
#unpack is the function used to convert into original value
original_data = unpack('iif',packed_data)
print(original_data)

original_int = unpack('i',packed_int)
print(original_int)


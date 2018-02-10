import math

ab = int(input())
bc = int(input())
res = ab*ab  + bc*bc

ac = math.sqrt(res)

angle_c = math.atan2(ab,bc)
angle_in_degree = math.degrees(angle_c)
angle_mbc = 90 - angle_in_degree
print(str((angle_mbc))+"\u00b0")
print(str(int(round(math.degrees(math.atan2(ab,bc))))) + '\u00b0')
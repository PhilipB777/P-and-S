# Philip Brady
# This is the Weekly Task 3

s = input("Enter Sentence: ")
slen = len(s)

# used mod to get first character printed
if slen % 2 == 0:
    print (s[slen:0:-2])
else:
    print (s[slen:0:-2] + s[0])